# undirected graph 1 -> n
# no cycles and has n - 1 edges
# 1 - 2 - 4 - 3 n = 4, edges = 3

# one extra edge gets added in making a cycle then
# given as an array of edges -> make an adj list

# return the edge that can be removed to make it connected still

# we can use a set to track cycles or not
# what happens when we find a cycle though, how do we figure out which one to remove?
# oh you can remove any edge in the cycle and it will remain connected

# so you can dfs, accounting for going backwards as not a cycle, but the moment
# a node gets revisited from a different node then we can remove that edge

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]
    
        # prev_node is used to help account for undirected-ness
        def dfs(node: int, pre_node: int):
            # base case: if this node is in visited, we want to return that edge
            if visit[node]:
                return True
            
            visit[node] = True

            for neigh in adj[node]:
                if neigh == pre_node:
                    continue
                if dfs(neigh, node):
                    return True
            
            return False
        
        # adj list -> 1:2 | 2:1
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            visit = [False] * (len(edges) + 1) # [False, False, ..., False]
            
            if dfs(src, -1):
                return [src, dst]
        
        return []
