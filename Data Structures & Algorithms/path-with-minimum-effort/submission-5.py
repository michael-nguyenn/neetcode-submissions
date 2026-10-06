"""
Use a min heap to create the shortest path like dijkstras
in dij, the heap actually replaces the q

so then we want to add (0,0,0) (effort,r,c)
then we pop from the heap, we check if this cell is the last one or not

if it's not then we want to go thru all the children
    if they're not in visited
        then we can add the child

"""
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:  
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        h= []
        heapq.heappush(h, (0,0,0)) # (effort,r,c)
        dist = [[float('inf')] * COLS for _ in range(ROWS)]
        dist[0][0] = 0
    

        while h:
            effort, row, col = heapq.heappop(h)

            if (row, col) == (ROWS-1, COLS-1):
                return effort

            if effort > dist[row][col]:
                continue

            for r,c in directions:
                new_r, new_c = row+r, col+c
                if new_r < 0 or new_r == ROWS or new_c < 0 or new_c == COLS:
                    continue

                new_effort = max(abs(heights[row][col] - heights[new_r][new_c]), effort)

                if new_effort < dist[new_r][new_c]:
                    heapq.heappush(h, (new_effort, new_r, new_c))
                    dist[new_r][new_c] = new_effort



        