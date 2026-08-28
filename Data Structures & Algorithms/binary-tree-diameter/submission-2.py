# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node) -> int:
            nonlocal res
            
            if not node:
                return 0

            # at a given node the max it can contribute is either both its children
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            res = max(res, left_height + right_height)
            return 1 + max(left_height, right_height)
            
        dfs(root)
        return res