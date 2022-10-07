def findResult(n1, n2, n3):
    """
       Примите от пользователя 3 числа и передайте ее в качестве параметра в функцию
       calcAvg. Функция calcAvg должна найти среднее значения между переданными
       3-мя числами. Посчитайте и отобразите в качестве результата среднее значение.

       """
    result = 0
    try:
        result = n1/n2/n3
    except ZeroDivisionError:
        result = 'Вы пытаетесь делить на ноль'
    except TypeError:
        result = 'Вы ввели строку!'
    except BaseException as be:
        result  = f'Неизвестная ошибка {be}'
    finally:
        return result

def evenNumber(lst):
    """
    Создайте функцию в, которой в качестве параметра принимается список, из
данного списка создайте два списка. В одной из них должны хранится только
четные числа, во второй же только нечетные числа.

    """
    evenNumber = []
    try:
        # evenNumber = [n for n in lst if n % 2 == 0]
        for i in range(10):
            if lst[i] % 2 == 0:
                evenNumber.append(lst[i])
    except IndexError:
        print('Вы вышли за пределы массива')
    finally:
        return evenNumber

if __name__ == '__main__':
    print(findResult(50, 10, 'Hello'))
    print(evenNumber([23,342,23,4,11,12]))