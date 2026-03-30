class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        else:
            val = val
        self.minStack.append(val)
        self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.minStack[self.size - 1]
        
