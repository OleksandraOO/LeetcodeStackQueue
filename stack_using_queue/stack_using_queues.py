from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def transfer_elements(self):
        while not self.q1.isEmpty():
            pop_element = self.q1.pop()
            if self.q1.isEmpty():
                while not self.q2.isEmpty():
                    self.q1.push(self.q2.pop())
                return pop_element
            self.q2.push(pop_element)

    def push(self, x: int) -> None:
        self.q1.push(x)

    def pop(self) -> int:
        return self.transfer_elements()
        # return self.q2.pop()

    def top(self) -> int:
        # self.transfer_elements()
        return self.q1.last.value

    def empty(self) -> bool:
        # self.transfer_elements()
        return self.q1.isEmpty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
# obj.push(3)
# obj.push(4)
param_2 = obj.top()
print(param_2)
param_2 = obj.pop()
print(param_2)
param_2 = obj.empty()
print(param_2)
# print(obj.pop())
# param_4 = obj.empty()
# print(param_4)