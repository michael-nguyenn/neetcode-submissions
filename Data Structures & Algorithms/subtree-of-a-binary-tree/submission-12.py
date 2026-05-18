# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Base Case
        if not root:
            return False

        # Recursive Cases
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False

        # Recursion
        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)