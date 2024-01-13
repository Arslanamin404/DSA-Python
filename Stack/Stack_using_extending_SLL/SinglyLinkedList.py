# ------------ Singly Linked List ------------ #
# * check notebook for detailed logic and diagram for better understanding
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data=None):
        new_node = Node(data, self.start)
        self.start = new_node

    def delete_at_start(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        else:
            pop_data = self.start.data
            self.start = self.start.next
