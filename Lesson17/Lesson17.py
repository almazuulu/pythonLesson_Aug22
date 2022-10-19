class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    def __makeCapital(self, name):
        return name.capitalize()

    def display(self):
        print(self.__name, self.__age, self.__address)

    def get_address(self):
        return self.__address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, newname):
        self.__name = self.__makeCapital(newname)

    def get_age(self):
        return self.__age

    def set_age(self, newage):
        if newage > self.__age:
            self.__age = newage
        else:
            print(f'Новый возраст {newage}'
                  f' не должен быть моложе текущего возраста {self.__age}')

p1 = Person('Adilet', 23, 'L Tolstoy 123')

# p1.name = 'Samat'
# print(p1.name)

p2 = Person('Tilek', 23, 'Sov 123')
# print(f'Второго человека зовут {p2.get_name()}')

# p1.set_age(21)
p1.set_age(25)
p1.display()

# p1.set_name('timur')
p1.display()

print(p1.name)
p1.name = 'esen'
p1.display()
# print(p1.get_age())
