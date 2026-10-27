"""
Problem
- Can move down or right at a given time, need to find the cheapest path down

Strategy
- We can use Dijstras to find the shortest path down to the bottom left corner
- 

Example
- Start with 1 in the heap. Pop from the heap and add 1+2, and 1+5
- Heap contains 3,6. Pop the 3, and add its children, 3+0, 3+4
- Heap contains 3,6,7. Pop the 3, add its child, 3+2
- Heap contains 6,7,8. 
"""

import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0,1), (1, 0)]
        h = [] # (cost, row, col)
        visited = set()

        # guaranteed to have at least one element
        heapq.heappush(h, (grid[0][0], 0, 0))

        while h:
            cost, row, col = heapq.heappop(h)
            if (row, col) == (ROWS-1, COLS-1):
                return cost
            visited.add((row, col))

            # Try to go down and right to explore
            for r, c in DIRECTIONS:
                new_r, new_c = row+r, col+c
                if new_r < 0 or new_r == ROWS or new_c < 0 or new_c == COLS or (new_r, new_c) in visited:
                    continue
                
                new_cost = cost + grid[new_r][new_c]
                if (new_r, new_c) == (ROWS-1, COLS-1):
                    return new_cost

                heapq.heappush(h, (new_cost, new_r, new_c))
