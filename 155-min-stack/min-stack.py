class MinStack:

    def __init__(self):
        self.stack = []
        self.second = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.second or value <= self.second[-1]:
            self.second.append(value)

    def pop(self) -> None:
        a =self.stack.pop()
        if a == self.second[-1]:
            self.second.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.second[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()