from CircularLinkList import *
MyList = CLL()

MyList.insert_at_start(30)
MyList.insert_at_start(20)
MyList.insert_at_start(10)
MyList.insert_at_last(40)
MyList.insert_at_last(50)
MyList.insert_at_last(60)
MyList.insert_at_last(70)
MyList.insert_after(60, 65)
MyList.insert_after(70, 80)

print("Before Deletion: ")
MyList.display()
print()
for x in MyList:
    print(x, end=" ")

print("\n\nAfter Deletion: ")
MyList.delete_start()
MyList.delete_last()
MyList.delete_item(10)
MyList.delete_item(80)
MyList.display()
print()
for x in MyList:
    print(x, end=" ")
