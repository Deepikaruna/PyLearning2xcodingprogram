# Encapsulation
# Inheritance
#polymorphism(method overridng and method overloading)


# Abstraction - oops
# It means hiding the details and showing what is required
#Abstract base class and abstract base methods

from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod  # Method defining
    def sound(self):
        pass
class Dog(Animal):
    pass
    def sound(self):
        return "Bow Bow"

class Cat(Animal):
    pass
    def sound(self):
        return ("Meow Meow")

dog = Dog("Rancho")
cat = Cat("Cutie")
print(dog.sound())
print(cat.sound())
