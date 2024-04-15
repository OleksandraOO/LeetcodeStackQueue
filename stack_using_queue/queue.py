class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    '''
    class implementing queue
    '''
    def __init__(self) -> None:
        self.first = self.last = None

    def __len__(self):
        x = 0
        node = self.last
        while node is not None:
            node = node.next
            x+=1
        return x

    def isEmpty(self):
        '''
        checking whether the queue is empty
        if the first element is None already 
        then the queue is empty
        '''
        return self.first is None

    def push(self,item):
        '''
        to push the element we need to move 
        pointer of the last element to the 
        new element
        '''
        temp = Node(item)
        if self.last is None:
            self.first = self.last = temp
            return
        self.last.next = temp
        self.last = temp

    def pop(self):
        '''
        moving the pointer of the first one
        '''
        if self.isEmpty():
            return
        temp = self.first
        self.first = temp.next
        if self.first is None:
            self.last = None
        return temp.value