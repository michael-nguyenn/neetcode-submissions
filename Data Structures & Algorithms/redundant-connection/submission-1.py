class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(len(edges) + 1)}
        visited = set()

        def dfs(node, parent) -> bool:
            if node in visited:
                return True
            
            visited.add(node)

            for neigh in adj_list[node]:
                if neigh == parent:
                    continue
                if dfs(neigh, node):
                    return True
            
            return False
        
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

            if dfs(src, -1):
                return [src, dst]

            visited.clear()

        return []

 
        