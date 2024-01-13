from SinglyLinkedList import *


class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.__count = 0

    def is_empty(self):
        return super().is_empty()

    def push(self, data=None):
        self.insert_at_start(data)
        self.__count += 1

    def pop(self):
        if not self.is_empty():
            self.delete_at_start()
            self.__count -= 1

    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("Stack Underflow!")

    def size(self):
        return self.__count


s1 = Stack()
s1.push(10)
s1.push(15)
s1.push(20)
s1.push(25)
print(f"Peek: {s1.peek()}")
print(f"Size: {s1.size()}")
s1.pop()
s1.pop()
print(f"\nPeek: {s1.peek()}")
print(f"Size: {s1.size()}")
