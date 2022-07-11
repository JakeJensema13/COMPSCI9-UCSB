from Car import Car
from CarInventoryNode import CarInventoryNode


class CarInventory:
    def __init__(self, left=None, right=None, parent=None, make=None, model=None):
        self.root = None  # A BST just needs a reference to the root node
        self.size = 0  # Keeps track of number of nodes
        self.left = left
        self.right = right
        self.parent = parent
        self.make = make
        self.model = model

    def isLeft(self):
        def isLeft(self):
            if self.getMake() < self.parent.getMake() or self.getMake() == self.parent.getMake() and self.getModel() < self.parent.getModel():
                return True
            return False

    def hasAnyChildren(self):
        if self.left or self.right:
            return True
        return False

    def hasRight(self):
        if self.right:
            return True
        return False

    def hasLeft(self):
        if self.left:
            return True
        return False

    def leaf(self):
        if self.left or self.right:
            return False
        return True

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getRoot(self):
        return self.root

    def getLeft(self):
        return self.left

    def getParent(self):
        return self.parent

    def getRight(self):
        return self.right

    def addCar(self, car):
        if self.root:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)
        self.size = self.size + 1

    def size(self):
        return self.size

    def getSuccessor(self, make, model):
        if self.root:
            res = self.__get(make.upper(), model.upper(), self.root)
            if res:
                if res.right:
                    res = res.right
                    while res.left:
                        res = res.left
                    return res

                else:
                    temp = res.parent
                    while temp:
                        if res.getMake() < temp.getMake() or (
                                res.getMake() == temp.getMake() and res.getModel() < temp.getModel()):
                            return temp
                        temp = temp.parent
                    return None
            else:
                return None

    def _addCar(self, car, currentNode):
        if car.getMake() == currentNode.getMake() and car.getModel() == currentNode.getModel():
            currentNode.cars.append(car)
        if car.getMake() < currentNode.getMake() or (
                car.getMake() == currentNode.getMake() and car.getModel() < currentNode.getModel()):
            if currentNode.getLeft():
                self._addCar(car, currentNode.left)
            else:
                currentNode.left = \
                    CarInventoryNode(car, parent=currentNode)
        if car.getMake() > currentNode.getMake() or (
                car.getMake() == currentNode.getMake() and car.getModel() > currentNode.getModel()):
            if currentNode.getRight():
                self._addCar(car, currentNode.right)
            else:
                currentNode.right = \
                    CarInventoryNode(car, parent=currentNode)

    def doesCarExist(self, car):
        if self.root:
            res = self._get(car, self.root)
            if res:
                return True
            else:
                return False
        else:
            return None

    # helper method to recursively walk down the tree
    def __get(self, make, model, currentNode):
        if not currentNode:
            return None
        if currentNode.getMake() == make.upper() and currentNode.getModel() == model.upper():
            return currentNode
        if make < currentNode.getMake():
            return self.__get(make, model, currentNode.left)
        else:
            return self.__get(make, model, currentNode.right)

    def _get(self, car, currentNode):
        if not currentNode:
            return None
        for i in range(0, len(currentNode.cars)):
            if currentNode.cars[i] == car:
                return currentNode
        if car < currentNode.car:
            return self._get(car, currentNode.left)
        else:
            return self._get(car, currentNode.right)

    def ___get(self, make, model, year, price, currentNode):
        if not currentNode:
            return None
        for i in currentNode.cars:
            if i.getMake().upper() == make.upper() and i.getModel().upper() == model.upper() and \
                    i.getYear() == year and i.getPrice() == price:
                return currentNode
        if make < currentNode.getMake():
            return self.___get(make, model, year, price, currentNode.left)
        else:
            return self.___get(make, model, year, price, currentNode.right)


    def inOrder(self):
        return self.inorder(self.root)

    def inorder(self, tree):
        ret = ""
        if tree != None:
            ret += self.inorder(tree.getLeft())
            ret += str(tree)
            ret += self.inorder(tree.getRight())
        return ret

    def preorder(self, tree):
        ret = ""
        if tree != None:
            ret += str(tree)
            ret += self.inorder(tree.getLeft())
            ret += self.inorder(tree.getRight())
            return ret
        else:
            return ret

    def preOrder(self):
        return self.preorder(self.root)

    def postorder(self, tree):
        ret = ""
        if tree != None:
            ret += self.inorder(tree.getLeft())
            ret += self.inorder(tree.getRight())
            ret += str(tree)
            return ret

    def postOrder(self):
        return self.postorder(self.root)

    def removeCar(self, make, model, year, price):
        nodeToRemove = self.___get(make, model, year, price, self.root)
        if self.size > 1 and nodeToRemove:
            for i in nodeToRemove.cars:
                if i.getMake() == make.upper() and i.getModel() == model.upper() and i.getYear() == year and i.getPrice() == price:
                    nodeToRemove.cars.remove(i)
            if len(nodeToRemove.cars) > 0:
                return True
            if len(nodeToRemove.cars) == 0:
                self.remove(nodeToRemove)  # remove modifies the tree
                return True
        elif self.size == 1 and nodeToRemove:
            #self.remove(nodeToRemove)
            self.root = None
            return True

        else:
            return False

    # Used to remove the node and account for BST deletion cases
    def remove(self, currentNode):
        # Case 1: Node to remove is leaf
        if currentNode.leaf():
            if currentNode.isLeft():
                currentNode.parent.left = None
                return True
            elif currentNode.isRight():
                currentNode.parent.right = None
                return True

        # Case 3: Node to remove has both children
        elif currentNode.bothKids():

            # Need to find the successor, remove successor, and replace
            # currentNode with successor's data / payload
            succ = currentNode.getSuccessor(currentNode.getMake(), currentNode.getModel())
            succ.spliceOut()
            currentNode.getMake = succ.getMake()
            currentNode.getModel = succ.getModel()
            currentNode.getYear = succ.getYear()
            currentNode.getPrice = succ.getPrice()

        # Case 2: Node to remove has one child
        else:
            # Node has leftChild
            if currentNode.left:
                if currentNode.isLeft():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                    return True
                elif currentNode.isRight():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right = currentNode.left
                    return True
                else:  # currentNode is the Root
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)

            # Node has rightChild
            else:
                if currentNode.right:
                    if currentNode.isLeft():
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.left = currentNode.right
                        return True
                    elif currentNode.isRight():
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.right = currentNode.right
                        return True
                    else:
                        currentNode.replaceNodeData(currentNode.rightChild.key,
                                                    currentNode.rightChild.payload,
                                                    currentNode.rightChild.leftChild,
                                                    currentNode.rightChild.rightChild)
    def spliceOut(self):
        # Case 1:
        # If node to be removed is a leaf, set parent's left or right
        # child references to None
        if self.leaf():
            if self.left:
                self.parent.left = None
            else:
                self.parent.right = None

        # Case 2:
        # Not a leaf node. Should only have a right child for BST
        # removal
        elif self.hasAnyChildren():
            if self.hasRight():
                if self.isLeft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent




