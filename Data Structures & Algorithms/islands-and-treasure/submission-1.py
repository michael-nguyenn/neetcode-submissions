from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()
        q = deque()

        # Load up the q treasure cells
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    visited.add((row, col))
                    q.append((row, col))
                    
        distance = 0
        while q:
            # Capture the current level
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance

                # add valid neighbors to the q
                for r, c in directions:
                    new_r, new_c = row + r, col + c
                    
                    if (new_r < 0 or new_r >= ROWS or 
                        new_c < 0 or new_c >= COLS or
                        grid[new_r][new_c] == -1 or
                        (new_r, new_c) in visited):
                        continue
                    
                    # Valid Cells
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))
        
            distance += 1



        