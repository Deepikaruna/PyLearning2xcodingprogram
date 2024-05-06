# Multiple inheritance
# Father, mother -->Son

class Father:
    def father_money(self):
        return "5"

    def home(self):
        return "This is from the Father"


class Mother:
    def mother_money(self):
        return "10"

    def home(self):
        return "This is from the Mother"

class Son(Mother, Father):
    pass


son = Son()
print(son.father_money())
print(son.mother_money())
print(son.home())
#MRO - Method Resolution Order

