# multi source BFS?
# look for all the cells containing 2 and seed the q
# every round, rot the fruit around it
# cells that are empty or rotten already or in visited -> no need to add to q
# at the end go thru the grid once more to see if there are any fresh fruit left

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q, visited = deque(), set()
        fresh = 0 # to keep track of how many we need to rot
        rounds = 0

        # Load up the q and keep track of how many fresh we have to rot
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                    fresh += 1
                    
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                print(f"{row}, {col}")
                grid[row][col] = 2
                fresh -= 1

                for r, c in directions:
                    new_r = row + r
                    new_c = col + c

                    if (new_r < 0 or new_r == ROWS or 
                        new_c < 0 or new_c == COLS or
                        (new_r, new_c) in visited or 
                        grid[new_r][new_c] != 1):
                        continue
                    
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))

            if q:
                rounds += 1

        return -1 if fresh > 0 else rounds
        

        
        

        
        


        