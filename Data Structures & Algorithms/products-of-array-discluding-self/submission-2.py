class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i in range(len(nums)):
            cur_prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                cur_prod *= nums[j]

            res[i] = cur_prod

        return res
