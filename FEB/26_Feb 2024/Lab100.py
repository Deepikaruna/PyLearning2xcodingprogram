# Web automation - Selenium
# Every page you going to automate


class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def loginconfimr(self):
        if self.password == "Pass123":
            print("You are allowed to enter")
        else:
            print("Invalid user")

amit = VWOLoginPage("amit@amit.com", "123")
amit.loginconfimr()
print("_____________")
deepika = VWOLoginPage("deepika@deepi.com", "Pass123")
deepika.loginconfimr()

print(id(amit)) # id basically means where they are stored references
print(id(deepika))