import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # this holds the larger half of elements
        self.max_heap = [] # this holds the smallere half of elements

    def addNum(self, num: int) -> None:

        if len(self.min_heap) == 0 or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        # Rebalance if we must
        if len(self.min_heap) - len(self.max_heap) > 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
        if len(self.max_heap) - len(self.min_heap) > 0:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)


    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        