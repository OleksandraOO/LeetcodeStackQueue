from collections import defaultdict, deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        cur = self.top
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty stack")
        return self.top.value

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        # if self.isEmpty():
        #     raise IndexError("empty stack")
        remove = self.top
        self.top = self.top.next
        self.size -= 1
        return remove.value

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.values = defaultdict(Stack)
        self.max_frequency = 0
    
    def __repr__(self) -> str:
        return f'{self.values[1]}, {self.values[2]}, {self.values[3]}   max : {self.max_frequency}'

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.values[self.freq[val]].push(val)
        self.max_frequency = max(self.freq[val], self.max_frequency)

    def pop(self) -> int:
        try:
            # print('-----------')
            # print(self.values[self.max_frequency])
            val_popped = self.values[self.max_frequency].pop()
            # print(self.values[self.max_frequency])
            # print('-----------')
            self.freq[val_popped] -= 1
            if self.values[self.max_frequency].size == 0:
                self.max_frequency -=1
            return val_popped
        except:
            pass


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
val = 3
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
param_2 = obj.pop()
print(param_2)
param_2 = obj.pop()
print(param_2)
param_2 = obj.pop()
print(param_2)