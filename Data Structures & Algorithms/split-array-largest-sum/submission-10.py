"""
Strategy
- We can perform binary search on the range of possible answers
- The smallest max subarray would be the largest number in the array
- The largest will be the sum of the subarray (technically we can never have this answer, but it helps narrow down the search space)

- We calculate the mid point, and then we check if that value is valid
- To determine if a value is valid we greedily create subarrays until they're greater than the mid point value. Once we're past that one, we create a new subarray.
- If we can create subarrays less than k, where all of them are less than the mid value, this number if feasible. This is the case because if we have < k subarrays all less than mid, then if we split a subarray again until we satisfy the k splits, all are guaranteed to be less than k
- If we are unable to do that, then it's impossible and the mid value is too small.
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def feasible(max_value):
            subarrays = 1
            max_sum = 0

            for num in nums:
                max_sum += num
                if max_sum > max_value:
                    subarrays += 1
                    max_sum = num
                
                if subarrays > k:
                    return False
            
            return True
                
        while left <= right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        