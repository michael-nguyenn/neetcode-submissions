# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q, res = deque(), []

        if root:
            q.append(root)
        
        while q:
            level_nodes = []
            # this lets us stop at the original length of the queue
            for _ in range(len(q)):
                cur_node = q.popleft()

                # add children to the list
                if cur_node.left:
                    q.append(cur_node.left)

                if cur_node.right:
                    q.append(cur_node.right)

                # add current to the level order list
                level_nodes.append(cur_node.val)
            
            res.append(level_nodes)


        return res

        