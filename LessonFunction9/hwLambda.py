# Task 2
"""
Функция, которая находит сумму двухзначного числа:
"""
def findSum(numb1):
    num1 = numb1 // 10
    num2 = numb1 % 10
    result = num1 + num2
    return result

#   return (numb1 // 10) + (numb1 % 10)
#
findSum2 = lambda numb1: (numb1 // 10) + (numb1 % 10)

print(findSum(25))
print(findSum2(25))

# Task 4
"""
Функция, которая находит среднее значение элементов от списка:
"""

def findAvg(lst):
    avgNum = sum(lst) / len(lst)
    return avgNum


findAvg2 = lambda lst: sum(lst) / len(lst)

print(findAvg([23, 4, 5, 2]))
print(findAvg2([23, 4, 5, 2]))

# Task 6
"""
Создайте программу, которая проверяет делятся ли два числа без остатка. Для
того, чтобы проверить на делимость используйте лямбду выражения с
проверкой результата с помощью if-else конструкции.
"""


def checkNum(n1, n2):
    # if n1 % n2 == 0:
    #     return 'Делится без остатка'
    # else:
    #     return 'Не делится без остатка'

    if n1 % n2:
        return 'Не делится без остатка'
    else:
        return 'Делится без остатка'

checkNum2 = lambda n1, n2: 'Не делится без остатка' if n1 % n2 else 'Делится без остатка'

print(checkNum(45, 5))
print(checkNum2(22, 5))
