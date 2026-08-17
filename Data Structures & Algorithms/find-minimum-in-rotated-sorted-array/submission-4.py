class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_num = float('inf') # can also initialize to any num in nums

        while left <= right:
            # if this portion of nums is already sorted
            # then we can record what's at left and return
            if nums[left] <= nums[right]:
                return min(min_num, nums[left])

            mid = (left + right) // 2

            # If we're in the left larger portion
            if nums[mid] >= nums[left]:
                left = mid + 1
            # Otherwise we're in the smaller portion
            # we'll record the num and search <-- for potentially
            # smaller
            else:
                right = mid - 1
                min_num = min(min_num, nums[mid])
            
        return min_num

