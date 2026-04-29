class LinkedList:
    # Inner Class For the structure of a Node
    class _Node:
        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        # Since i is guaranteed to be positive
        # We'll create a dummy node
        self.head = self.tail = LinkedList._Node(-1)

        # Internal Tracking 
        self.items = 0


    def get(self, index: int) -> int:
        if self.items == 0 or index >= self.items:
            return -1
        
        trav = self.head

        for i in range(index + 1):
            trav = trav.next

        return trav.value


    def insertHead(self, val: int) -> None:
        # Create a new node
        new_node = LinkedList._Node(val)

        # In the case of an empty linked list
        # We'll keep head pointing at the dummy node, and move tail
        if self.items == 0:
            self.head.next = new_node
            self.tail = new_node
        # If there is at least one item
        else:
            # First point the new node to the previous first node
            new_node.next = self.head.next

            # Then we'll change our head pointer
            self.head.next = new_node
        
        # Increment items
        self.items += 1
            
    def insertTail(self, val: int) -> None:
        new_node = LinkedList._Node(val)

        # In the case of an empty linked list
        # We'll keep head pointing at the dummy node, and move tail
        if self.items == 0:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.items += 1

    def remove(self, index: int) -> bool:
        # Edge Cases
        if self.items == 0 or index >= self.items:
            return False

        trav = self.head

        for i in range(index):
            trav = trav.next

        # If we're trying to remove the last node, we should move tail
        if trav.next == self.tail:
            self.tail = trav
            trav.next = None
        # Otherwise we're removing some node in the middle
        else:
            trav.next = trav.next.next

        self.items -= 1
        return True

    def getValues(self) -> List[int]:
        a = []

        # We'll move trav from the dummy head first
        trav = self.head.next

        while (trav != None):
            a.append(trav.value)
            trav = trav.next

        return a
        
