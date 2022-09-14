#Task 1
"""
Создайте программу, в которой пользователь будет указывать размер словаря,
после чего устанавливать ключи и значения с клавиатуры, например:

# Результат выполнения программы
Количество элементов: 3
Ключ: name
Значение: John
Ключ: age
Значение: 22
Ключ: happiness
Значение: 0.98
{"name": "John", "age": "22", "happiness": "0.98"}
"""

sizeDict = int(input('Введите размер словаря: '))

myDictSome = {}

for i in range(sizeDict):
    key = input('Ключ: ')
    val = input('Значение: ')

    myDictSome[key] = val

print(myDictSome)

#Task4

dict = {}
for n in range(1,7+1):
    dict[n] = n**2
# print(dict)

dictNums = {n:n**2 for n in range(1,7+1)}

print(dict)
print(dictNums)

dictNums2 = {n:n**3 for n in range(10,21)}
print(dictNums2)


