#Добавление элементов в список
myList = [34,5,54,6,67,7]
myList.append(23)
myList.append('Altyn')
myList.append(['a', 'Hello', True, 23.4])

print(myList) #[34, 5, 54, 6, 67, 7, 23, 'Altyn', ['a', 'Hello', True, 23.4]]

myList2 = [34,5,54,6,67,7]
myList2.insert(2,11)
myList2.insert(5,'Aiperi')
print(myList2)

#Удаление элементов из списка
myList3 = [34,5,54,6,67,7]
del myList3[-2]
print(myList3)

myList3 = [34,5,67,67,54,6,67,7]
myList3.remove(67)
print(myList3)

# del myList3
# print(myList3)

myList3.clear()
print(myList3)

myList4 = [34,5,67,67,54,6,67,7]
myList4.pop()
myList4.pop(1)
# print(myList4)

myList5 = [34,5,67,67,54,6,67,7]
lastElement = myList5.pop()
print(lastElement)
print(myList5)

#Нахождение дублирующих элементов
print(myList5.count(67)) #3





