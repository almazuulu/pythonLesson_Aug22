#Task 2
"""
Каждое 3-ее число в промежутке между 1 и 25-ти (Необходимо 25 включить в
промежуток) необходимо умножить на 5. Выполните данное упражнение с
помощью цикла while.
Пример вывода на консоли:

5 20 35 50 65 80 95 110 125
"""
count = 1
while count <= 25:
    print(count * 5, end=" ")
    count += 3

#Task3
numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1,
7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7,
1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0,
9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4,
0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9,
3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9,
1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1,
2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5,
4, 0, 9, 0]
count = 0

# while count < len(numbers):
#     if numbers[count] == 4:
#         # numbers.pop(count)
#         # del numbers[count]
#     count += 1
#
while 4 in numbers:
    numbers.remove(4)
print()
print(numbers)

#Task 4
"""
На вход программе поступает слово. Вам необходимо воспроизвести процесс, в
котором каждый раз у этого слово будет пропадать первая и последняя буква.
Этот процесс необходимо закончить, когда в слове останется только одна буква
или слово станет пустой строкой. При этом результат каждого этапа нужно
выводить

Пример:
word = “Законодательство”
Результат на консоли:
аконодательств
конодательст
онодательс
нодатель
одател
дате
ат
"""

word = "Законодательство"
# print(word[1:])
# print(word[:-1])
# print(word[1:-1])
# word = word[1:-1]
# print(word)

while len(word) > 0:
    word = word[1:-1]
    print(word)

