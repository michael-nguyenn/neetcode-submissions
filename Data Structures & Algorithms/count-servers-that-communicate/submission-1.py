"""
Problem
- m*n grid, 1 = server, 0 = nada
- Two servers can communicate if they're on same row or column
- As long as you can communicate with at least one other server, you're in the tally

Strategy
- We don't need to traverse, so no DFS or BFS?
- (0,0) is in row 0, col 0
- (0, 1) is in row 0, col 1
    - shares row 0 with one another 
- (1, 2) is in row 1, col 2
- (2, 2) is in row 2 col 2
    - shares col 1
- (3,3) is in row 3, col 3

- create m sets for rows, n sets for cols
- we go thru the grid
    - for the 1s we see, 
        - we see if it exists in row or col, if so then we add.
        - then we add it to the corresponding entries
- the very first time we add to a set means that won't get counted for properly
- we need a special way to mark that initial add, maybe a set? O(n*m) introduction?

Example
- (0,0), not in either sets, so we add it to rows[0], cols[0]
- (0,1) in rows[0], so we increment res, add it to cols[1]
    - special_set (0,0), go thru the set and see if row or col match the entry getting added in, if so increment the count and delete the set entry 
- (1,2) added to rows[1], cols[2]
- (2,2) is in cols[2], increment res, add it to rows[2]
"""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = {}, {}

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows[row] = 1 + rows.get(row, 0)
                    cols[col] = 1 + cols.get(col, 0)
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if rows[row] > 1 or cols[col] > 1:
                        res += 1
                
        return res
                    
        