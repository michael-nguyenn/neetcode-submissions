# 2 * 4 = 8 * -3 = -24 * 5 = -120 * -1 = 120 <- depending on negatives we could flip flop
# -3 * 0 = 0 * -2 = 0 <- 0s including a zero destroys our number

# brute force would be a nested loop, and calculate every single subarray, and track with res
# we can optimize this by using a cur_max, cur_min, whichever multiplies and gives the largest
# we can use that to compare to res

# for zeros we need to reset the cur_min and cur_max, since the moment we include a zero we reset everything
# when calculating cur_min, cur_max it could also be the element we're considering

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_max, cur_min = 1, 1

        for i in range(len(nums)):
            temp = cur_max
            cur_max = max(cur_max * nums[i], cur_min * nums[i], nums[i])
            cur_min = min(temp * nums[i], cur_min * nums[i], nums[i])
            res = max(cur_max, res)

        return res

        