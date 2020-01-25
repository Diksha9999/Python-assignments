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

class Car(Automobile):
    def __init__(self,make,model,mileage,price,doors):
        Automobile.__init__(self,make,model,mileage,price)
        self.doors= doors

        def set_doors(self,doors):
           self.doors=doors

        def get_doors(self):
            return self.doors

class Truck(Automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        Automobile.__init__(self, make, model, mileage, price)
        self.drive_type=drive_type

        def set_drive_type(self,dt):
           self.drive_type=dt

        def get_drive_type(self):
            return self.drive_type

class SUV(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        Automobile.__init__(self, make, model, mileage, price)
        self.pass_cap=pass_cap

        def set_pass_cap(self,s):
            self.pass_cap=s
        def get_pass_cap(self):
            return self.pass_cap



def main():
    n = Automobile(40, 'swift', 44, 6600)
    print(n.get_model())
    print(n.get_make())
    print(n.get_mileage())
    print(n.get_price())

    a= Automobile.Car(33,'caaar',40,55,55)
    print(a.get_doors())

main()

