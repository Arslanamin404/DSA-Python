from bst import *
tree = BST()
tree.insert("Kashmir")
tree.insert("Iraq")
tree.insert("Oman")
tree.insert("Qatar")
tree.insert("Kuwait")
tree.insert("Germany")
tree.insert("France")
tree.insert("Australia")
tree.insert("India")
tree.insert("Pakistan")
tree.insert("Africa")

print("\n---------------------------------------------")
# result = tree.inOrder()

print("InOrder Traversing: ")
print("------------------")
print(tree.inOrder())

print("\n\n------------------")
print("PreOrder Traversing: ")
print("------------------")
print(tree.preOrder())

print("\n\n------------------")
print("PostOrder Traversing: ")
print("------------------")
print(tree.postOrder())

print("\n---------------------------------------------\n\n")
