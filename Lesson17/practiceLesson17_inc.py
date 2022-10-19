#Task 2
"""
name, age, address, can_vote (Можно будет установить
«да», «нет. По умолчанию для can_vote установлен
параметр «Да», а для возраста установлен 18)
• В конструктор нужно передавать все атрибуты, кроме
can_vote. Атрибут can_vote устанавливается в
зависимости от возраста человека.
• Создать геттер и геттер для age, name, address
• В сеттере происходит настройка возраста, затем в
зависимости от возраста can_vote становится “Да”, если
возраст человека выше либо равно 18-ти, иначе атрибут
can_vote принимает в себя «Нет».
• Создайте метод для отображение всех информаций о
человеке.
Создайте необходимые экземпляры класса и передайте в
конструктор все соответствующие параметры
"""
class Person:
    def __init__(self,name, address, age=18):
        self.__name = name
        self.__age = age
        self.__adress = address
        self.__canVote = None

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,newAge):
        self.__age = newAge
        if newAge >= 18:
            self.__canVote = 'Yes'
        else:
            self.__canVote = 'No'
    # def getAge(self):
    #     return self.__age
    #
    # def setAge(self,newAge):
    #     self.__age = newAge
    #     if newAge >= 18:
    #         self.__canVote = 'Yes'
    #     else:
    #         self.__canVote = 'No'
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname

    def getAddress(self):
        return self.__adress

    def setAddress(self, newaddress):
        self.__adress = newaddress

    def display(self):
        print(self.__name, self.__age, self.__adress, self.__canVote)

p1 = Person('Adam', 'B Street 123', 23)
p1.age = 30
p1.display()
