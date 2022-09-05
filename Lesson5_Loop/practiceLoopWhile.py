#Task 2
"""
Отобразите сумму каждого второго числа в промежутке от 1 до 20-ти
"""
sumNum = 0
count = 1 # 3 5 7 9 .. 19

while count <= 20:
    sumNum = sumNum + count #sumNum += count
    count = count + 2 #count += 2

#Task 3
"""
Вычислите среднее арифметическое значение в промежутке между
числами 15 и 30 и отобразите на экране.
"""
sumNum2 = 0
avgNum = 0
count2 = 15
lenght = 0

# n = int(input('Num: '))
n = 30
while count2 < n:
    sumNum2 += count2
    lenght += 1
    count2 += 1

avgNum = sumNum2 / lenght
print(avgNum)

#Task 4
"""
Выведите столбец чисел от 34 до 67 с выводом только четных
чисел.
"""

count = 34
while count < 67:
    if count % 2 == 0:
        print(count)
    count += 1








