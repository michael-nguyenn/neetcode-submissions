"""
Problem
- The key insight is partitioning your array into two groups of stones, and then
finding the smallest difference between their sums.
- The difference between two stones is their absolute difference
- 
          0 1 2 3 4 5 6
Example  [2,7,4,1,8,1]

stone_sum = 23
target = (23 + 1) // 2 = 12

dfs(0, 0)
    dfs(1, 0)
        dfs(2, 0)
            dfs(3, 0)
                dfs(4, 0)
                - Receives 21 and 5, picks 5
                    dfs(5, 0)
                    - Receives 23, and 21, picks 21
                        dfs(6, 0) -> [] and [2,7,4,1,8,1]
                        - 0 - (23 - 0) = 23
                        - Returns 23
                        dfs(6, 1)
                        - 1 - (23 - 1) = 21
                        - Returns 21
                    dfs(5, 8)
                    - Receives 7 and 5, picks 5
                        dfs(6, 8)
                        - 8 - (23 - 8) = 7
                        - Returns 7
                        dfs(6, 9)
                        - 9 - (23 - 9) = 5
                        - Returns 5
                dfs(4, 1)
                    dfs(5, 1)
                    - Receives 21 and 19, picks 19
                        dfs(6, 1)
                        - Same as above, returns 21
                        dfs(6, 2)
                        - 2 - (23 - 2) = 19
                        - Returns 19
                    dfs(5, 9)
                    - Receives 5 and 3, returns 3
                        dfs(6, 9) -> [1, 8] and [2, 7, 1, 4]
                        - Same as above, returns 5
                        dfs(6, 10) -> [1, 1, 8] and [2, 7, 4]
                        - 10 - (23 - 10) = 3
                        - Returns 3
            dfs(3, 4)
        dfs(2, 7)  
    dfs(1, 2)

"""

# Try to partition the set so both sides cancel one another out
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # First get all the weights of the stones
        total_weight = sum(stones)
        half = (total_weight + 1) // 2
        cache = {} # (idx, total) -> minimum difference

        # Total starts at 1, and we want to get it as close as possible to half
        # That would give a 0 aka no stones left
        def dfs(idx, total):
            if (idx, total) in cache:
                return cache[(idx, total)]

            if total >= half or idx == len(stones):
                cur_dif = abs((total_weight-total) - total)
                cache[(idx, total)] = cur_dif
                return cur_dif
            
            # Otherwise, at the current index, we either use this
            # weight in the left partition or we don't
            cache[(idx, total)] = min(
                dfs(idx+1, total),
                dfs(idx+1, total+stones[idx])
            )
            return cache[(idx, total)]

        return dfs(0, 0)
            
        