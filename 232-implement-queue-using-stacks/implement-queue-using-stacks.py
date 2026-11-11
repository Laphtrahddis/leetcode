class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []     

    def push(self, x: int) -> None:
        self.in_stack.append(x)        

    def pop(self) -> int:
        if len(self.out_stack):
            popValue = self.out_stack[-1]
            self.out_stack.pop()
            return popValue
        else:
            while self.in_stack:
                lastVal = self.in_stack.pop()
                self.out_stack.append(lastVal)
            popValue = self.out_stack[-1]
            self.out_stack.pop()
            return popValue

    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        else:
            while self.in_stack:
                lastVal = self.in_stack.pop()
                self.out_stack.append(lastVal)
            return self.out_stack[-1]
        

    def empty(self) -> bool:
        if not self.in_stack and not self.out_stack:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
