import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0} # dp[i] represents the min amount of coins it takes to sum to i

        def find_coin_amount(amount: int) -> int:
            if amount < 0:
                return math.inf
            if amount in dp:
                return dp[amount]
            
            res = math.inf
            for coin in coins:
                res = min(find_coin_amount(amount - coin), res)
            
            res += 1
            dp[amount] = res
            return res
        
        res = find_coin_amount(amount)
        return -1 if res == math.inf else res
            