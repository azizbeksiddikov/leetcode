# Link: https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefix.append(min(val, self.prefix[-1] if self.prefix else val))

    def pop(self) -> None:
        self.prefix.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1]

# minStack = MinStack()
# minStack.push(1)
# minStack.push(2)
# minStack.push(0)
# print(minStack.getMin()) # return 0
# print(minStack.pop())    # return 0
# print(minStack.top())    # return 2
# print(minStack.getMin()) # return 1