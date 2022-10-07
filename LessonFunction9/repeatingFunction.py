#Task 5
"""
Написать лямбду выражение, которое принимает в себя два аргумента num1 и
num2 и возвращает результат деления num2 на num1
"""

devFind = lambda n1, n2: n1/n2
print(devFind(4,2))


#Task 6

""""
Необходимо создать функцию, которая, принимая в себя какое-нибудь число
возвращает ответ «Четное» или «Не четное» значение. Далее на основе этой
функции необходимо проверить данный список [12,33,45 ,4,54,1,32,11 ,67,88]
используя ранее созданную функцию на «Четность» или «Не четность»
используя map. У вас должен вернуться следующий новый список:
"""

def chot(n):
 if n % 2:
  return "Ne chotnoe"
 else:
  return "Chetnoe"

numsList = list(map(chot, [23, 12, 15, 20]))
print(numsList)

#Генераторы списков
lst = [23, 12, 15, 20]
numsList2 = ['Четное' if el % 2 == 0 else 'Не четное' for el in lst]
print(numsList2)

#Функция
def checkNum(lst):
    newList = []
    for el in lst:
        if el % 2 == 0:
           newList.append('Четное')
        else:
           newList.append('Не четное')
    return newList

print(checkNum(lst))

#Task 7

"""
Есть следующий список:
[‘HELLO’,’HOW ARE YOU’, ‘I AM FINE’, ‘THANK YOU’]

Используя map и лямбду выражения создайте новый список, в котором
содержится этот же список, но в нижнем регистре.
"""

#Генератор списка
lst=['HELLO','HOW ARE YOU', 'I AM FINE', 'THANK YOU']
newList = [el.lower() for el in lst]
print(newList)

def makeLower(lst):
    newList = []
    for el in lst:
        newList.append(el.lower())

    return newList
print(makeLower(lst))






