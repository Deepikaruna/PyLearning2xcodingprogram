class Person:
        # Class variables/instance variable we should create then
    name = None
    age = None

# Then method declaration(function)

    def walk(self):
        a = 10  # local variable
        print("Hi your name is", self.name)
        print("Hi your age is", self.age)
        print(a)

# to create an objects
amit = Person()
amit.walk()
