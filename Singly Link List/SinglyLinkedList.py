# ------------ Singly Linked List ------------ #
# * check notebook for detailed logic and diagram for better understanding
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start
        # self.count = 0

    def is_empty(self):
        return self.start == None

    def search(self, data=None):
        temp = self.start
        while temp != None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def insert_at_start(self, data=None):
        new_node = Node(data, self.start)
        self.start = new_node
        # self.count += 1

    def insert_at_last(self, data=None):
        new_node = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        else:
            self.start = new_node
        # self.count += 1

    def insert_after(self, insert_after=None, data=None):
        temp = self.search(insert_after)
        if temp is not None:
            new_node = Node(data, temp.next)
            temp.next = new_node
        else:
            print(f"The node with data {insert_after} was not found.")
        # self.count += 1

    def display(self):
        temp = self.start
        if self.start == None:
            print("List is Empty")
        else:
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next

    def delete_at_start(self):
        if self.is_empty():
            print("List is Empty!")
        else:
            temp = self.start
            self.start = temp.next
        # self.count -= 1

    def delete_at_last(self):
        # if list is empty
        if self.is_empty():
            print("List is Empty!")
        # if only 1 node is present
        elif self.start.next == None:
            self.start = None
        # if more than 2 nodes are present
        else:
            temp = self.start
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
        # self.count -= 1

    def delete_data(self, deleted_item):
        # if list is empty
        if self.is_empty():
            print("List is Empty!")
        # if only 1 node is present
        elif self.start.next == None:
            if self.start.data == deleted_item:
                self.start = None
        # if more than 2 nodes are present
        else:
            temp = self.start
            # if we want to delete first node
            if temp.data == deleted_item:
                self.start = temp.next
            else:
                while temp.next != None:
                    if temp.next.data == deleted_item:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
        # self.count -= 1

    def __iter__(self):
        return SLLIterator(self.start)

    def __len__(self):
        count = 0
        current = self.start
        while current:
            count += 1
            current = current.next
        return count

    def delete_SLL(self):
        self.start = None
        # self.count = 0


class SLLIterator:
    def __init__(self, start):
        # * Initialize the iterator with the starting node
        self.current = start

    def __iter__(self):
        # * Make the iterator object itself iterable enabling it to be used in a for loop or other iterable directly.
        return self

    def __next__(self):
        # * Check if the current node is None (end of linked list).
        if not self.current:
            # If it is the end, raise StopIteration to signal the end of iteration.
            raise StopIteration

        # Retrieve the data from the current node.
        data = self.current.data
        # Move the iterator to the next node.
        self.current = self.current.next
        # Return the data of the current node.
        return data


if __name__ == "__main__":
    myList = SLL()
    myList.insert_at_start(50)
    myList.insert_at_start(10)
    myList.insert_at_start(5)
    myList.insert_at_last(90)
    myList.insert_at_last(99)
    myList.insert_after(50, 20)
    myList.insert_after(99, 100)
    

    print(myList.is_empty())
    print("\nBefore Deletion: ")
    print(f"Length of SLL = {len(myList)}")
    # print(f"Length of SLL using count = {myList.count}")
    for x in myList:
        print(x, end=" ")
    # myList.display()

    print("\n\nAfter Deletion: ")

    myList.delete_at_start()
    myList.delete_at_last()
    myList.delete_data(50)
    myList.delete_data(99)

    print(f"Length of SLL = {len(myList)}")
    # print(f"Length of SLL using count = {myList.count}")

    for x in myList:
        print(x, end=" ")
    # myList.display()

    print("\n\nAfter deleting Link List: ")
    myList.delete_SLL()
    print(f"Length of SLL = {len(myList)}")
    # print(f"Length of SLL using count = {myList.count}")
