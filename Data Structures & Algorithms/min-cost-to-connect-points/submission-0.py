class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        point_map = {(x, y): [] for x, y in points}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                if i == j:
                    continue

                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                point_map[(x1, y1)].append((dist, (x2, y2)))


        start = tuple(points[0])
        visited.add(start)
        heap = point_map[start][:]
        heapq.heapify(heap)
        
        while len(visited) < len(points):
            dist, point = heapq.heappop(heap)

            if point in visited:
                continue
            
            res += dist
            visited.add(point)
            
            for edge in point_map[point]:
                heapq.heappush(heap, edge)
        
        return res
            
