class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # set an arbitrary value
        left, right = 0, len(nums) - 1

        while left <= right:
            # special case where we're in a sorted portion,
            # we can just take the smallest element
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break

            # otherwise perform special binary
            mid = (left + right) // 2
            res = min(nums[mid], res)

            # means we're in the larger (rotated portion)
            # and we should move --> to enter the smaller portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                # this means we're in the smaller portion, there's no point 
                # in searching right cause every element is larger
                # we move right to potentially enter an even smaller portion
                right = mid - 1

        return res

            