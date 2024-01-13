class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, data=None):
        return self.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("EMPTY Stack!")
        else:
            return super().pop()

    def peek(self):
        if self.is_empty():
            return "EMPTY Stack!"
        else:
            return self[-1]

    def size(self):
        return len(self)

    def insert(self, index=None, data=None):
        raise AttributeError("No attribute Insert is in Stack!")

    def remove(self, data=None):
        raise AttributeError("No attribute Remove is in Stack!")
