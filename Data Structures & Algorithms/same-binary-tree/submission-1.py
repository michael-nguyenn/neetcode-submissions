# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base Cases
        # Is symmetrical
        if not p and not q:
            return True
        
        # Is not symmetrical
        if not p or not q:
            return False

        # Mismatched Values
        if p.val != q.val:
            return False

        # This means the values match and we can explore the other trees
        # Recursion
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)