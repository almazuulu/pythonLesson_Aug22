#Task 1
"""
Дано натуральное число N и последовательность из N элементов. Требуется
вывести эту последовательность в обратном порядке.
Входные данные
Программа принимает на вход натуральное число N (N ≤ 103). Во второй строке
через пробел идут N целых чисел, по модулю не превосходящих 103 - элементы
последовательности.
"""

def print_reversed(n, lst):
    # for i in range(n-1, -1, -1):
    #     print(lst[i])
    # i = n - 1
    # while i > -1:
    #     print(lst[i])
    #     i-=1
    if n == 1:
        return lst[0]
    if n == 0 :
         return lst[0]
    # if len(lst) == 0:
    #     return
    print(lst[-1])
    lst.pop()

    return print_reversed(n-1, lst)

def list_sum_recursive(sList: list):
    if len(sList) == 2:
        sum1 = sList[0] + sList[1]
        return sum1
    else:
        sum2 = list_sum_recursive(sList[0:-1]) + sList[-1]
        return sum2

def flatten(lst):
    if len(lst) == 0:
        return lst
    # if type(lst[0]) == list:
    if isinstance(lst[0], list):
        return (flatten(lst[0])) + flatten(lst[1:])

    return lst[:1] + flatten(lst[1:])

if __name__ == "__main__":
    # print_reversed(5, [5, 9, 3, 2, 7])
    # lst = [5, 9, 3, 2, 7]
    # # print(lst[-1])

    print(list_sum_recursive([5, 9, 3, 2, 7]))
    print(flatten([1, [2, 3, [4]], 5]))
