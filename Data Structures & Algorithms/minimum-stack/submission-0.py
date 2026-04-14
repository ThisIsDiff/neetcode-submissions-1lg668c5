class MinStack:
    def __init__(self):
        self.mstack = []
        self.minval = []

    def push(self, val: int) -> None:
        self.mstack.append(val)
        if (self.minval and self.mstack[self.minval[-1]] <= val):
            return
        self.minval.append(len(self.mstack) - 1)

    def pop(self) -> None:
        if (self.mstack):
            self.mstack.pop()

        if (self.minval[-1] >= len(self.mstack)):
            self.minval.pop()
            

    def top(self) -> int:
        return self.mstack[-1]

    def getMin(self) -> int:
        if self.mstack:
            return self.mstack[self.minval[-1]]
            
