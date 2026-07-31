class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {0: 1}

        def dfs(sum: int) -> int:
            if sum < 0:
                return 0

            if sum in memo:
                return memo[sum]
            
            res = 0

            for num in nums:
                res += dfs(sum - num)
            
            memo[sum] = res
            return res

        return dfs(target)
        