# class and objects in python
# class - Attributes & behaviour

# person class --> object deepi,kanu

class Person:
    # Attributes - > Data members
    name = None
    age = 32
    id = None
    phone_no = None

    # Behaviour -> Methods ( not the functions). Whenever functions are used
    # in the class itis called methods
    # self will be the first arugument which is nothing but instance in the class
    # self is instance reference
    # functions can be independent wheres methods are part of the cla


def talk(self):
    print("I can talk")


def sleep(self, name):
    print("I am a method")
    print("Sleep")


def walk(self):
    return "I am walking"


def another():
    print("I am a function")


# creating objects - class name()
deepika = Person()
deepika.name = "deepika"
print(deepika.name)

kanu = Person()