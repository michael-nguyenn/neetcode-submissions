class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = { (m-1, n-1) : 1 }
   
        
        def paths(row: int, col: int) -> int:
            # Base Case = When we fly off the grid
            # We can only go off the right side or bottom
            if (row, col) in memo:
                return memo[(row,col)]

            if row == m or col == n:
                return 0
            
            # If we're not at a base case then we can explore
            # our two options in hand going down or right
            num_paths = 0

            num_paths += paths(row + 1, col)
            num_paths += paths(row, col + 1)

            memo[(row, col)] = num_paths
            return num_paths
        
        return paths(0, 0)
            
        