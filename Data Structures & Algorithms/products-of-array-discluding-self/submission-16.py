class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        # Fill out the res with prefix where res[i] is the
        # product of all numbers to the left of it
        res[0] = 1
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]

        # Now we traverse backwards, keep track of postfix prod
        # and multiply at res[i]

        # postfix represents the product of the numbers to the
        # right of it 

        # start at the second last element and go until the begin
        post_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * post_prod
            post_prod = post_prod * nums[i]

        return res
