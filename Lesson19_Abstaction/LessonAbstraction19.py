class CanFly:
    def fly(self):
        print('This object flies!')

class Bird(CanFly):
    pass

class AirCraft1(CanFly):
    pass

from abc import ABC, abstractmethod

class AirCraft(ABC):
    @abstractmethod
    def fly(self):
        pass
    @abstractmethod
    def ride(self):
        pass

class Tu154(AirCraft):
    def fly(self):
        print('Летает на высоте 8000 м')

    def ride(self):
        print('Скорость езды 350 км-ч')


class AirBus750(AirCraft):
    def fly(self):
        print('Летает на высоте 10000 м')

    def ride(self):
        print('Скорость езды 550 км-ч')


# a1 = AirCraft()
# a1.fly()

# c1 = CanFly()
# c1.fly()
# b1 = Bird()
# b1.fly()