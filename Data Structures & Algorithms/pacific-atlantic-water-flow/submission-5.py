# 8:32
# graph traversal
# pacific ocean = top row / first column
# atlantic ocean = bot row / right column
# start at the edges and then see how far in we can go
# use two sets of visited, then take the union of both
# we're allowed to go in if the neighbor is greater or equal to
# our cell

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(0,1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        pacific = set()
        atlantic = set()

        def dfs(row, col, seen):            
            for r,c in DIRECTIONS:
                new_r = row + r
                new_c = col + c
                if (new_r < 0 or new_r == ROWS or 
                    new_c < 0 or new_c == COLS or 
                    (new_r, new_c) in seen or
                    heights[new_r][new_c] < heights[row][col]):
                    continue

                seen.add((new_r, new_c))
                dfs(new_r, new_c, seen)

        # Go through top/bottom row
        for i in range(COLS):
            if (0, i) not in pacific:
                pacific.add((0,i))
                dfs(0, i, pacific)
        
            last_row = ROWS - 1
            if (last_row, i) not in atlantic:
                atlantic.add((last_row, i))
                dfs(last_row, i, atlantic)
        
        # Go through left/right side
        for i in range(ROWS):
            if (i, 0) not in pacific:
                pacific.add((i, 0))
                dfs(i, 0, pacific)
            
            last_col = COLS - 1
            if (i, last_col) not in atlantic:
                atlantic.add((i, last_col))
                dfs(i, last_col, atlantic)
        
        # now how do we get the union of the two sets?
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r,c])
 
        return res
        