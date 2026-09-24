# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            cur_len = len(q)
            for i in range(cur_len):
                cur_node = q.popleft()

                if i == cur_len - 1:
                    res.append(cur_node.val)
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        
        return res



        