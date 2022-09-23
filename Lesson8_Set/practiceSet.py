#Task 1
"""
Добавьте в заданное множество, заданный список:
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
"""
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

commonSet = sampleSet.union(sampleList)
# commonSet2 = sampleSet | sampleList
print(commonSet)
# print(commonSet2)

#Task 2
"""
Необходимо вернуть схожий результат взятый из двух разных множеств:
Пример:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.intersection(set2)
print(set3)

set3_1 = set1 & set2
print(set3_1)

#Task 3
"""
Даны два множества, необходимо обновить первое множество с элементами,
которые есть только в первом элементе, но нету во втором элементе.
Пример:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
"""
set1 = {10, 20, 30}
set2 = {20, 40, 50}

setCommons = set1.difference(set2)
setCommons2 = set1 - set2
print(setCommons)
print(setCommons2)


#Task 4
"""
Создайте множество из двух элементов: 1 и 3. Выполните действия:
• добавьте один новый элемент;
• добавьте сразу несколько элементов в множество;
• добавьте список и еще одно множество в ваше изначально созданное
множество.
"""

mySet = {1,3}

#Task 4-1
mySet.add(5)

#Task 4-2
mySet.update([23,4,54])
print(mySet)

n = int(input('Введите кол-во элементов: '))
for i in range(n):
    num = int(input('Введите число: '))
    mySet.add(num)

print(mySet)

#Task 5
mySetOne = {12,4,54,11,9}
mySetFrozen = frozenset({10,45,154,10})

myNewSet = mySetOne.union(mySetFrozen)
print(myNewSet)

myNewSet.update((99,98))
print(myNewSet)

myNewSet = list(myNewSet)
myNewSet.pop(0)
myNewSet = set(myNewSet)
print(myNewSet)


# word = 'asdasdas'
# print(len(word))
# words = ['bishkek', 'school', 'father', 'mother']
# for w in words:
#     if len(w) > 6:
#         print(w)

# word = ['hhsads']
#
# for i in myNewSet:
#     print(i)





