""" 
Problem
- nums array and integer k, return true if there exists a good subarray
- good subarray
    - length >= 2
    - sum of elements is a multiple of k
- How do you determine if x is a multiple of k?
    - x must be larger than k
    - when k must divide fully into x as in an int type
        - we could do if x / k == x // k

Strategy
- We need to test out every subarray right?
- [23], [23, 2], [23, 2, 6], [23, 2, 6, 4], [23, 2, 6, 4, 7]
- [2], [2, 6], [2, 6, 4], [2, 6, 4, 7]
- [6], [6, 4], [6, 4, 7]
- [4], [4, 7]
- [7]

- prefix [23, 25, 31, 35, 42]
    - To get from 0:0 -> take whatever number you're at
    - To get 1:1 -> Take prefix[1] minute prefix[1-1] = 2
    - To get 2:3 -> prefix[3] - prefix[1]
    - prefix[j] - prefix[i-1] (unless i == 0)
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0 for _ in range(len(nums))]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix[i] = total

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                cur_sum = prefix[j] if i == 0 else prefix[j] - prefix[i-1]

                if cur_sum / k == cur_sum // k:
                    return True
        
        return False


                
        



