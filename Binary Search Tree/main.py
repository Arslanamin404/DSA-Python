from bst import *
tree = BST()
tree.insert(90)
tree.insert(80)
tree.insert(15)
tree.insert(120)
tree.insert(92)
print("\n---------------------------------------------")
# result = tree.inOrder()

print(f"InOrder Traversing: {tree.inOrder()}\n", end=" ")
print(f"\nPreOrder Traversing: {tree.preOrder()}\n", end=" ")
print(f"\nPostOrder Traversing: {tree.postOrder()}\n", end=" ")

print(f"\nMin Value in Tree: {tree.get_min()}")
print(f"\nMax Value in Tree: {tree.get_max()}")
print(f"\nSize of Tree = {tree.get_size()} elements")

print("---------------------------------------------")
tree.delete(120)
print(f"After Deletion\n{tree.inOrder()}\n", end=" ")
print(f"\nSize of Tree = {tree.get_size()} elements")

print("---------------------------------------------\n\n")
