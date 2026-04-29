from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Array to store the output
        res = []

        # Early Exit
        if not root:
            return res

        # Otherwise we'll use a queue to process each node
        q = deque()

        # We'll add the first node to the queue to start things off
        q.append(root)

        while q:
            temp = []

            for i in range(len(q)):
                node = q.popleft()  # Remove the Node
                temp.append(node.val) # Form the sub array

                # Then we'll add its children (if any) to the queue
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            # Once we're out of the inner loop we can add to our resulting array
            res.append(temp)
        
        return res