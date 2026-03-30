class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None for i in range(capacity)]
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # Check if the array is full
        if self.size == self.getCapacity():
            self.resize()
        
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Index into the element at the end of the array's size
        print(self.getSize())
        print(self.array)
        endValue = self.array[self.getSize() - 1]
        # Set the last element to None
        self.array[self.getSize() - 1] = None
        # Decrement the array's size
        self.size -= 1 
        return endValue

    def resize(self) -> None:
        self.array += [None for i in range(self.getCapacity())]

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return len(self.array)