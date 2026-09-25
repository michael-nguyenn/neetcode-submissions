class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])

        def spread(r,c): 
            nonlocal to_rot

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            to_rot.add((r,c))
            for r_,c_ in directions: 
                if 0 <= r+r_ < rows and 0 <= c+c_ < cols:
                    to_rot.add((r+r_,c+c_))

        time = 0
        while True: 
            to_rot = set()
            fresh = set()
            for r in range(rows):
                for c in range(cols): 
                    if grid[r][c] == 2: 
                        spread(r,c)
                    if grid[r][c] == 1:
                        fresh.add((r,c))

            # No more fresh fruits 
            if not fresh:
                break

            # Spread the rot
            for r,c in to_rot:
                if grid[r][c] == 1: 
                    grid[r][c] = 2

            # First case edge case as fresh_prev does not exist 
            if time == 0: 
                time += 1
                fresh_prev = fresh
                continue

            # If fresh fruit stayed the same, then no more spread
            if fresh_prev == fresh: 
                return -1 
            fresh_prev = fresh

            time += 1
        
        return time