from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(row, col):
            q = deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                for r, c in directions:
                    cur_row = row + r
                    cur_col = col + c

                    if (cur_row < 0 or cur_col < 0 or 
                        cur_row == ROWS or cur_col == COLS or
                        (cur_row, cur_col) in visited or
                        grid[cur_row][cur_col] == "0"
                        ):
                        continue
                    
                    visited.add((cur_row, cur_col))
                    q.append((cur_row, cur_col))
                    

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == "1":
                    res += 1
                    bfs(row, col)
        
        return res