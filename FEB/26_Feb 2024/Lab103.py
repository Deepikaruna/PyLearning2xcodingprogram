class MyClass:

    def __init__(self):
        self.name = "Amit"
    def public_func(self):
        print("public function")

    def __private_func(self):
        print("This is private")

    # to access private
    def public_fn_private(self):
        self.__private_func()
    # security --> Not everyone can access your variables

a = MyClass()
a.public_func()
a.__private_func: