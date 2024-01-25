class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root
        self.__count = 0

    def is_empty(self):
        return self.root == None

    def insert(self, data=None):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert(data, self.root)
        self.__count += 1

    # * Insert using recursion
    def __insert(self, data=None, current_node=None):
        if data == current_node.data:
            raise ValueError("Duplicate values not allowed in BST!")
        elif data < current_node.data:
            if current_node.left:
                self.__insert(data, current_node.left)
            else:
                current_node.left = Node(data)
        else:
            if current_node.right:
                self.__insert(data, current_node.right)
            else:
                current_node.right = Node(data)

    def search(self, data=None):
        return self.__r_search(self.root, data)

    # using recursion
    def __r_search(self, current_node=None, data=None):
        if current_node is None or current_node.data == data:
            return current_node
        # left subtree
        if data < current_node.data:
            return self.__r_search(current_node.left, data)
        # right subtree
        else:
            return self.__r_search(current_node.right, data)

    def inOrder(self):
        self.__result = []
        self.__r_inOrder(self.root)
        return self.__result

    def __r_inOrder(self, current_node):
        # * Left SubTree --> Root Node ---> Right Subtree
        if current_node:
            self.__r_inOrder(current_node.left)
            self.__result.append(current_node.data)
            self.__r_inOrder(current_node.right)

    def preOrder(self):
        self.__result = []
        self.__r_preOrder(self.root)
        return self.__result

    def __r_preOrder(self, current_node):
        # * Root Node ---> Left SubTree  ---> Right Subtree
        if current_node:
            self.__result.append(current_node.data)
            self.__r_preOrder(current_node.left)
            self.__r_preOrder(current_node.right)

    def postOrder(self):
        self.__result = []
        self.__r_postOrder(self.root)
        return self.__result

    def __r_postOrder(self, current_node):
        # * Left SubTree  ---> Right Subtree ---> Root Node
        if current_node:
            self.__r_postOrder(current_node.left)
            self.__r_postOrder(current_node.right)
            self.__result.append(current_node.data)

    # leaf node of left most subtree contains min value
    def get_min(self):
        return self.__r_min(self.root)

    def __r_min(self, current_node):
        if current_node.left:
            return self.__r_min(current_node.left)
        else:
            return current_node.data

    # leaf node of right most subtree contains max value
    def get_max(self):
        return self.__r_max(self.root)

    def __r_max(self, current_node):
        if current_node.right:
            return self.__r_max(current_node.right)
        else:
            return current_node.data

    def get_size(self):
        return self.__count
