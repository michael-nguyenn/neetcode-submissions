class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def find_rest(row, col):
            if (row < 0 or col < 0 or 
                row == ROWS or col == COLS or 
                (row, col) in visited or 
                grid[row][col] == "0"):
                return False
            
            visited.add((row, col))

            for r, c in directions:
                find_rest(row + r, col + c)
        
        
        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) not in visited) and grid[row][col] == "1":
                    res += 1
                    find_rest(row, col)

        return res