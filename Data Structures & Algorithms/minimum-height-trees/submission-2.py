from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        res = []
        min_height = math.inf
        adj_list = {i:[] for i in range(n)}
        
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        for i in range(n):
            q = deque()
            q.append(i)
            visited = set()
            visited.add(i)
            height = 0

            while q:
                height += 1
                for _ in range(len(q)):
                    node = q.popleft()

                    for neigh in adj_list[node]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)

            if height < min_height:
                res = [i]
                min_height = height
            elif height == min_height:
                res.append(i)
            else:
                continue

        return res
                           