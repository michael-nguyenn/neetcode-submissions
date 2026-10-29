class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, t):
            if i == len(nums):
                return 1 if t == target else 0
            if (i, t) in cache:
                return cache[(i, t)]

            res = dfs(i+1, t+nums[i])
            res += dfs(i+1, t-nums[i])
            cache[(i, t)] = res
            return res

        return dfs(0, 0)
        
        