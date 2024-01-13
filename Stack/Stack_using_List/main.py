class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, data=None):
        self.data.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        else:
            self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        else:
            return self.data[-1]

    def size(self):
        return len(self.data)


if __name__ == "__main__":
    MyStack = Stack()
    MyStack.push(10)
    MyStack.push(20)
    MyStack.push(30)
    MyStack.pop()
    print(MyStack.size())
    print(MyStack.peek())
