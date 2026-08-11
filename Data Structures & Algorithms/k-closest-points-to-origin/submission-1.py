import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = math.sqrt(pow(0 - x, 2) + pow(0 - y, 2))
            heap.append((dist, (x, y)))
        
        heapq.heapify(heap)
        
        while heap and k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res