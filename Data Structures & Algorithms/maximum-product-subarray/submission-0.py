class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            cur_prod = 1
            for j in range(i, len(nums)):
                cur_prod *= nums[j]
                res = max(cur_prod, res)

        return res