class Password:

    def __init__(self,password):
        self.__password = password
        self.public_var = 10

    # Encapsuslation says use public functions to user private data memebers
    def get_password(self,is_auth):
        if is_auth:
            print (self.__password)
        else:
            print("Invalid password")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
            print("Set to correct",self.password)
        else:
            print("Not allowed, weak password")


pwd = Password("Hacker123")
print(pwd.public_var)
pwd.get_password(False)
pwd.set_password("deepika@123456")
