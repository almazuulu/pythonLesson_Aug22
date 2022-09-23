#Способы создания множества
#1 способ
mySet = set()
print(mySet)
print(type(mySet))

#2 способ
mySet2 = {23,43,54,1,43,54,23,13,18,18,18,18}
print(type(mySet2))
print(mySet2)

#3 способ - Ошибка - создается словарь
mySet3 = {} #Словарь!
print(type(mySet3))

#4 способ - путем конвертации из других коллекций
myList = [23,45,56,23,465,12,54,45,54,11,23,11]
mySet4 = set(myList)
print(mySet4)

word = 'kandaksndfsf kdsbfkewrwq sdas'
mySet5 = set(word)
print(mySet5)

myTuple = (23,342,12,'s', 'hello', 2, 123)
mySet6 = set(myTuple)
print(mySet6)

myList = [23,45,56,23,465,12,54,45,54,11,23,11]
myList = list(set(myList))
print(myList)

# setUnique = set(myList)
# myList = list(setUnique)
# print(myList)

myNestedList = [
    [234,54,545,23],
    [34,45,3,34,45],
    [34,54,63]
]

# myNestedList = list(set(myNestedList))
# print(myNestedList)

fSet, sSet, tSet = set(myNestedList[0]), set(myNestedList[1]), set(myNestedList[2])
print(fSet)
print(sSet)

myNestedList = [
    list(fSet), list(sSet), list(tSet)
]

print(myNestedList)

#Индексное обращение во множество дает Ошибку!
mySet2 = {23,43,54,1,43,54,23,13,18,18,18,18}

setMy = {11, 12, 45, 465, 54, 23, 56}
# print(setMy[2])
# del setMy[3]

#Измерение длины set

print(mySet2)
print(len(mySet2))

#Нахождение макс и мин и сум значения
print(max(mySet2)) #54
print(min(mySet2)) #1
print(sum(mySet2)) #152

#Проверка на вхождения in not in
print(54 in mySet2) #True
print(11 not in mySet2) #True

# mySortedSet = {1,2,2,3,4,5,5,6,7,8,9}
# print(mySortedSet)

print(sorted(mySet2))

mySortedSet = set(sorted(mySet2))
# print(type(mySortedSet))
# print(mySortedSet)

mySet2 = {1, 43, 13, 18, 54, 23}

for i in mySet2:
    print(i)

# for i in range(len(mySet2)):
#     print(mySet2[i])

setOne = {23,43,532,54}
setTwo = setOne.copy()
print(id(setOne))
print(id(setTwo))


#Удаление элементов из множетсва
setTwo.pop()
print(setTwo)
print(setOne)

# myList1 = [23,343,52]
# myList2 = myList1
#
# print(id(myList1))
# print(id(myList2))
# myList2.pop()
#
# print(myList2)
# print(myList1)

#Метод clear - вычищение элементов
setOne.clear()
print(setOne)

setMy = {11, 12, 45, 465, 54, 23, 56}
#Метод remove  - удаление элементов
setMy.remove(465)
print(setMy)

# setMy.remove(33)
# print(setMy)

#Метод discard  - удаление элементов
setMy.discard(33)
print('Hello world')

#Добавление элементов - метод add
setMy.add(33)
print(setMy)

setMy.add(53)
print(setMy)


setMy = {11, 12, 45, 465, 54, 23, 56}
setMy2 = {23,43,54,23,435}
setMy.update(setMy2)
print(setMy)

#issubset issuperset
branchhospital = {'Sergei','Elena', 'Marat'}
mainhospital = {'Sergei', 'Elena', 'Marat', 'Timur', 'Stepan', 'Oleg'}

print(branchhospital.issubset(mainhospital)) #True
print(mainhospital.issuperset(branchhospital)) #True


h1 = {'Sergei', 'David', 'Anna', 'Aisuluu', 'Aiperi','Elena', 'Marat'}
h2 = {'Sergei', 'Elena', 'Marat', 'Timur', 'Stepan', 'Oleg'}

h4 = {'Yrys', 'Tilek', 'Marat','Oleg'}
h2_list= ['Sergei', 'Elena', 'Marat', 'Timur', 'Stepan', 'Oleg']

#union - Объед колл при этом удаляя дубликаты
h3 = h1.union(h2_list)
h5 = h1.union(h2).union(h4)
print(h5)

#intersection &
h_obwiy_sotrudnik = h1.intersection(h2)
h_obwiy_sotrudnik2 = h1.intersection(h2).intersection(h4)
print(h_obwiy_sotrudnik)
print(h_obwiy_sotrudnik2)

h_obwiy_sotrudnik3 = h1 & h2
print(h_obwiy_sotrudnik3)

print('-'*20)
#intersection udate - удаляет не повторяющиеся элементы со второй коллекции
# h1.intersection_update(h2)
# print(h1)
# print(h2)

# h2.intersection_update(h1)
# print(h1)
# print(h2)

#difference = разница
h_diff = h1.difference(h2)
print(h_diff)

h_diff2 = h2.difference(h1)
print(h_diff2)


#differenc_update = разница
# h2.difference_update(h1)
# print(h1)
# print(h2)

#sym_differenc_update = сим разница
sym_diff = h1.symmetric_difference(h2)
print(sym_diff)

#frozenset = состовляет неизменяемые множества

h_frozen = frozenset({'Yrys', 'Tilek', 'Marat','Oleg', 'Oleg'})
print(type(h_frozen))
print(h_frozen)

# h_frozen.remove('Yrys')
# h_frozen.add('Askar')

#Отображение элементов ч-з
mySet = {34,54,6,76,23,5}
print(mySet)
#

# myList = [123,43,54,546,6]
# for i in range(len(myList)):
#     print(f'{i+1} -ый элемент: {myList[i]}')


# 1-sposob
counter = 1
for n in mySet:
    print(f'{counter}-ый элемент: {n}')
    counter += 1

print('-'*30)



