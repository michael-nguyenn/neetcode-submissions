"""
Problem
Array has been rotated, aka shifted --> between 1-n times. Need to find
a target, and return the index

Strategy
- In a rotated array, the array is partitioned into two halves. 
- A left half where all elements are greater than a right half
- We're in a left half if mid is >= left
- Otherwise we're in the right half
- If we're in the left half the target is out of range if
    target is < left or target is > mid
    move left up
- If we're in the right half the target is out of range if
    target is > right or < mid
    move right down
- What if we end up in a sorted half?

Example
 0 1 2 3 4 5
[3,4,5,6,1,2], target = 1
- l = 0, r = 5, m = 2
- we in left half, 1 is less than left which means it's in the right half
and we move the left pointer mid + 1
- l = 3, r = 5, m = 4
- target is found and we move on

 0 1 2 3 4
[5 1 2 3 4] target = 5
l = 0, r = 4 m = 2
- 2 is < 5 so we're in the right half
- target is in this half so then we search left 
- l = 0, r = 1, m = 1
- 1 is < 5, so we're in the right half
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid-1
                else:
                    left = mid+1
        
        return -1


        