"""
Problem
- break up 's' into as many substrings as possible (from dictionary)
- return the minimum # of breaks needed

Strategy
- for each index in s, try to match to a dictionary word, anytime we match a dic word, that's a potential partition.
- if we cannot form a word at a given index, then that becomes a partition itself

Example "neetcodes"
backtrack(0)
- scans from 0, neet matches so we do 1 + backtrack(4)
    backtrack(4)
    - scans from 4, code matches so we do 1 + backtrack(8)
        backtrack(8)
        - finds nothing at s, so we do 1 + backtrack(9)
            backtrack(9)
            - base case returns 0
        - returns 1
    - codes doesn't match so we return 2
- continue scannng and see that neetcode matches, so we do 1 + backtrack(8)
    backtrack(8)
    - find nothing blah blah
"""
# import sys
# sys.setrecursionlimit(20000)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        cache = {len(s): 0}
        dictionary = set(dictionary)

        def dfs(start) -> int:
            if start in cache:
                return cache[start]
            
            res = float('inf')
            for i in range(start, len(s)):
                if s[start:i+1] in dictionary:
                    res = min(res, dfs(i+1))
            
            res = min(res, 1 + dfs(start+1)) # this is the case where nothing matches

            cache[start] = res
            return res
                
        dfs(0)
        return cache[0]

        