class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__count = 0

    def is_empty(self):
        return self.__front == None

    def enqueue(self, data=None):
        new_node = Node(data)
        if self.is_empty():
            self.__rear = self.__front = new_node
        else:
            self.__rear.next = new_node
            self.__rear = new_node
        self.__count += 1

    def dequeue(self):
        if not self.is_empty():
            if self.__front.next == None:
                self.__rear = self.__front = None
            else:
                self.__front = self.__front.next
            self.__count -= 1
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.__front.data
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

    def get_rear(self):
        if not self.is_empty():
            return self.__rear.data
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

    def size(self):
        return self.__count


if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(10)
    myQueue.enqueue(20)
    myQueue.enqueue(30)
    myQueue.enqueue(40)
    myQueue.enqueue(50)
    print(f"Front: {myQueue.get_front()} ")
    print(f"Rear: {myQueue.get_rear()} ")
    myQueue.dequeue()
    print(f"\nFront: {myQueue.get_front()} ")
    print(f"Rear: {myQueue.get_rear()} ")
