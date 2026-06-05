"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def clone(node):

            # If this exists we should return the cloned node
            if node in old_to_new:
                return old_to_new[node]

            # Otherwise this node isn't in the mapping
            # We create the node and then recursively link to
            # neighbors

            new_node = Node(node.val)
            old_to_new[node] = new_node

            for neighbor in node.neighbors:
                cloned_neighbor = clone(neighbor)
                new_node.neighbors.append(cloned_neighbor)
            
            return new_node

        return clone(node) if node else None
