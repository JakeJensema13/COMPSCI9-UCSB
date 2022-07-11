from Pizza import  *
from CustomPizza import *
from SpecialtyPizza import *

class PizzaOrder:

    def __init__(self, time):
        self.time = time
        self.pizza = ''
        self.total = float(0)

    def setTime(self, time):
        self.time = time
    def getTime(self):
        return self.time
    def addPizza(self, pizza):
        self.pizza += (pizza.getPizzaDetails() + "\n" +"----" + "\n")
        self.total += pizza.getPrice()


    def getOrderDescription(self):
        return "******\nOrder Time: {}\n{}\nTOTAL ORDER PRICE: ${:.2f}\n******\n".format(self.time,self.pizza[slice(0, len(self.pizza)-1)], self.total )

cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000) #12:30:00PM
order.addPizza(cp1)
order.addPizza(sp1)
#print(order.getOrderDescription())

'****[72 chars]\n---\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ p[150 chars]****'
'****[72 chars]\n----\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ [155 chars]**\n'

