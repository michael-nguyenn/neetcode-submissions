"""
Problem
- positive nums array, want to see if we can split into two halves where each half equals one another

Strategy
- since we're spliting into two halves that have to equal one another we could sum up the entire nums
    -> return early if that sum isn't % 2 
- spliting up the sum also gives us the exact target needed for one half
- we can include/exclude a num where exlcude means second partition, if we can find a subset where include's total == half, then that's our true case

Cases
- if our partition sum == half -> true 
- if parition sum > half -> false
- if i == len(nums) -> false (this means our partition sum is too small)

Example [1,2,3,4] total = 10 half = 5
dfs(0, 0) idx, partition1_sum
- take 1 
    dfs(1, 1)
    - take 2 
        dfs(2, 3)
        - take 3
            dfs(3, 6)
            -> over our half point, can return False
        - skip 3
            dfs(3, 3)
            - take 4
                dfs(4, 7)
                -> over our half point, can return False
            - skip 4
                dfs(4, 3)
                -> i == len(nums) -> return False
            -> return False
        -> return False
    - skip 2
        dfs(2, 1)
        - take 3
            dfs(3, 4)
            - take 4
                dfs(4, 8)
                -> over half -> False
            - skip 4
                dfs(4, 4)
                -> under half -> False
            -> return False
        - ignore 3
            dfs(3, 1)
            - take 4
                dfs(4, 5)
                -> == half way -> return True
            -> returns True
        -> returns True
    -> returns True
-> returns True
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        memo = {}

        def dfs(i, cur_sum):
            if cur_sum == half:
                return True
            if i == len(nums) or cur_sum > half:
                return False
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = (dfs(i + 1, cur_sum + nums[i]) or dfs(i + 1, cur_sum))
            
            return memo[(i, cur_sum)]
        
        return dfs(0, 0)
        