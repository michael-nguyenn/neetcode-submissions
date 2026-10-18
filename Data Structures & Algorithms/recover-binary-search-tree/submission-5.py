# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
In inorder traversal we visit each node one at a time
- So we can have two vars holding pointers to the nodes to swap
- and hold onto a prev (start off as -inf
- once we visit the node, we can then compare it to prev
    - if prev is greater than current then that's our inversion
"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second = None, None
        prev = None

        def inorder(cur):
            nonlocal first, second, prev

            if not cur:
                return
            
            inorder(cur.left)

            if prev and prev.val > cur.val:
                if not first:
                    first = prev
                second = cur 
            
            prev = cur
            
            inorder(cur.right)
        
        inorder(root)
        first.val, second.val = second.val, first.val
        