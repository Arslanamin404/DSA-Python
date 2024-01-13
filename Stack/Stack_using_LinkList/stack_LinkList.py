class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data=None):
        new_node = Node(data, self.start)
        self.start = new_node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.data
            self.start = self.start.next
            self.count -= 1
            return data
        else:
            raise IndexError("EMPTY Stack!")

    def peek(self):
        if self.is_empty():
            raise IndexError("EMPTY Stack!")
        else:
            return self.start.data

    def size(self):
        return self.count
