class MinStack:

    # Inner Class
    class _Node:
        def __init__(self, value, min_val):
            self.value = value
            self.min_val = min_val

    def __init__(self):
        self.stack = []  

    def push(self, val: int) -> None:

        # If we're pushing onto the stack for the firs time
        if not self.stack:
            node = MinStack._Node(val, val)
            self.stack.append(node)
        # Otherwise we'll compare the min value of the prev node
        else:
            node = MinStack._Node(val, min(self.stack[-1].min_val, val))
            self.stack.append(node)


    def pop(self) -> None:
        node = self.stack.pop()
        return node.value
        

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.stack[-1].min_val
        
