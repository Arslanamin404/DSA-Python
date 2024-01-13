class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data=None):
        new_node = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = new_node
        self.start = new_node

    def insert_at_last(self, data=None):
        if self.is_empty():
            new_node = Node(None, data)
            self.start = new_node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            new_node = Node(temp, data)
            temp.next = new_node

    def search(self, data=None):
        if self.is_empty():
            print("List is Empty")
        else:
            temp = self.start
            while temp != None:
                if temp.data == data:
                    return temp
                temp = temp.next
            return None

    def insert_after(self, insert_after_data=None, data=None):
        temp = self.search(insert_after_data)
        if temp != None and temp.next != None:
            new_node = Node(temp, data, temp.next)
            temp.next = new_node
        elif temp != None:
            # if we want to add after last node
            new_node = Node(temp, data)
            temp.next = new_node
        else:
            print(f"The node with data {insert_after_data} was not found.\n")

    def delete_start(self):
        if self.is_empty():
            print("List is Empty!")
        else:
            if self.start.next != None:
                self.start.next.prev = None
            self.start = self.start.next

    def delete_last(self):
        if self.is_empty():
            print("List is Empty!")
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None

    def delete_data(self, delete_value):
        if self.is_empty():
            print("List is Empty!")
        elif self.start.next == None:
            if self.start.data == deleted_item:
                self.start = None
        else:
            temp = self.start
            if temp.data == delete_value:
                self.start = temp.next
            else:
                while temp != None:
                    if temp.data == delete_value:
                        temp.prev.next = temp.next
                        break
                    temp = temp.next

    def delete_DLL(self):
        self.start = None

    def __iter__(self):
        return Iterator(self.start)


class Iterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
