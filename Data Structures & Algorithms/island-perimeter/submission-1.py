class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def count_neighbor(row, col):
            count = 0
            for r, c in directions:
                if row+r < 0 or row+r == ROWS or col+c < 0 or col+c == COLS or grid[row+r][col+c] == 0:
                    count += 1
            
            return count



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res += count_neighbor(row, col) 

        return res     
        