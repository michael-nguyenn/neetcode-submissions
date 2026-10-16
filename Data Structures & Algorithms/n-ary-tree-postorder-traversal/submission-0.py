"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

"""
- Post order is, visit left, visit right, visit root.
- For a N-ary array we have more than a left
- So we have to call postorder for each of the children, starting from the left

Cases
- Base case is when the root is None -> Return
- After visiting all the children, then we can append to res

Strategy
- Children is an array of Nodes
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return 

            for child in root.children:
                dfs(child)
            
            res.append(root.val)
        
        dfs(root)
        return res

        