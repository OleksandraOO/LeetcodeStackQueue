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
        if self.isEmpty():
            raise IndexError("empty stack")
        remove = self.top
        self.top = self.top.next
        self.size -= 1
        return remove.value
