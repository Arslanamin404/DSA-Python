class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data=None):
        if self.is_empty():
            new_node = Node(None, data, None)
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node
        else:
            new_node = Node(self.start.prev, data, self.start)
            self.start.prev.next = new_node
            self.start.prev = new_node
            self.start = new_node

    def insert_at_last(self, data=None):
        if self.is_empty():
            new_node = Node(None, data, None)
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node
        else:
            new_node = Node(self.start.prev, data, self.start)
            self.start.prev.next = new_node
            self.start.prev = new_node

    def search(self, data=None):
        if self.is_empty():
            return None
        else:
            temp = self.start
            while True:
                if temp.data == data:
                    # print("Found")
                    return temp
                temp = temp.next
                if temp == self.start:
                    break
            return None

    def insert_after(self, after_wala=None, data=None):
        temp = self.search(after_wala)
        if temp is not None:
            if temp.next == self.start:
                # self.insert_at_last(data)
                new_node = Node(self.start.prev, data, self.start)
                self.start.prev.next = new_node
                self.start.prev = new_node
            else:
                new_node = Node(temp, data, temp.next)
                temp.next.prev = new_node
                temp.next = new_node

    def display(self):
        current = self.start
        if self.is_empty():
            print("Empty List")
        else:
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.start:
                    break

    def delete_first(self):
        if self.start.next == self.start:
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def delete_last(self):
        if self.start.next == self.start:
            self.start = None
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev

    def delete_data(self, deleted_val=None):
        if self.start.next == self.start and self.start.data == deleted_val:
            self.start = None
        else:
            if self.start.data == deleted_val:
                self.delete_first()
            else:
                temp = self.start
                while True:
                    if temp.data == deleted_val:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                    temp = temp.next
                    if temp == self.start:
                        break

    def __iter__(self):
        return Iterator(self.start)


# copy paste iterator🤣😉
class Iterator:
    def __init__(self, start):
        self.temp = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.temp == None or (self.current == self.start and self.count == 1):
            raise StopIteration
        else:
            self.count = 1
            data = self.current.data
            self.current = self.current.next
            return data


if __name__ == "__main__":
    myList = CDLL()
    myList.insert_at_start(30)
    myList.insert_at_start(20)
    # myList.insert_at_start(10)
    # myList.insert_at_last(40)
    # myList.insert_at_last(50)
    # myList.insert_after(10, 15)
    # myList.insert_after(50, 60)
    print("\n----------------------------")
    myList.display()
    print("\n----------------------------\n\n")
    print("After Deletion:")
    # myList.delete_first()
    # myList.delete_first()
    # myList.delete_last()
    # myList.delete_last()
    myList.delete_data(30)
    print("----------------------------")
    myList.display()
    print("\n----------------------------\n\n")
