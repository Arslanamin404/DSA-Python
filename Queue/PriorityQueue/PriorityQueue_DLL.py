class Node:
    def __init__(self, prev=None, data=None, priority=None, next=None):
        self.prev = prev
        self.data = data
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self, start=None):
        self.__start = start
        self.__count = 0

    def is_empty(self):
        return self.__start == None

    def push(self, data, priority):
        new_node = Node(None, data, priority, None)
        if self.is_empty():
            self.__start = new_node
        elif priority < self.__start.priority:
            new_node.next = self.__start
            self.__start.prev = new_node
            self.__start = new_node
        else:
            current = self.__start
            while current.next is not None and current.priority <= new_node.priority:
                current = current.next
            if current.prev is not None:
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node
            else:
                new_node.next = self.__start
                self.__start.prev = new_node
                self.__start = new_node
        self.__count += 1

    def pop(self):
        if not self.is_empty():
            pop_data = self.__start.data
            pop_priority = self.__start.priority
            self.__start = self.__start.next
            self.__count -= 1
            return pop_data, pop_priority
        else:
            raise IndexError("Queue Underflow! Queue is empty.")

    def size(self):
        return self.__count


if __name__ == "__main__":
    queue = PriorityQueue()
    assert queue.is_empty() == True
    queue.push(50, 5)
    queue.push(20, 2)
    queue.push(10, 1)
    queue.push(40, 4)
    queue.push(30, 3)
    print("------------------------------")
    print(f"Size: {queue.size()}")
    print("------------------------------")
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())

    print(f"Size: {queue.size()}")
    print("------------------------------")
