class Node:
    def __init__(self, data=None, priority=None, next=None):
        self.data = data
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data=None, priority=None):
        new_node = Node(data, priority, None)
        if self.is_empty():
            self.start = new_node
        elif priority < self.start.priority:
            new_node.next = self.start
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.count += 1

    def pop(self):
        if not self.is_empty():
            pop_data = self.start.data
            pop_priority = self.start.priority
            self.start = self.start.next
            self.count -= 1
            return f"{pop_data} {pop_priority}"
        else:
            raise IndexError("Queue Underflow!")

    def size(self):
        return self.count


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

    popped_elements = []  # Store popped elements
    while not queue.is_empty():
        print(queue.pop())
    print(f"Size: {queue.size()}")
    print("------------------------------")
