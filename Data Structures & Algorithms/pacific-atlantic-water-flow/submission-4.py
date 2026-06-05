class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        def dfs(r, c, visited, prev_height):
                if ((r,c) in visited or 
                    r < 0 or c < 0 or 
                    r == ROWS or c == COLS or 
                    heights[r][c] < prev_height):
                    return

                # Means we're finding a new valid cell
                visited.add((r, c))

                for row, col in directions:
                    dfs(r + row, c + col, visited, heights[r][c])

        # Go through the top/bottomo rows
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c]) # find all cells that can flow to pacific
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])

        # Go through the left/right sides
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        # Then go through the whole grid and get the intersection
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        
        return res

