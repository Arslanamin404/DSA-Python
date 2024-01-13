class Queue:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def enqueue(self, data=None):
        # insertion
        self.list.append(data)

    def dequeue(self):
        # deletion
        if not self.is_empty():
            self.list.pop(0)
        else:
            raise IndexError("Empty Queue")

    def get_front(self):
        if not self.is_empty():
            return self.list[0]
        else:
            raise IndexError("Empty Queue")

    def get_rear(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Empty Queue")

    def size(self):
        return len(self.list)


if __name__ == "__main__":
    myList = Queue()
    myList.enqueue(10)
    myList.enqueue(20)
    myList.enqueue(30)
    myList.enqueue(40)
    myList.enqueue(50)
    
    print(f"Front: {myList.get_front()}")
    print(f"Rear: {myList.get_rear()}")

    myList.dequeue()
    myList.dequeue()
    myList.enqueue(60)
    print(f"\nFront: {myList.get_front()}")
    print(f"Rear: {myList.get_rear()}")
