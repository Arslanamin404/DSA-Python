from SLL import *


class Stack:
    def __init__(self):
        self.myList = SLL()
        self.__count = 0

    def is_empty(self):
        return self.myList.is_empty()

    def push(self, data=None):
        self.myList.push(data)
        self.__count += 1

    def pop(self):
        self.myList.pop()
        self.__count -= 1

    def peek(self):
        return self.myList.start.data

    def size(self):
        return self.__count


if __name__ == "__main__":
    myStack = Stack()
    myStack.push(10)
    myStack.push(15)
    myStack.push(20)
    myStack.push(25)
    myStack.push(30)
    
    print(f"Size: {myStack.size()}")
    print(f"peak: {myStack.peek()}")

    myStack.pop()
    
    print(f"\nSize: {myStack.size()}")
    print(f"peak: {myStack.peek()}")

    myStack.pop()
    
    print(f"\nSize: {myStack.size()}")
    print(f"peak: {myStack.peek()}")
