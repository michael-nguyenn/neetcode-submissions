class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        res = nums[0]

        for num in nums:
            temp = cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(num * temp, num * cur_min, num)
            res = max(cur_max, res)

        return res