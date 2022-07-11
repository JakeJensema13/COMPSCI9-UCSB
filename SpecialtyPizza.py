from Pizza import *
from CustomPizza import *

class SpecialtyPizza:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        if self.size == "S":
            self.price = float(12.00)
        if self.size == 'M':
            self.price = float(14.00)
        if self.size == 'L':
            self.price = float(16.00)

    def getPrice(self):
        return self.price
    def getSize(self):
        return self.size

    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n".format(self.size, self.name, self.price)
