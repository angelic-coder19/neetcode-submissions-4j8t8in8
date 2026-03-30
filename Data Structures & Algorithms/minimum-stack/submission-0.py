class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        min = self.stack[0]
        for n in self.stack:
            if n < min:
                min = n
        return min
        
