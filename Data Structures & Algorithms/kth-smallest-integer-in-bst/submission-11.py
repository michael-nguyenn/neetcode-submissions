# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        res = None

        def inorder(root):
            nonlocal res
            
            if not root or res is not None:
                return

            inorder(root.left)

            nonlocal counter
            counter -= 1
            if counter == 0:
                res = root.val


            inorder(root.right)

        inorder(root)
        return res