"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clones = {}
        q = collections.deque()
        
        # Clone the original
        clone = Node(node.val, [])
        clones[node] = clone
        q.append(node)

        while q:
            cur_node = q.popleft()
            
            for neighbor in cur_node.neighbors:
                if neighbor not in clones:
                    clone = Node(neighbor.val, [])
                    q.append(neighbor)
                    clones[neighbor] = clone
                
                clones[cur_node].neighbors.append(clones[neighbor])
        
        return clones[node]
                
        