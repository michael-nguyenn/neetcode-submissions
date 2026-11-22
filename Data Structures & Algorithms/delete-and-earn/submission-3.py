"""
- if we take one number, we should always take all of them
- if we skip one number, we should skip all of them
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cache = {}
        nums.sort()

        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(nums):
                return 0

            j = i # j is the index of the last duplicate of nums[i]
            while j+1 < len(nums) and nums[j] == nums[j+1]:
                j += 1

            # if we take, we should take all and then skip 
            k = j 
            while k+1 < len(nums) and nums[k+1] - nums[j] == 1:
                k += 1

            cache[i] = max((j-i+1) * nums[i] + dfs(k+1), dfs(j+1))
            return cache[i]
        
        return dfs(0)

            
