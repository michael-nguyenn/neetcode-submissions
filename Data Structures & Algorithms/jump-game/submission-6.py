class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [ False for _ in range(len(nums))]
        dp[len(nums) - 1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            for step in range(1, nums[i] + 1):
                if i + step < len(nums):
                    dp[i] = dp[i + step]
                if dp[i]:
                    break

        return dp[0]