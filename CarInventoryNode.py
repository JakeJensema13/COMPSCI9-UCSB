from Car import *

class CarInventoryNode:
	def __init__(self , car,  left = None, right = None, parent = None, make = None, model = None, year = None, price = None, root = None):
		self.root = root
		self.cars = []
		self.cars.append(car)
		self.car = car
		self.left = left
		self.right = right
		self.parent = parent
		self.make = make
		self.model = model
		self.year = year
		self.price = price

	def hasRight(self):
		if self.right:
			return True
		return False

	def hasLeft(self):
		if self.left:
			return True
		return False

	def isRoot(self):
		if self.parent == None and self.left == None and self.right == None:
			return True
		return False


	def leaf(self):
		if self.left or self.right:
			return False
		return True

	def bothKids(self):
		if self.right and self.left:
			return True
		return False

	def isLeft(self):
		if self.getMake() < self.parent.getMake() or (self.getMake() == self.parent.getMake() and self.getModel() < self.parent.getModel()):
			return True
		return False

	def isRight(self):
		if self.getMake() > self.parent.getMake() or (self.getMake() == self.parent.getMake() and self.getModel() > self.parent.getModel()):
			return True
		return False


	def getYear(self):
		return self.year

	def setParent(self, parent):
		self.parent = parent

	def setRight(self, right):
		self.right = right

	def setLeft(self, left):
		self.left = left

	def getParent(self):
		return self.parent

	def getRight(self):
		return self.right

	def getLeft(self):
		return self.left

	def getMake(self):
		return self.car.getMake()

	def getModel(self):
		return self.car.getModel()

	def getPrice(self):
		return self.car.getPrice()

	def replaceNodeData(self, key, value, lc, rc):
		self.key = key
		self.payload = value
		self.left = lc
		self.right = rc

		if self.hasLeft():
			self.left.parent = self
		if self.hasRight():
			self.right.parent = self



	def __str__(self):
		carss = ''
		for i in self.cars:
			if i.getMake() == self.cars[0].getMake() and i.getModel() == self.cars[0].getModel():
				carss += (str(i)) + "\n"
		return carss


cn = CarInventoryNode
car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
carNode = CarInventoryNode(car1)
carNode.cars.append(str(car2))
