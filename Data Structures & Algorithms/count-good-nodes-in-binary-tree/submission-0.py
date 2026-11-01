# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Problem
- a node is considered good if path from root to node x contain no values greater than x
- if we the root of a subtree then this node is valid if
    - we are > than the root / > than the largest value seen so far

Strategy
- Can a preorder traversal
- If the current node is > than largestSeen, then this becomes largestSeen 
- Otherwise you pass in the largestSeen from before

Cases
- Falling off the tree returns 0
- If we're larger then we contribute 1
- If we're not we contribute 0
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, largest_seen):
            if not root:
                return 0
            
            if root.val >= largest_seen:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, largest_seen) + dfs(root.right, largest_seen)
        
        return dfs(root, -float('inf'))

        
        
        