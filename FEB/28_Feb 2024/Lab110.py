#Hierarchical inheritance

class Vehicle:
    def info(self):
        return  "This is a vehicle"

class Car(Vehicle):
    def info(self):
        return "This is a Car"
class Bicycle(Vehicle):
    def info(self):
        return "This is a Bicycle"

car = Car()
bicycle = Bicycle()

print(car.info())