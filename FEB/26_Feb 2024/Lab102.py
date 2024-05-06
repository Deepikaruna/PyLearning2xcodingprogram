#Encapsulation example - bind the data variables and methods(hide the important variables)
# Datamembers/class variables
#functions- they are closed within a single blueprint
#wrapping or binding the data variabls with the methods
#Disadvantage of encapsulation is not hiding all data variables like password which is sensitive
# so they introduced 3 different type of data memebers/class variables

class Car:
    name = None
    # 3 different type of data memebers/class variables

    def __init__(self):
        self.public_var = "public"   # public - Anyone can access it
        self._protected_variable = "protected123"
        self.__private_var = "pass@123"
    def _protectedmethod(self):
        print("Protected!")
    def _privatemethod(self):
        print("Private!")
    def printName(self):
        print(self.name)

xuv = Car()
xuv.printName()

#Lambo = Car("Lambo")
#Lambo.printName()

#print(xuv.name)
#by using different methods we can access the protected and private variables

print(xuv.public_var)
print(xuv._protectedmethod())
print(xuv._privatemethod())