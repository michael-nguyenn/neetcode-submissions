# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Since k will be the kth smallest element, we can
        # Do an in-order, and count the times up from there
        i, res = 0, 0

        def helper(root, k):
            nonlocal i, res

            if not root or i == k:
                return

            helper(root.left, k)

            i += 1
            if i == k:
                res = root.val
                return

            helper(root.right, k)

        helper(root, k)
        return res