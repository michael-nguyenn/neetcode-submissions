class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Since there's repeated work we can store (i,j) -> int
        memo = {}

        def dfs(i: int, j:int) -> int:
            if i == len(text1):
                return 0
            if j == len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                longest = 1 + dfs(i + 1, j + 1)
                memo[(i, j)] = longest
                return longest
            else:
                longest = max(dfs(i + 1, j), dfs(i, j + 1))
                memo[(i, j)] = longest
                return longest
        
        return dfs(0, 0)

        