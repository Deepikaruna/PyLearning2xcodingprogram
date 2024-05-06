from abc import ABC,abstractmethod

class ATB(ABC):

    @abstractmethod  # Method defining
    def perform_task1(self):
        pass

    @abstractmethod  # Method defining
    def perform_task2(self):
        pass
class Kanu(ATB):
    pass
    def sound(self):
        return "Bow Bow"

    def perform_task1(self):
        return "Bow Bow"

    def perform_task1(self):
        return "Meow Meow"

anu = Kanu()
kanu.perform_task1()
kanu.perform_task2()