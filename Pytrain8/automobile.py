class Automobile:
    def __init__(self, make, model, mileage, price):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price

    def set_make(self):
        self.make=make

    def set_model(self):
        self.model=model

    def set_mileage(self):
       self.mileage=mileage

    def set_price(self):
       self.price=price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_mileage(self):
        return self.mileage


    def get_price(self):
        return self.price

n=Automobile(40,'swift',44,6600)
print(n.get_model())
print(n.get_make())
print(n.get_mileage())
print(n.get_price())
