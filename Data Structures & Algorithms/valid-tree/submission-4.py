"""
Problem
- We're given n which represents the number of nodes in the tree from 0-n-1
- We're also given their undirected edges
- We need to see if the edges makes a valid tree
- A tree is valid if it is connected, and there is no cycle

Strategy
- Make an adj list, spawn a BFS on the adj list, if we come accross a cycle then we're gg
- At the end compare the seen set with n to see if everything was connected

Example
{
    0: [1]
    1: [0, 2, 3, 4]
    2: [1, 3]
    3: [1, 2]
    4: [1]
}   

- q entry can be (child, parent)
- Visited = 0, 1, 2, 3
- Start with 0, add its children to the q
- Pop 1 from the q, append 2, 3, and 4 to the q
- Pop 2 from the q, append 3
- Pop 3 from the q, append 2 to the q
- Pop 4 return
- Pop 3 from the q, see that it's already visited and return false

Edge Cases
- 1 node -> return True, BFS will handle this fine
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        q = collections.deque()
        visited = set()
        q.append((0, 0))

        while q:
            node, parent = q.popleft()

            if node in visited:
                return False
            
            visited.add(node)

            for child in adj[node]:
                if child != parent:
                    q.append((child, node))
        
        return len(visited) == n

        