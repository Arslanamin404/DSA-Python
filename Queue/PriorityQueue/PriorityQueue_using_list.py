class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data=None, priority=None):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
        else:
            raise IndexError("Queue Underflow! List is Empty.")

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = PriorityQueue()
    print(f"Is Empty: {queue.is_empty()}")
    queue.push("Logic Building", 1)
    queue.push("PUBG", 5)
    queue.push("Coding", 3)
    queue.push("Problem Solving", 2)
    queue.push("Food", 0)
    
    while not queue.is_empty():
        print(queue.pop())
