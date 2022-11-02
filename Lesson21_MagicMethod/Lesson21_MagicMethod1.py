class Person:
    def __init__(self, name, age, adress, children):
        self.__name = name
        self.__age = age
        self.__adress = adress
        self.children = children

    def __str__(self):
        return f'Человека звать {self.__name} и ему {self.__age} лет'

    def __add__(self, other):
        if isinstance(other, int):
            return self.__age + other
        return self.__age + other.__age

    def __iadd__(self, other): #p1+=1
        return self.__age + other

    def __radd__(self, other):
        if isinstance(other, int):
            return self.__age + other
        return self.__age + other.__age

    def __sub__(self, other):
        if isinstance(other, int):
            return self.__age - other
        return self.__age - other.__age

    def __isub__(self, other): #isub p1-=1
        if isinstance(other, int):
            return self.__age - other
        return self.__age - other.__age

    def __rsub__(self, other):
        if isinstance(other, int):
            return self.__age - other
        return self.__age - other.__age

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__age * other
        return self.__age * other.__age

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.__age * other
        return self.__age * other.__age

    def __mod__(self, other):
        if isinstance(other, int):
            return self.__age % other
        return self.__age % other.__age

    def __rmod__(self, other):
        if isinstance(other, int):
            return self.__age % other
        return self.__age % other.__age

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__age / other
        return self.__age / other.__age

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__age / other
        return self.__age / other.__age


    # def __divmod__(self, other):
    #     return self.__age % other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def __gt__(self, other):
        return self.__age > other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    def __ge__(self, other):
        return self.__age >= other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __contains__(self, item):
        return item in self.__name

    def __reversed__(self):
        return self.__name[::-1]

    def __index__(self, other):
        return self.__name.find(other)

    def __delattr__(self, item):
        self.children.remove(item)

    def __delitem__(self, key):
        del self.children[key]

    def __call__(self, salary):
        salaryTotal = None
        if self.__age > 50:
            salaryTotal = (self.__age - 50) * salary
        else:
            print(self.__age * salary * 0.5)

        print(f'Заработная плата для артиста: {salaryTotal}')

    # def __del__(self):
    #     print('Deleted object')

    def __len__(self):
        return len(self.children)
#
# p1 = Person('Tom Cruise', 65, 'Bav Hills 123', ['Timur Cruise'])
# p2 = Person('Michael Jackson', 61, 'Baker Street 1234', ['Selena Jackson', 'Peter Jackson', 'Rinat Jackson'])
# p3 = Person('Peter Frank', 5, 'LA Lincoln Street 123', [])
# #
# # print(p1.name)
# # print(p2.name)
#
# print(p1)
# print(p2)
# print(p1 % 15)
# print(p1 / p3)
# print(p1 / 20.3)
#
# print(100 + p3)
# print(1000/ p1)
#
# print('Tom' in p1)
# p1(500000)
# p2(500000)
#
# print(len(p1))
# print(len(p2))
# #
# # del p1[0]
# # del p2[1]
# # del p2[1]
# #
# # print(len(p1))
# # print(len(p2))
#
#
# # p1.__delattr__('Timur Cruise')
# # print(p1.children)
# # del p1
#
#
# # print(p1.__reversed__())
#
# # someList = ['asd', 'asd', 'dfa', 'tr']
# # someList.reverse()
# # print(someList)
# # words = ['Bishkek', 'Moscow', 'Ekaterenburg']
# # print('Bishkek' in words)
#
#
# #
# # print(p1 + p2)
# # print(p1 - p2)
# # print(p1 * p2)
# # print(p1 == p2)
# # print(p2 > p1)
# # print(p1 < p2)
# #
# # print(p1 >= p2)
# # print(p1 <= p2)
# # # print(p1 + 200)
# #
# # print(p1 + 200)
# # print(200 + p1)

"""
Создать класс Банковский аккаунт, с аттрибутами id, баланс, 
имя владельца аккаунта, список счетов :[euro, som, ruble] и тд 

Создать магические методы:
 -  Для добавления средств
 -  Для измерения кол-во списка счетов
 -  Для умножения средств 
 -  Для сравнения счетов
 - Создайте вызывающий магический метод, который посчитает общую сумму 
 за сохранение денег на счету в течении определенного кол-ва лет
 пример: 
 acc1(summaObsluzh, kolvoLet) 
"""

class BankAccount:
    def __init__(self, id , balance, name, listId):
        self.__id = id
        self.__balance = balance
        self.__name = name
        self.__listId = listId

    def __add__(self, other):
        if type(other) == int:
            return self.__balance + other
        return self.__balance + other.__balance

    def __len__(self):
        return len(self.__listId)

    def __mul__(self, other):
        if type(other) == int:
            return self.__balance * other
        return self.__balance * other.__balance

    def __ge__(self, other):
        if type(other) == int:
            return self.__balance >= other
        return self.__balance >= other.__balance

    def __call__(self,summaObsluzh,kolvoLet):
        totalAmt = self.__balance - (summaObsluzh * kolvoLet)
        return f'Общая сумма после обслуживания в течении {kolvoLet} составляет {totalAmt}'

acc1 = BankAccount(213123123123, 50000, 'Sergei Valerievich', ['euro', 'som', 'ruble'])
acc2 = BankAccount(21312312332, 40000, 'Valeriy Valerievich', ['euro', 'som', 'dollar'])

print(acc1(summaObsluzh = 500, kolvoLet = 10))
print(acc2(summaObsluzh = 650, kolvoLet = 15))








