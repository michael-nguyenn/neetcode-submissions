class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[None for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        def dfs(i:int, j:int) -> int:
            if cache[i][j]:
                return cache[i][j]
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            shortest = 0
            if word1[i] == word2[j]:
                shortest += dfs(i+1, j+1)
            else:
                shortest += 1 + min(
                    dfs(i, j+1),
                    dfs(i+1, j),
                    dfs(i+1, j+1)
                )
            
            cache[i][j] = shortest
            return shortest
        
        return dfs(0, 0)


