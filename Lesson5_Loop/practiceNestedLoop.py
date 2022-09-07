"""
Task 3

Напишите программу, где на вход принимается две значения a и b,
где a – это кол-во строк и b – это кол-во столбцов.
Учитывая это вы должны продолжать принимать от пользователя
числа до тех пор, пока ваша таблица не будет заполнена.
В конце вам необходимо будет вывести информацию на экране.
"""

row = int(input("Row: "))
col = int(input("Col: "))

numListNested = []

for i in range(row):
    tempList = []
    for j in range(col):
        num = int(input(f'Enter number {j+1} for {i+1} row: '))
        tempList.append(num)
    numListNested.append(tempList)

print('='*25)
print(numListNested)
for row in numListNested:
    for num in row:
        print(num, end=" ")
    print()

