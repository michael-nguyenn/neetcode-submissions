import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        res = []

        for num in arr:
            heapq.heappush_max(heap, ((abs(x - num)), num))

            if len(heap) > k:
                heapq.heappop_max(heap)
        
        while heap:
            _, num = heapq.heappop_max(heap)
            res.append(num)
        
        res.sort()
        return res