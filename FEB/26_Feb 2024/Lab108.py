# Multilevel inheritance

class GF:
    def home(self):
        print("5BHK Flat")
class Father(GF):
    pass
    def home2(self):
        print("GOA")
class Son(Father):
    pass
    def home3(self):
        print("BANGALORE")

kpy = Son()
kpy.home()
kpy.home2()
kpy.home3()

mmd = Father()
mmd.home()
mmd.home2()

gkd = GF()
gkd.home()