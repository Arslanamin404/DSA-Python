from SinglyLinkedList import *

myList1 = SLL()
myList2 = SLL()

# List 1
myList1.insert_at_start(30)
myList1.insert_at_start(20)
myList1.insert_at_start(10)
myList1.insert_after(30, 40)
myList1.insert_at_last(50)


# List 2
myList2.insert_at_start(70)
myList2.insert_at_start(60)
myList2.insert_after(70, 80)
myList2.insert_at_last(90)
myList2.insert_at_last(100)


print("List 1 ")
for x in myList1:
    print(x, end=" ")


print("\n\nList 2 ")
for x in myList2:
    print(x, end=" ")


print("\n\n-------------------------------")
search_data = int(input("Enter number to search in SLL: "))
if (myList1.search(search_data)):
    print(" >> Found in list << ")
else:
    print(" >> Not found in list << ")
