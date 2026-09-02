import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profits = []
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)
        
        for _ in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(max_profits, -p)
            
            if not max_profits:
                break

            w += -heapq.heappop(max_profits)
        
        return w

        