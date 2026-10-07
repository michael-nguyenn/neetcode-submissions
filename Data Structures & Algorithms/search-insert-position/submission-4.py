"""
Problem
- Binary Search the nums for target. 
- If the target isn't found then we need to return the index where it's supposed to be at
- Which means we're finding the left most number >= to

Example [-1,0,2,4,6,8] target = 5 index 0-5
- mid = 2, num is < target, search right
- mid = 4, num is > target, search left
- left = 3, right = 3
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if right <= len(nums) and nums[mid] >= target:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

        