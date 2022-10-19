class Person:
    def __init__(self, name, age, adress, lst_childrenNames):
        # print('Человек родился!')
        self.nperson = name
        self.ageperson = age
        self.aperson = adress
        self.kidsList = lst_childrenNames

    def display_info(self):
        print(f'Этого человека зовут: {self.nperson}'
              f'\nВозраст этого человека: {self.ageperson}'
              f'\nАдрес этого человека: {self.aperson}')

    def sayHello(self):
        print(f'Привет от {self.nperson}')

    def showKids(self, schoolname):
        print(f'Все дети учатся в {schoolname}: ')

        for k in self.kidsList:
            print(k)

    def sleep(self):
        print(f'Я - {self.nperson} сплю у себя дома по адресу {self.aperson}')

p1 = Person('Askar', 23, 'Lev Tolstoy 22', ['Idris', 'Aisuluu', 'Aiperi'])
p1.nperson = 'Samat'
p1.aperson = 'Sovetskaya 22'

p2 = Person('Peter', 55, 'Baker Street 123', ['Adam'])

# p1.display_info()
# p2.display_info()
# p2.sleep()
# p1.sayHello()
# p1.display_info()


# p1.name = 'Askar'
# p1.age = 23
# print(p1.name)
# p1.sayHello()
#
# p2 = Person()
# p2.name = 'Adilet'
# print(p2.name)
# p2.sleep()


print(p1.aperson, p1.nperson, p1.ageperson)
p1.wifeName = 'Alina Maratova'
print(p1.aperson, p1.nperson, p1.ageperson, p1.wifeName)
p1.display_info()
#
# print(p2.wifeName)

p1.showKids('Lenin')
p2.showKids('61')

n = 2
print(n.bit_count())
print(type(n))

name = 'sdssdas'
sList = name.split()
print(type(name))

# class Str:
#     def split(self):
#         someList = []
#         for ...:
#             someList.append(c)
#         return  someList
print(type(p1))



