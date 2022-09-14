#Task 1
"""
Скопировать элемент 44 и 55 из текущего кортежа в новый кортеж
tuple1 = (11, 22, 33, 44, 55, 66)
"""

tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple1[3:5]
tuple2 = tuple1[-3:-1]
print(tuple2)

#Task 2
""""
Создайте кортеж из имен людей. Выведите все имена через цикл for
по шаблону: "Привет, [ИМЯ]".
"""

name = "Adik", "Maks", "Elena", "Timur"
# print(type(name))
for n in name:
    print(n, end=" ")

#Task 3
"""
Вывести заданный кортеж в обратном порядке:
aTuple = (10, 20, 30, 40, 50)
"""
aTuple = (10, 20, 30, 40, 50)
aTuple2 = aTuple[::-1]
print(aTuple2)

#Task 4
"""
Распаковать нижеследующий кортеж по параметрам :
aTuple = (10, 20, 30, 40)
"""
aTuple = (10, 20, 30, 40, 50, 60, 70)
# a = aTuple[0]
# b = aTuple[1]
# c = aTuple[2]
# d = aTuple[3]

listNum = list(range(10,16))
print(listNum)

a, b, c, d, e, f, h = aTuple
print(c)
print(d)
print(h)

n1, n2, n3, n4, n5, n6 = listNum
print(n3)












