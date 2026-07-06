class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(20000)
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        memo = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[i,j]

            longest_path = 1

            for r, c in directions:
                if 0 <= i + r < ROWS and 0 <= j + c < COLS and matrix[i][j] < matrix[i + r][j + c]:
                    longest_path = max(longest_path, 1 + dfs(i + r, j + c))
            
            memo[i,j] = longest_path
            return longest_path

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(dfs(i, j), res)
        
        return res