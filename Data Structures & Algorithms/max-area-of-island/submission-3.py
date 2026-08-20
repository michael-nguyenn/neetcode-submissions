# DFS SOLUTION

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0

        def find_area(row, col):
            if (row < 0 or row == ROWS or 
                col < 0 or col == COLS or 
                grid[row][col] == 0):
                return 0
            
            # sink the island then get the area of surrounding islands
            area = 1 # accounts for the current island
            grid[row][col] = 0

            for r, c in directions:
                area += find_area(row + r, col + c)
            
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, find_area(row, col))

        return max_area


        