class Deque:
    class _Node:
        def __init__(self, value: int):
            self.val = value
            self.next = None

    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:

        new_node = Deque._Node(value)

        # In the case of an empty Queue
        if self.isEmpty():
            self.head = new_node
        # This is the case where there's only one item
        elif self.head == self.tail:
            self.head.next = new_node
        # Otherwise we have at least two items
        else:
            self.tail.next = new_node

        self.tail = new_node

    def appendleft(self, value: int) -> None:

        new_node = Deque._Node(value)

        # In the case of an empty Queue
        if self.isEmpty():
            self.head = self.tail = new_node
        # Otherwise there is at least one node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        value = self.tail.val
        # Here we'll see if there is only one node
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            trav = self.head
            while trav.next.next != None:
                trav = trav.next
            
            trav.next = None
            self.tail = trav

        return value
            
    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        value = self.head.val

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return value

        
