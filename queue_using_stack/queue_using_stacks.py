from queue_using_stack.stack import Stack
class MyQueue:
    """
    class realising queue by using 2 stacks
    """
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def __repr__(self) -> str:
        return f'first: {self.st1}     second: {self.st2}'

    def transfer_elements(self):
        """
        transfering elements to change 
        the direction of the stack
        """
        if self.st2.isEmpty():
            while not self.st1.isEmpty():
                self.st2.push(self.st1.pop())

    def push(self, x: int) -> None:
        """
        regular push to the base stack
        """
        self.st1.push(x)

    def pop(self) -> int:
        """
        transfering elements so the direction 
        would be correct and pop of the last 
        element
        """
        self.transfer_elements()
        return self.st2.pop()

    def peek(self) -> int:
        """
        returning peek element
        """
        self.transfer_elements()
        return self.st2.peek()

    def empty(self) -> bool:
        """
        check by using isEmpty of Stack class
        """
        return self.st1.isEmpty() and self.st2.isEmpty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(1)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
