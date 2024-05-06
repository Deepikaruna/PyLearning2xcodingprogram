class calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = calculator()
result = object_ref.sum(3, 4)
print(result)

object_ref1 = calculator()
result = object_ref1.sub(3, 4)
print(result)

object_ref2 = calculator()
result = object_ref2.mul(3, 4)
print(result)

object_ref3 = calculator()
result = object_ref3.div(3, 4)
print(result)
