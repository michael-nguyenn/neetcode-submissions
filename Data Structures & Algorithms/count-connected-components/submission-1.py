class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        components = 0

        def dfs(node: int):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)
            
        for node in adj:
            if node not in visited:
                components += 1
                dfs(node)

        return components