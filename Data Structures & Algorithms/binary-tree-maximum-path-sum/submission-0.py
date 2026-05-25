# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            # base case
            if not root:
                return 0

            # calculate left and right maxes
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # normalize the two incase they contribute negative
            # in this case it's better to contribute 0
            left_max = max(left_max , 0)
            right_max = max(right_max , 0)

            # see how much we would contribute if we could
            # use both sides (split)
            res[0] = max(res[0], (left_max + right_max + root.val))

            # return the highest value path up
            return root.val + max(left_max, right_max)
        
        dfs(root)
        return res[0]
            