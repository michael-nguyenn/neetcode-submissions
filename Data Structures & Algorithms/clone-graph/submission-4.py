from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}
        q = deque()
        new_node = Node(node.val)
        old_to_new[node] = new_node
        q.append(node)

        while q:
            cur_node = q.popleft()

            for neighbor in cur_node.neighbors:
                if neighbor not in old_to_new:
                    new_node = Node(neighbor.val)
                    old_to_new[neighbor] = new_node
                    q.append(neighbor)

                old_to_new[cur_node].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]

