"""
Problem
- Start somewhere in the grid
- Can move in four standard directions
- Have maxMoves moves
- Path ends right when you leave the grid

Strategy
- Use BFS where each round represents one move of max moves
- Create a grid with m rows and n columns
- Use a q and seed it with (startRow,startRow)
- while q and maxMoves > 0:
    - decrement maxMoves/ or increment moves
    - add to a visited set
    - for the four directions
        - if we're out of bounds, then we increment res
        - if it's in visited continue
        - otherwise we should add to the queue

Cases
- Stop when no more moves or no more items in the queue, that means we've made it off the board

"""
from collections import defaultdict
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        ROWS, COLS = m, n
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        frontier = {(startRow, startColumn):1} # paths we're on after k moves
        res = 0

        for _ in range(maxMove):
            next_frontier = defaultdict(int)

            for (row, col), count in frontier.items():
                for r,c in DIRECTIONS:
                    new_r, new_c = row+r, col+c

                    if new_r < 0 or new_r == ROWS or new_c < 0 or new_c == COLS:
                        res = (res+count) % MOD
                    else:
                        next_frontier[(new_r, new_c)] += count
            
            frontier = next_frontier
        
        return res

