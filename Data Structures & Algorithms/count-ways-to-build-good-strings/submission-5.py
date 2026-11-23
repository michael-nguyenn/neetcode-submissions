class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high + max(zero, one))]
        dp[high] = 1

        for i in range(high-1, -1, -1):
            dp[i] = dp[i+zero] + dp[i+one]
            
            if i >= low:
                dp[i] += 1
        
        return dp[0] % 1000000007


