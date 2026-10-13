"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

"""
Problem
- Node = True if grid[i][j] == 1 else False
- If the node has four children then isLeaf == False

Strategy
- Check if the current grid has all the same values or not
    - Pass in row_start, row_end, col_start, col_end
    - Go thru each and cell, and check if they're the same value
    - Return boolean

- Dividing the grid into four
    - Pass in row_start, row_end, col_start, col_end
    # - First quad = 
    #     - 0 - r_start + r_end // 2 
    #     - 0 - c_start + c_end // 2
    # - Bottom left quad =
    #     - r_start + r_end // 2 + 1 -> end
    #     - 0 - c_start + c_end // 2
    # - Top right =  
    #     - 0 - r_start + r_end // 2 
    #     - c_start + c_end // 2 + 1 -> end
    # - Bottom Right =
    #     - r_start + r_end // 2 + 1 -> end
    #     - c_start + c_end // 2 + 1 -> end


- If not all same value, isLeaf is set to False, value is set anything
- Create a Node(val=anything, isLeaf=False) 
- Set the four children 

- If all same values then set isLeaf to True
- Set val to the value of the grid, set four children to None & stop


"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def check(r_start, r_end, c_start, c_end) -> bool:
            value = grid[r_start][c_start]
            for r in range(r_start, r_end):
                for c in range(c_start, c_end):
                    if grid[r][c] != value:
                        return False
            return True

        def divide(r_start, r_end, c_start, c_end):
            r_half = (r_start + r_end ) // 2
            c_half = (c_start + c_end) // 2

            top_left = (r_start, r_half, c_start, c_half)
            top_right = (r_start, r_half, c_half, c_end)
            bottom_left = (r_half, r_end, c_start, c_half) 
            bottom_right = (r_half, r_end, c_half, c_end)

            return (top_left, top_right, bottom_left, bottom_right)

        def dfs(r_start, r_end, c_start, c_end):
            # - If not all same value, isLeaf is set to False, value is set anything
            # - Create a Node(val=anything, isLeaf=False) 
            # - Set the four children 
            # - If all same values then set isLeaf to True
            # - Set val to the value of the grid, set four children to None & stop

            if check(r_start, r_end, c_start, c_end):
                return Node(grid[r_start][c_start], True, None, None, None, None)
            
            # Here means our check failed 
            cur = Node(1, 0, None, None, None, None)
            top_l, top_r, bot_l, bot_r = divide(r_start, r_end, c_start, c_end)

            cur.topLeft = dfs(top_l[0], top_l[1], top_l[2], top_l[3])
            cur.topRight = dfs(top_r[0], top_r[1], top_r[2], top_r[3])
            cur.bottomLeft = dfs(bot_l[0], bot_l[1], bot_l[2], bot_l[3])
            cur.bottomRight = dfs(bot_r[0], bot_r[1], bot_r[2], bot_r[3])

            return cur

        return dfs(0, len(grid), 0, len(grid[0]))
        