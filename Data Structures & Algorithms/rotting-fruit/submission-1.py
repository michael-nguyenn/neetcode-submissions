from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()
        visit = set()
        min_mins, fresh = 0, 0

        # go through each cell and load up the rotten ones
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visit.add((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        
        # now we'll drain the q one level at a time
        # each time we complete a level, we check if we've rotted anything and increment
        while q:
            has_rot = False
            for _ in range(len(q)):
                row, col = q.popleft()

                for r, c in directions:
                    # ignore invalid directions
                    new_r, new_c = row + r, col + c

                    if (new_r < 0 or new_r == ROWS or 
                        new_c < 0 or new_c == COLS or
                        (new_r, new_c) in visit or
                        grid[new_r][new_c] == 0):
                        continue
                    
                    # otherwise the new cell is a fresh fruit and we'll rot it
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
                    visit.add((new_r, new_c))
                    has_rot = True
                    fresh -= 1
                    
            # Increment at the end of level
            if has_rot:
                min_mins += 1
        

        return min_mins if fresh == 0 else -1


        