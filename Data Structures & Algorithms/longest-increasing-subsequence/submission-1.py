class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            cur = 0

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cur = max(dfs(j), cur)
            
            memo[i] = 1 + cur
            return 1 + cur
        

        for i in range(len(nums)):
            res = max(res, dfs(i))
        
        return res