class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.backup_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        while self.main_stack:
            self.backup_stack.append(self.main_stack.pop())
        to_return = self.backup_stack.pop()
        while self.backup_stack:
            self.main_stack.append(self.backup_stack.pop())
        return to_return

    def peek(self) -> int:
        while self.main_stack:
            self.backup_stack.append(self.main_stack.pop())
        to_return = self.backup_stack[-1]
        while self.backup_stack:
            self.main_stack.append(self.backup_stack.pop())
        return to_return
        
    def empty(self) -> bool:
        return not bool(self.main_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()