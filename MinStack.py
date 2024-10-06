class MinStack:

    def __init__(self):

        self.stack = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if(not self.mins or self.mins[-1]>=val):
            self.mins.append(val)
        

    def pop(self) -> None:

        a = self.stack.pop()
        if(a==self.mins[-1]):
            self.mins.pop()
        

    def top(self) -> int:

        t = self.stack.pop()
        self.stack.append(t)
        return t
        

    def getMin(self) -> int:
        return (self.mins[-1] if self.mins[-1]!=float("inf") else float("inf"))
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()