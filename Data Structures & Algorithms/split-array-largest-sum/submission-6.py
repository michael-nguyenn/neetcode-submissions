class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            prefix[i] = running_sum

        def range_sum(start, end):
            return prefix[end] - (0 if start == 0 else prefix[start - 1])

        cache = {}

        def dfs(i, splits):
            if (i, splits) in cache:
                return cache[(i, splits)]

            # Everything left is one subarray
            if splits == 1:
                return range_sum(i, len(nums) - 1)

            res = float('inf')
            # Leave at least splits - 1 elements for the remaining subarrays
            for j in range(i, len(nums) - splits + 1):
                first = range_sum(i, j)
                # First subarray only grows from here, can't beat res
                if first >= res:
                    break
                res = min(res, max(first, dfs(j + 1, splits - 1)))

            cache[(i, splits)] = res
            return res

        return dfs(0, k)