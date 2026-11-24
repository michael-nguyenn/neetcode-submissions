"""
Problem
- given array of ints represent coin denominations, and a target amount 
- need to return the number of distinct combinations that total to that amount

Example 4 [1,2,3]
dfs(0, 0) []
- take 1
    dfs(0, 1) [1]
    - take 1
        dfs(0, 2) [1, 1]
        - take 1
            dfs(0, 3) [1, 1, 1]
            - take 1
                dfs(0, 4) [1, 1, 1, 1]
                -> base case return 1
            - don't take 1
                dfs(1, 3) [1, 1, 1]
                - take 2
                    dfs(1, 5) [1, 1, 1, 2]
                    -> base case return 0
                - don't take 2
                    dfs(2, 3) [1, 1, 1]
                    - take 3
                        dfs(2, 6) [1, 1, 1, 3]
                        -> base case return 0
                    - don't take 3
                        dfs(3, 3)
                        -> base case return 0 (idx out of bounds)
                    -> return 0 
                -> return 0
            -> return 1 + 0
        - don't take 1
            dfs(1, 2) [1, 1]
            - take 2
                dfs(1, 4) [1, 1, 2]
                -> base case return 1
            - don't take 2 
                dfs(2, 5) [1, 1, 3]
                -> base case return 0
            -> return 1
        -> return 1 + 1 = 2
    - don't take 1 
        dfs(1, 1) [1]
        - take 2 
            dfs(1, 3) [1, 2]
            - take 2
                dfs(1, 5) [1, 2, 2]
                -> base case return 0
            - don't take 2
                dfs(2, 3) [1, 2]
                - take 3
                    dfs(2, 6) [1, 2, 3]
                    -> base case return 0
                - don't take 3
                    dfs(3, 3)
                    -> base case return 0
                -> return 0
            -> return 0
        - don't take 2
            dfs(2, 1) [1]
            - take 3
                dfs(2, 4) [1, 3]
                -> base case return 1
            - don't take 3
                dfs(3, 1)
                -> bc return 0
            -> return 1
        -> return 1
    -> return 1
- don't take 1
    dfs(1, 0) []
    - take 2
        dfs(1, 2) [2]
        - take 2   
            dfs(1, 4) [2, 2]
            -> base case return 1
        - don't take 2
            dfs(2, 2) [2]
            - take 3
                dfs(2, 5)
                -> base case return 0
            - don't take 3
                dfs(3, 2)
                -> base case return 0
            -> RET 0
        -> RET 0
    - don't take 2
        dfs(2, 0)
            
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, total):
            if i == len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            if (i, total) in cache:
                return cache[(i, total)]
            
            # we either take the coin at index of i or not
            cache[(i, total)] = dfs(i, total+coins[i]) + dfs(i+1, total)
            return cache[(i, total)]
        
        return dfs(0, 0)
        