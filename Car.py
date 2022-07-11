class Car:
    def __init__(self, make, model, year, price):
        self.cars = []
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price

    def getYear(self):
        return self.year


    def __gt__(self, other):
        if self.make > other.make:
            return True
        if self.make == other.make and self.model > other.model:
            return True
        if self.make == other.make and self.model == other.model and self.year > other.year:
            return True
        if self.make == other.make and self.model == other.model and self.year == other.year and self.price > other.price:
            return True
        return False

    def __lt__(self, other):
        if self.make < other.make:
            return True
        if self.make == other.make and self.model < other.model:
            return True
        if self.make == other.make and self.model == other.model and self.year < other.year:
            return True
        if self.make == other.make and self.model == other.model and self.year == other.year and self.price < other.price:
            return True
        return False

    def  __eq__(self, other):
        if self.make == other.make and self.model == other.model and self.year == other.year and self.price == other.price:
            return True
        return False

    def  __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}"


#c1 = Car('aonda', 'cs1', 2001, 2000)
#c2 = Car('bonda', 'cs1', 2001, 1900)

#print(c1)