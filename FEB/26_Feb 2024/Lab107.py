# Single inheritance

class Father:

    gold = 5
    def drive_car(self):
        print("Lambo")

    def threeBhkFlat(self):
        print("3bhk flat")


class Son(Father):
    pass


deepika = Son()
deepika.drive_car()
deepika.threeBhkFlat()
print(deepika.gold)

mmd = Father()
mmd.drive_car()
mmd.threeBhkFlat()
mmd.gold