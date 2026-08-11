import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Need a max heap so we'll go through each stone and heappush the negative
        # O(n*logn)
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        
        # Then continuously pop from our heap while there are at least 2 elements
        while len(h) >= 2:
            w1, w2 = -heapq.heappop(h), -heapq.heappop(h)
            
            if w1 == w2:
                continue
            else:
                heapq.heappush(h, w2-w1) # negates for us
            
        return -h[0] if h else 0

        