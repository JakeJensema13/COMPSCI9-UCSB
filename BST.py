from TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None  # A BST just needs a reference to the root node
        self.size = 0  # Keeps track of number of nodes

    def length(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    # helper method to recursively walk down the tree
    def _put(self, key, val, currentNode):
        print(currentNode)
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = \
                    TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = \
                    TreeNode(key, val, parent=currentNode)

    def get(self, key):  # returns payload for key if it exists
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    # helper method to recursively walk down the tree
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)


bst = BinarySearchTree()
print(bst.root)
print(bst.length())

bst.put(1, 'one')
print(bst.root.payload)
print(bst.root.hasLeftChild())
