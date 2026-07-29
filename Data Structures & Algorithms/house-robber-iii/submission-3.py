# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {} # root -> their max rob value

        def dfs(root):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]
            
            max_rob = 0
            rob_this_house = root.val
            skip_this_house = 0

            # This skips the immediate child
            if root.left:
                rob_this_house += dfs(root.left.left) + dfs(root.left.right)

            if root.right:
                rob_this_house += dfs(root.right.left) + dfs(root.right.right)
            
            # max_rob currently holds the maximum if we skipped a child
            # we have to see what happens if we skip the node itself
            skip_this_house += dfs(root.left) + dfs(root.right)

            max_rob = max(rob_this_house, skip_this_house)
            memo[root] = max_rob
            return max_rob

        return dfs(root)