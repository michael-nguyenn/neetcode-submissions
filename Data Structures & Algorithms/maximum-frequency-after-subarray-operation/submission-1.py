"""
[2,1,1,2,2] k = 1
k_count = 2
res  = 2

v = 1, skip
v = 2, cur = 0 
    - i=0, 2 == v, increment cur
    - i=1, 1 == k, decrement cur
    - i=2, 1 == k, decrement cur
        - we reset cur since it's negative now
    - i=3, 2==v, increment cur
    - i=4, 2==v, increment cur

- we should go in range of 1 -> max(nums), we skip over k b/c it doesn't make sense
"""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        total_k = nums.count(k)
        max_v = max(nums)
        res = total_k
        
        for val in range(1, max_v+1):
            if val == k:
                continue
            
            cur = 0 # reps # of nums we can change to k
            for num in nums:
                cur = max(cur, 0)

                if num == val:
                    cur += 1
                elif num == k:
                    cur -= 1 # we're losing a k here
                
                
                res = max(res, cur+total_k)
        
        return res


        