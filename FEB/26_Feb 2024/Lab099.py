class Car:
    name = None
    make = None
    model = None

    def __init__(self):
        print("Hello i will be called when a object is created") # Defining non-parameter contructor


    def __init__(self,o_name,o_make,o_model): # Special function which will call when object is created
        self.name = o_name
        self.make = o_make
        self.model = o_model
    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)

lambo = Car("lambo","v2","2024")
lambo.start_engine()
print("___________")
xuv = Car("xuv","v6","2023")
xuv.start_engine()

alto = Car()
alto.start_engine()

# this is an example of paramterized contructor