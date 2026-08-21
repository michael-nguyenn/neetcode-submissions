import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        res = []

        for num in arr:
            heapq.heappush(heap, (-(abs(x - num)), -num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            _, num = heapq.heappop(heap)
            res.append(-num)
        
        res.sort()
        return res