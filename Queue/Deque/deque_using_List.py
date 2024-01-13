class Deque:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def insert_front(self, data=None):
        self.list.insert(0, data)

    def insert_rear(self, data=None):
        self.list.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.list.pop(0)
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

    def delete_rear(self):
        if not self.is_empty():
            self.list.pop(-1)
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

    def size(self):
        return len(self.list)


if __name__ == "__main__":
    myDeque = Deque()
    myDeque.insert_front(10)
    myDeque.insert_front(20)
    myDeque.insert_front(30)
    myDeque.insert_rear(40)
    myDeque.insert_rear(50)
    myDeque.insert_rear(60)
    
    print("----------------------------------------")
    print(f"Font: {myDeque.get_front()}")
    print(f"Rear: {myDeque.get_rear()}")
    print("----------------------------------------")
    
    myDeque.delete_front()
    myDeque.delete_rear()
    print(f"Font: {myDeque.get_front()}")
    print(f"Rear: {myDeque.get_rear()}")
    print("----------------------------------------")
    