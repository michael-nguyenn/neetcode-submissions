"""
So starting at the last idx - len(nums) - 1, we can set that to 0

dp[5] = 0
dp[4] = min(1 + dp[4 + j]) for j in range(1 - nums[i])
dp[4] = 1 + dp[5] = 1
dp[3] = 1 + dp[4] = 2
dp[2] = 1 + dp[3] = 3
dp[1] = 1 + min(dp[2], dp[3], dp[4], dp[5]) = 1
dp[0] = 1 + dp[1] = 2
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        dp = [float("infinity")] * len(nums)
        dp[-1] = 0
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0:
                continue # remains infinity
            for j in range(1, nums[i]+1):
                if i + j < len(nums):
                    dp[i] = min(1 + dp[i + j], dp[i])
        
        return dp[0]
        