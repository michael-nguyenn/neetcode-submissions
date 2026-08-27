class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [0] * (len(edges) + 1)
        parent = [i for i in range(len(edges) + 1)]
        
        def find(node: int) -> int:
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1: int, node2: int) -> bool:
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False
            
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
            elif rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
            else:
                parent[parent2] = parent1
                rank[parent1] += 1
            
            return True
        
        for src, dst in edges:
            if not union(src, dst):
                return [src, dst]
        