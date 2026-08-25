import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        res = []

        if a > 0:
            heapq.heappush_max(heap,(a, 'a'))
        if b > 0:
            heapq.heappush_max(heap, (b, 'b'))
        if c > 0:
            heapq.heappush_max(heap, (c, 'c'))
        
        while heap:
            num, char = heapq.heappop_max(heap)
            if not res or char != res[-1]:
                for i in range(min(2,num)):
                    res.append(char)
            
                if num - 2 > 0:
                    heapq.heappush_max(heap, (num - 2, char))
            else:
                if not heap:
                    break
                
                num2, char2 = heapq.heappop_max(heap)
                res.append(char2)
                
                # push original and second back on
                heapq.heappush_max(heap, (num, char))

                if num2 - 1 > 0:
                    heapq.heappush_max(heap, (num2 - 1, char2))

        return "".join(res)