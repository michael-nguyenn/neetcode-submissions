"""
Problem
- given a binary string, and starting in index 0
- you can move from i to j if
    - i + minJump <= j <= min(i + maxJump, end of arr)
    - s[j] == 0
- so you can jump between minJump -> maxJump and if the spot is 0

Example 1
dfs(0)
    can jump between 0+2 -> 0+4
    dfs(4)
        can jump between 6 (4+2) and 7 (end of arr)
        dfs(7) we at the end so return true
"""
import sys
sys.setrecursionlimit(10000)


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        nums = list(s)
        cache = {len(nums)-1: True} # i -> able to get to end or not
        
        def dfs(i):
            if i in cache:
                return cache[i]
            
            end = min(i+maxJump, len(nums)-1)
            for jump in range(i+minJump, end+1):
                if nums[jump] == '0':
                    if dfs(jump):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False
        
        return dfs(0)

        