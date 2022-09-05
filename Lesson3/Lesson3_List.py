#Создание списка
#1 Способ
myList = []

#2 Способ
myList2 = list()

#Измерение кол-во элементов внутри списка
patientsList = ['Светалана Григорьева', 'Марат Сафин', 'Олег Тинькоф',
                ['Ребенок 1', 'Ребенок 2 Петр', 'Ребенок 3']]

print(f'Кол-во пациентов: {len(patientsList)}')
print(f'Кол-во пациентов: {len(patientsList[3])}')

print(f'Ребенок 2: {patientsList[3][1]}')

#Adding lists - Добавление к списку др списка
numbList = [12,4,54,6]
numbList2 = [3,45,6]
twoList = numbList + numbList2
print(twoList)

numbList = numbList + [23]
print(numbList)

#Дублирование списков
doubleList = numbList * 2
triple = [23,43,6,5] * 3
print(doubleList)
print(triple)

#Проверка на вхождение
print('Светалана Григорьева' in patientsList) #True
print('Канат Тимофеев' in patientsList) #False

#Проверка на не вхождение
print('Светалана Григорьева' not in patientsList) #False
print('Канат Тимофеев' not in patientsList) #True

#Макс Мин СУм
numbList = [12,4,54,6]
numbList2 = [3,45,6]

print(max(numbList))
maxunmb = max(numbList)
print(maxunmb)

print(min(numbList))
print(sum(numbList))

alphabet = ['a', 'b', 'c', 'd']
print(max(alphabet))
print(min(alphabet))

# print(sum(alphabet)) #error

alphabetNum = ['a', 'b', 45, 'c', 'd', 11]
# print(max(alphabetNum)) #error
#print(min(alphabetNum)) #error
#print(sum(alphabetNum))

#Сортировка
numbList3 = [24,54,665,21,4,645,2]
print(sorted(numbList3))
sortedNums = sorted(numbList3)
print(sortedNums)
# numbList3 = sorted(numbList3)
# print(numbList3)
numbList3.sort()
print(numbList3)

print(sorted(numbList3, reverse=True))

alList = ['t', 'a', 'e', 'r', 'c']
print(sorted(alList))
print(sorted(alList, reverse=True))

alList2 = ['t', 'a', 'e', 'r', 'c', 23,54]
# print(sorted(alList2)) #Error

numbList3 = [24,54,665,21,4,645,2]
# print(numbList3[::-1])
numbList3.reverse()
print(numbList3)

numbList1 = [2,4,5,6,67]
numbList2 = [2,4,5,8]

print(numbList2 > numbList1)

numbList3 = [24,54,665,21,4,645,2]

print(f'Среднее значение: {sum(numbList3)/len(numbList3)}')









