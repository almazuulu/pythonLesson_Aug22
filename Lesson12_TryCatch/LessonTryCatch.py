result = 0
n1 = 0
n2 = 0
myList = [23,34,123,43,5]
try:
    n1 = int(input('Num1 :'))
    n2 = int(input('Num2 :'))

    if n2 > n1:
        raise Exception('Второе число не может быть больше чем первое!')
    result = n1 - n2
    # print(myList[8])

except ZeroDivisionError as zerdiv:
    print(f'Вы попытались делить ноль! А конкретно ошибка называется {zerdiv}')
    result = n1 / 2
except (ValueError, IndexError):
    print(f'Введите не строки! А число! ИЛИ Вы пытаетесь обратится к не сущ-му индексу!')
    result = n1 / 10
except Exception as e:
    print(f'Предупреждение! {e}')
    n1 = int(input('Num1 :'))
    n2 = int(input('Num2 :'))
except BaseException:
    print(f'Неизвестный тип ошибки!')
finally :
    print(f'Результат деления: {result}')
    result = n1 - n2

print('Продолжение программы ...')
print(n1 * n2)

# myList = [213,43,433,4]
# print(myList[5])
