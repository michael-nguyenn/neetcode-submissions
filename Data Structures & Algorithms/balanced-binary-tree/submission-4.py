# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, 0)
            
            left_bal, left_height = dfs(root.left)
            right_bal, right_height = dfs(root.right)
            balanced = left_bal and right_bal and abs(left_height - right_height) <= 1

            return (balanced, 1 + max(left_height, right_height))

        return dfs(root)[0]

        