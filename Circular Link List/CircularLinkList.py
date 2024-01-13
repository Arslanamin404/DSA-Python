class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last == None

    def insert_at_start(self, data=None):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node

        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def insert_at_last(self, data=None):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def search(self, data=None):
        if self.is_empty():
            return None
        else:
            temp = self.last.next
            while temp != self.last:
                if temp.data == data:
                    return temp
                temp = temp.next
            # Check the last node
            if temp.data == data:
                return temp
            return None

    def display(self):
        if self.is_empty():
            print("List is EMPTY!")
        else:
            current = self.last.next
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.last.next:
                    break

    def insert_after(self, search_data=None, data=None):
        temp = self.search(search_data)
        if temp is not None:
            new_node = Node(data, temp.next)
            temp.next = new_node
            if temp == self.last:
                self.last = new_node

    def delete_start(self):
        if self.is_empty():
            print("List is Empty!")
        else:
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if self.is_empty():
            print("List is Empty!")
        else:
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data=None):
        if not self.is_empty():
            # if only one node is present
            if self.last.next == self.last and self.last.data == data:
                self.last = None
            else:
                # if the deleted data was present in first node
                if self.last.next.data == data:
                    self.delete_start()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        # if the deleted data was present in last node
                        if temp.next == self.last and self.last.data == data:
                            self.delete_last()
                            break
                        if temp.next.data == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    def __iter__(self):
        return Iterator(self.last.next)


class Iterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None or (self.current == self.start and self.count == 1):
            raise StopIteration
        else:
            self.count = 1
            data = self.current.data
            self.current = self.current.next
            return data
