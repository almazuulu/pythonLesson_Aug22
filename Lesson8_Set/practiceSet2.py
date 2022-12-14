#Task 3
"""
3) Вашей программе будут поступать на вход N списков, содержащих целые числа
Для каждого введенного списка определите, сколько в нем встречается различных чисел.
Входные данные
Сперва поступает натуральное число N - количество списков
В следующих N строк вводятся значения каждого списка, разделенные через пробел
Выходные данные
Вывести на отдельной строке количество различных чисел каждого введенного списка в том же порядке, в котором вводились списки

Пример ввода:

5
1, 23, 45
1 2 3, 23,16
1 2 3 4 4 4 3 4 1 2
123 1000 800 123
98 832 32 4 343 242 42 432

Пример вывода:

1
3
4
3
8
"""
num = int(input("Введите количество списков: "))

commonList = []
for i in range(num):
    tempList = [int(n) for n in input('Введите числа отделяя каждую запятым: ').split()]
    commonList.append(tempList)

print('-'*20)
for lst in commonList:
    print(f'Кол-во уникальных элементов: {len(set(lst))}')

