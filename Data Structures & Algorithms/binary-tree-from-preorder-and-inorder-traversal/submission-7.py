# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        preorder_idx = 0
        def build(left, right):
            nonlocal preorder_idx

            if left > right:
                return None

            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1

            mid = inorder_map[root.val]
            root.left = build(left, mid-1)
            root.right = build(mid+1, right)
            return root

        return build(0, len(preorder)-1)
        