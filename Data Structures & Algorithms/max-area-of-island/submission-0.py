from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        max_area = 0

        def find_area(row, col) -> int:
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            area = 0

            while q:
                row, col = q.popleft()
                area += 1

                for r, c in directions:
                    new_r, new_c = row + r, col + c

                    if (new_r < 0 or new_r == ROWS or 
                        new_c < 0 or new_c == COLS or 
                        grid[new_r][new_c] == 0 or 
                        (new_r, new_c) in visited):
                        continue

                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))

            return area

        # Go thru the grid and search for an unexplored island
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(max_area, find_area(row, col))

        return max_area 