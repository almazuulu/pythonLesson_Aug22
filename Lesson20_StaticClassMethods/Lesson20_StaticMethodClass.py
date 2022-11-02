from datetime import date

class Car:
    def __init__(self, carName, yearProduction):
        self.carName = carName
        self.yearProduction = yearProduction
        self.somePar = 10

    def display(self):
        print(f'Я машина, с именем {self.carName}')

    @classmethod
    def classMethod(cls,carName,yearProduction):
        return cls(carName, date.today().year - yearProduction)

    @staticmethod
    def staticMethod(yearProduction):
        return yearProduction


car1 = Car('Toyota 200', 2008)
car2 = Car.classMethod('Audi 100', 1999)
car3 = Car('Rolce Royce', 2012)

print(car1.carName)
print(car1.yearProduction)

print(car2.carName)
print(car2.yearProduction)

print(car3.staticMethod(2005))
print(car1.yearProduction)



# car2 = Car('Audi 100', 1999)



# car1.carName = 'BMW X5'

# car1.display()
# car2.display()

# print(car1.classMethod())


# print(car2.classMethod())
#
# print(car1.staticMethod())
# print(car2.staticMethod())


