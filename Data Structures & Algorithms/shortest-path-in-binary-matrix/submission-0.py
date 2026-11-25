"""
Problem
- given a nxn matrix, and return the shortest clear path (all 0s) from the top left (0, 0) to bottom right (n-1, n-1)
- you can move in all 8 directions, up (1, 0), down (-1, 0), right (0, 1), left (0 , -1), up/left (1, -1), up/right (1, 1), down/left (-1, -1), down/right (-1, 1)

Example
   c0 c1 c2
r0 [0, 1, 0]
r1 [1, 0, 0]
r2 [1, 1, 0]

Cases
- if no path exists return -1
- length 1 grid will either return 1 or -1
- if the first cell is 1 then return -1

Strategy
- seed the q with (0, 0) (row, col)
- while the q still has elements in it
    - start our path_len = 1  (the # of round we're on)
    - capture the level of the q
        - pop from the q
        - mark visited 
            - if the popped element is (n-1, n-1) return the path_len
            - for each of the directions, append to the q if legal
- if we make it out here we should return -1

Trace
visited = (0, 0), (1, 1)
level 1: q = [(0, 0)]
- pop (0, 0) -> mark visited -> enque (1, 1)

level 2: q = [(1, 1)]
- pop (1, 1) -> mark visited -> enque (1, 2), (2, 2)

level 3: q = [(1, 2), (2, 2)]
- pop (1, 2) -> mark visited -> enque (0, 2), (2, 2)
- pop (2, 2) -> IS BOTTOM RIGHT, RETURN 3

Complexity
- Time: O(m*n), worst case we traverse thru the entire grid
- Space: O(m*n), q can hold up to grid elements
"""
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visited = set()
        q = deque()

        if grid[0][0] == 1:
            return -1

        q.append((0, 0))
        
        path_len = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                if (row, col) == (ROWS-1, COLS-1):
                    return path_len
                
                visited.add((row, col))

                for r, c in directions:
                    nr, nc = row+r, col+c
                    if (nr < 0 or nr == ROWS or 
                    nc < 0 or nc == COLS or 
                    (nr, nc) in visited or 
                    grid[nr][nc] == 1):
                        continue

                    q.append((nr, nc))
                
                
            path_len += 1

        return -1

        