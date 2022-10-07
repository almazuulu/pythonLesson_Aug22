#Создание лямбда функции
from typing import List

def sayHello():
    print('Hello world!')

sayHello()
sayHello()

hello = lambda : print('Hello world!')

def powNumberFunc(n1, n2):
    print(n1 ** n2)

powNumber = lambda n1, n2: print(n1 ** n2)

powNumber(5,2)
powNumberFunc(5,2)

def mathFunction(n1, n2, n3, lf):
    result = lf(n1, n2, n3)
    print(result)

mathFunction(23,43,5, lambda a, b, c: (a * b) + c)
mathFunction(23,5,2, lambda a, b, c: f'1 ая цифра это: {a} а '
                                      f'возведение в степень второго числа третьим = {b**c}')

def select_oper(option):

    if option == 1:
        return lambda n1, n2, n3: n1 + n2 + n3
    elif option == 2:
        return lambda n1, n2: n1 * n2
    else:
        return lambda n1, n2: n1**n2


f1 = select_oper(2)
f2 = select_oper(3)
f3 = select_oper(1)
print(f1(23,4))
print(f3(23,4,7))

checkNum = lambda n1, n2: 'Even' if (n1 * n2) % 2 == 0 else 'Odd'
print(checkNum(3,5))



