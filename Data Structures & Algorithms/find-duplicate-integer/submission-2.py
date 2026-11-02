"""
Problem
- array of size 5, holds 6 integers [1,2,3,4,5]
- there is one number that repeats, every other appears once

Example
[1,2,3,2,2] 
- index 0 maps to 1
- index 1 maps to 2
- index 2 maps to 3
- index 3 maps to 2
- cycle

[1,2,3,4,4] size 4 but contains 5 in range of [1,4],  [1,2,3,4,4]
- index 0 maps to 1
- index 1 maps to 2
- index 2 maps to 3
- index 3 maps to 4
- index 4 maps to 4
- index 4 maps to 4

Strategy
- nums[i] gives us the next element
- nums[nums[i]] gives us the next next
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                break

        cur = 0
        while True:
            cur = nums[cur]
            slow = nums[slow]

            if cur == slow:
                return cur


        