from DoublyLinkList import *

myList = DLL()
myList.insert_at_start(60)
myList.insert_at_start(50)
myList.insert_at_start(40)
myList.insert_at_start(30)
myList.insert_at_last(70)
myList.insert_at_last(80)
myList.insert_at_last(90)
myList.insert_at_last(100)
myList.insert_after(100, 110)
myList.insert_after(110, 120)
myList.insert_at_last(130)

print(myList.search(130))
print(myList.search(230))

print("\nBefore Deletion:")
for x in myList:
    print(x, end=" ")

myList.delete_start()
# myList.delete_start()
# myList.delete_last()
# myList.delete_last()
# myList.delete_data(130)

print("\n\nAfter Deletion: ")
for x in myList:
    print(x, end=" ")

# print(myList.start.next.prev)

# user_input = int(input("\n\nEnter the number to check if it is present or not: "))
# print("\n\n------------------------------------")
# print("\tFound in List") if myList.search(
#     user_input) else print(f"\t{user_input}, Not Found in List")
# print("------------------------------------\n\n")
