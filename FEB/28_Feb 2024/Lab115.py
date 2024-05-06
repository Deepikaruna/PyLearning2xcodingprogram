# Method Overriding - Same name in parent and the child
# child always override the parent function
# super means call my parent function

class Animal():

    def __init__(self):
        pass
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def __init__(self):
        pass
    def sound(self):
            super().sound()
            print("Dog Sound")

#animal = Animal()
#animal.sound()

dog = Dog()
dog.sound()
