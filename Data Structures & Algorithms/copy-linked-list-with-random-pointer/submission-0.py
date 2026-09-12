"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clones = {} # node -> cloned_node

        def dfs(node) -> Optional[Node]:
            if not node:
                return None
            if node in clones:
                return clones[node]
        
            # Clone the node
            cur = Node(node.val)
            clones[node] = cur
            clones[node].next = dfs(node.next)
            clones[node].random = dfs(node.random)

            return clones[node]

        return dfs(head)

        