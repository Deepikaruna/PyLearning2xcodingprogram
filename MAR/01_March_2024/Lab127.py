class xyz:
    def f1(self):
        try:
            a=int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int only values as a")
        else:
            print(a)
        finally:
            print("Anyhow i will be printed")

x = xyz()
x.f1()