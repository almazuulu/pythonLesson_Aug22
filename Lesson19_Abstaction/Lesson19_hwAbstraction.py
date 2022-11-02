"""
#Task 1

Есть некий Абстрактный класс Car у которого есть абстрактный
метод brake(), gas() и приватные поля:
• model;
• color;
• maxSpeed;
Реализуйте и переопределите вышеописанные методы в классах
наследниках Sedan, SportCar, FamilyCar

#Task 2

Есть абстрактный класс Person, в нем содержится абстрактный
метод calculateMyExpenses(), whereToEat(), earnMoney()
В классах наследниках Student, BankWorker, Doctor необходимо
переопределить вышеописанные методы для каждого класса по
своему.
"""
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, model, color, maxSpeed):
        self.__model = model
        self.__color = color
        self.__maxSpeed = maxSpeed

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @property
    def speed_max(self):
        return self.__maxSpeed

    @speed_max.setter
    def speed_max(self, speed_max):
        self.__maxSpeed = speed_max

    @abstractmethod
    def gas(self):
        pass

    @abstractmethod
    def brake(self):
        pass

class FamilyCar(Car):
    def __init__(self, modelBabyseat, model, color, maxSpeed):
        self.model = model
        self.color = color
        self.speed_max = maxSpeed
        self.__modelBabySeat = modelBabyseat

    @property
    def modelBabyseat(self):
        return self.__modelBabySeat

    @modelBabyseat.setter
    def modelBabyseat(self, newBabySeat):
        self.__modelBabySeat = newBabySeat

    def gas(self):
        print(f'Максимально можно разогнаться до {self.speed_max} км/ч')

    def brake(self):
        print(f'Семейный автомобиль {self.model} с цветом {self.color} затормозил')


#Task 2
class Person(ABC):
    def __init__(self, name, age, profession, budget):
        self.__name = name
        self.__age = age
        self.__profession = profession
        self.__budget = budget

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.name

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, newProfession):
        self.__profession = newProfession

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, newBudget):
        self.__budget = newBudget

    @abstractmethod
    def calculateMyExpenses(self):
        pass

    @abstractmethod
    def whereToEat(self):
        pass

    @abstractmethod
    def earnMoney(self):
        pass

class Studen(Person):
    def __init__(self,name, age, profession, budget,hrRate, hrWorked):
        self.name = name
        self.age = age
        self.profession = profession
        self.budget = budget
        self.__hrRate = hrRate
        self.__hrWorked = hrWorked

    @property
    def hrRate(self):
        return self.__hrRate

    @property
    def hrWorked(self):
        return self.__hrWorked

    @hrWorked.setter
    def hrWorked(self, newHr):
        self.__hrWorked = newHr

    def earnMoney(self):
        return self.hrRate * self.hrWorked

    def whereToEat(self):
        # locationEat = input('Где вы будете кушать? ')
        # totalMoney =  self.calculateMyExpenses()

        if self.budget == 94:
            print('вы кушаете в KFC')

        elif self.budget == 74:
            print('вы кушаете в Navigator')

    def calculateMyExpenses(self):
        whatToBuy = int(input('Какую сумму потратите на покупку? '))

        totalMoney = self.budget + self.earnMoney() - whatToBuy

        print(f'Денег осталось после покупки: {totalMoney}')
        self.budget = totalMoney

if __name__ == '__main__':
    # famCar = FamilyCar('Chicco', 'Honda Odyssey', 'White', 150)
    # famCar.gas()
    # famCar.brake()

    student1 = Studen('Asan', 20, 'Student', 50, 8, 8)
    student1.calculateMyExpenses()
    student1.whereToEat()

"""
Создать Класс Conditioner
с переменным model, brand, temperature, mode(холодно, жарко)

- Установить температуру в цельции в качестве 
переменного задать новую температуру
Поменять изн установленную температуру

- Создать новый метод, который В зависимости от новой температуры 
возвращает новое измененное значение mode 

- Создать метод для выключение - полностью изменяет температуру на 0
- Метод включение - вы должны спрашивать какую температуру задать?  
и в зависимости от этой температуру новое измененное значение mode (Желательно)

- Создать метод для получения информация - метод Display() 
"""








