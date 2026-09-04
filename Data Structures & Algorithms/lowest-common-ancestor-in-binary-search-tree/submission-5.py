# Lowest node T that both p and q are descendants.
# Initially p & q will be both on the left side or right side of cur node
# If p & q are both less than cur -> go left
# if p & q are both greater than cur -> go right
# otherwise this is the lowest common ancestor
    # beyond this point we'd only have at most p or q below us.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # since p & q both exist we're safe to start searching
        # we'll never traverse all the way down, since we're guaranteed to find the ancestor
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


        