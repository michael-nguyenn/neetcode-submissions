class Node:
    def __init__(self, val = None, key = None):
        self.val = val
        self.key = key
        self.n = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # map key -> node
        self.capacity = capacity
        self.size = 0
        self.head = Node(-1, -1) # Least recently used
        self.tail = Node(-1, -1) # Most recently used
        self.head.n, self.tail.prev = self.tail, self.head
    
    def add(self, cur: Node):
        self.tail.prev.n = cur
        cur.n = self.tail
        cur.prev = self.tail.prev
        self.tail.prev = cur
    
    def remove(self, cur: Node):
        cur.prev.n = cur.n
        cur.n.prev = cur.prev
        cur.n = None # to be explicit
        cur.prev = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        cur = self.cache[key]
        self.remove(cur)
        self.add(cur)
        return cur.val


    def put(self, key: int, value: int) -> None:
        # key doesn't exist we have to create the node
        if key not in self.cache:
            # create the entry and add it to our hash map
            cur = Node(value, key)
            self.cache[key] = cur

            # add it to our q
            self.add(cur)
            self.size += 1

            # if our size is over capacity we evict from head
            if self.size > self.capacity:
                to_remove = self.head.n
                self.remove(to_remove)
                del self.cache[to_remove.key]
                self.size -= 1
                
        # otherwise we update the value and update ordering
        else:
            cur = self.cache[key]
            self.remove(cur)
            self.add(cur)
            cur.val = value
        
        
