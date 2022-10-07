#Task 1
def reverseNumber():
    """
    Создать функцию, которая принимает в себя в качестве параметра трехзначное
    число, а затем выводит их в обратном порядке
    """
    number = 0
    try:
        number = int(input('Введите число: '))
        number = str(number)
        number = int(number[::-1])

    except ValueError as ve:
        print(f'Ошибка, введите число вместо строки или символа! Вид ошибки: {ve}')
    except BaseException as be:
        print(f'Ошибка! {be}')

    finally:
        print(f'Полученный результат: {number}')

def findNegative(n1, n2, n3):
    """
    Создать функцию, которая принимает в себя в качестве параметра три целых
    числа, функция должна вывести количество положительных и количество
    отрицательных чисел.
    """
    nList = [n1, n2, n3]
    cntPos = 0
    cntNeg = 0
    try:
        for n in nList:
            if n >= 0:
                cntPos += 1
            else:
                cntNeg += 1

    except BaseException:
        print('Ошибка, попытайтесь снова!')

    finally:
        print(f'Кол-во пол-ых чисел: {cntPos}'
              f'\nКол-во отрицательных значений: {cntNeg}')


if __name__ == '__main__':
    reverseNumber()
    n1 = 21
    n2 = 'dsfsf'
    n3 = -12
    findNegative(n1, n2, n3)
