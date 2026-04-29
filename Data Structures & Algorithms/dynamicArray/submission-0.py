class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:

        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]
 

    def resize(self) -> None:
        # New capacity
        new_array = [0] * self.capacity * 2
        # Copy over the current array into the new array
        for i in range(self.size):
            new_array[i] = self.array[i]

        # Set capacity, and array accordingly
        self.capacity *= 2
        self.array = new_array


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
