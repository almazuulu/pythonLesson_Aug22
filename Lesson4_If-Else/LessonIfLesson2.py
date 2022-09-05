

#split() -> from string -> list
text = "Python, Java, C++, C#, JS, PHP"
langList = text.split(",")
print(langList)

#join() from list -> string
textLang = ",".join(langList)
print(textLang)
print(type(textLang))


#Primer 1
# cities = input('Введите города в, которых вы были отделяя пробелом: ').split()
#
# count = len(cities)
# if count >= 4:
#     print(f'Да вы путещественник! Вы были аж в {count} городах!')
# else:
#     print(f'{count} тоже хороший результат, еще вся жизнь впереди!')

#Моржовый оператор

# if (count:=len(cities)) >= 4:
#     print(f'Да вы путещественник! Вы были аж в {count} городах!')
# else:
#     print(f'{count} тоже хороший результат, еще вся жизнь впереди!')

if (num := int(input('Num: '))) %2 == 0:
    print(f'Четное число {num}')
else:
    print(f'{num} Не четное значение!')

#Switch -  Case

weekday = int(input('Which day?: '))

if weekday == 1:
    print('Monday')
elif weekday == 2:
    print('Tuesday')
elif weekday == 3:
    print('Wednesday')
#...
else:
    print('I don\'t know that day!')


#math -case

print('*'*20)
print('Match - Case: ')

match weekday:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 5|6|7:
        print('Weekends')
    # ...
    case _:
        print('I don\'t know that day!')


typeName = 34

match typeName:
    case int():
        print('Integer type')
    case float():
        print('Float type')

num1 = int(input('Num1 :'))
num2 = int(input('Num2 :'))
num3 = int(input('Num3 :'))

