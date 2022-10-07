
#Practice Lesson 1

#Task 2
"""
Напишите функцию exponentiation, которая принимает на вход целое число и
выводит на экран через пробел квадрат и куб этого числа.
"""
def exponentiation(num):
    return f'{num**2} и {num**3}'

print(exponentiation(5))

#Task 3
"""
Примите от пользователя 3 числа и передайте ее в качестве параметра в функцию
calcAvg. Функция calcAvg должна найти среднее значения между переданными
3-мя числами. Посчитайте и отобразите в качестве результата среднее значение.
"""

def calcAvg(n1, n2, n3):
    return (n1 + n2 + n3)/3

print(calcAvg(23,4,53))

#Practice Lesson 2

#Task 1
"""
Давайте считать человека подростком, если его возраст находится в пределах от
12 до 17 лет. Напишите функцию is_person_teenager , которая помогает по
возрасту определить является ли человек подростком или нет.
"""

def is_person_teenager(age):
    if age > 12 and age<=17:
        return True
    return False

print(is_person_teenager(16))

#Task 2
"""
Напишите функцию generate_fizz_buzz_list , которая принимает одно целое
число n - размер списка. Функция generate_fizz_buzz_list должна
"""

def generate_fizz_buzz_list(n):
    fizzbuzz = []

    for i in range(1,n+1):
        if i % 3 ==0 and i % 5==0:
            fizzbuzz.append('fizzbuzz')
        elif i % 3 ==0:
            fizzbuzz.append('fizz')
        elif i % 5 == 0:
            fizzbuzz.append('buzz')
        else:
            fizzbuzz.append(i)

    return fizzbuzz

print(generate_fizz_buzz_list(22))

#Task 3
"""
Напишите функцию only_one_positive , которая принимает произвольное
количество числовых аргументов и возвращает True , когда из всех переданных
значений только одно положительное, в противном случае верните False
Вам необходимо написать только определение функции only_one_positive
"""

def only_one_positive(*numbs):
    count = 0
    for i in numbs:
        if i >=0:
            count += 1
    if count != 1:
        return False
    else:
        return True

print(only_one_positive(-2,-3,-1))


#Task 4

"""
Напишите функцию, в которой принимается неопределенное кол-во чисел и
найдите сумму этих всех чисел. Вам необходимо вернуть сумму из этой
функции добавить к ней любое число.
"""

def find_sum(*args):
    return sum(args)

result = find_sum(23,43,523,43453,1) + 100
print(result)