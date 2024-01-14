class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class Deque:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__count = 0

    def is_empty(self):
        return self.__front == None

    def insert_front(self, data=None):
        new_node = Node(None, data, None)
        if self.is_empty():
            self.__front = self.__rear = new_node
        else:
            self.__front.prev = new_node
            new_node.next = self.__front
            self.__front = new_node
        self.__count += 1

    def insert_rear(self, data=None):
        new_node = Node(None, data, None)
        if self.is_empty():
            self.__front = self.__rear = new_node
        else:
            new_node.prev = self.__rear
            self.__rear.next = new_node
            self.__rear = new_node
        self.__count += 1

    def delete_front(self):
        if not self.is_empty():
            if self.__front.next == None:
                self.__front = self.__rear = None
            else:
                self.__front = self.__front.next
            self.__count -= 1
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

    def delete_rear(self):
        if not self.is_empty():
            if self.__front.next == None:
                self.__front = self.__rear = None
            else:
                self.__rear.prev.next = None
            self.__count -= 1
        else:
            raise IndexError("Queue Underflow! No data in the queue.")

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

    def clear(self):
        self.__front = self.__rear = None
        self.__count = 0


if __name__ == "__main__":
    myDeque = Deque()
    myDeque.insert_front(10)
    myDeque.insert_front(20)
    myDeque.insert_front(30)
    myDeque.insert_rear(40)
    myDeque.insert_rear(50)
    myDeque.insert_rear(60)
    print("--------------------------------------------------")
    print(f"Front: {myDeque.get_front()}")
    print(f"Rear: {myDeque.get_rear()}")
    print(f"Size: {myDeque.size()}")

    myDeque.delete_front()
    print("--------------------------------------------------")
    print(f"Front: {myDeque.get_front()}")
    print(f"Rear: {myDeque.get_rear()}")
    print(f"Size: {myDeque.size()}")

    myDeque.clear()
    print("--------------------------------------------------\nAfter using Clear:")
    print(f"Size: {myDeque.size()}")
    print("--------------------------------------------------")
