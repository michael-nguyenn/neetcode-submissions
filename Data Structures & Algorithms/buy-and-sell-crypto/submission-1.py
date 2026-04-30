class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left, right = 0, 1

        while right < len(prices):
            # profit case
            if prices[left] <= prices[right]:
                profit = prices[right] - prices[left]
                res = max(profit, res)
            # non profit
            else:
                left = right
            
            right += 1 # right will move regardless
        
        return res