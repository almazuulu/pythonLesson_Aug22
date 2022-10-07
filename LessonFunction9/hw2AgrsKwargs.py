#Task 1

""""
Напишите функцию info_kwargs, которая принимает произвольное количество
именованных аргументов.
Функция info_kwargs должна распечатать именованные аргументы в каждой
новой строке в виде пары <Ключ> = <Значения>, причем ключи должны
следовать в алфавитном порядке. Пример работы смотрите ниже
"""

def info_kwargs(**kwargs):
    for i in sorted(kwargs.keys()):
        print(i, '=', kwargs[i])

someDict = {
    'Tilek': 'Lev Tolstoy 123',
    'Aisuluu': 'Panfilov 23',
    'Chyngyz': 'Mira 7',
    'Bolot': 'Tolstoy 55'
}

info_kwargs(first_name="John", last_name="Doe", age=33)

print('*'*20)
info_kwargs(**someDict)



#Task 2
"""
Ваша задача написать функцию format_name_list , которая принимает список
словарей, у каждого словаря в этом списке есть только ключ name .
Функция format_name_list должна вернуть строку, в которой все имена из списка
разделяются запятой кроме последних двух имен, они должны быть разделены
союзом "и". Если в списке нет ни одного имени, функция должна вернуть
пустую строку. Ниже представлены примеры:

Пример ввода:
format_name_list( [{'name': 'Bart'}, {'name': 'Lisa'},
{'name': 'Maggie'}] )

Пример вывода:
'Bart, Lisa и Maggie'
"""

def format_name_list(lst):
    text = str()
    listNames = []
    lastIndex = len(lst) - 1
    if len(lst) == 1:
        print(lst[0]['name'])
    elif len(lst) == 2:
        print(f'{lst[0]["name"]} и {lst[lastIndex]["name"]}')
    else:
        for i in range(len(lst) - 1):
            listNames.append(lst[i]['name'])
        text = ', '.join(listNames)
        text += f' и {lst[lastIndex]["name"]}'

    # str = list(l[0])
    # text = ''
    # n = len(str)
    #
    # for i in range(n):
    #     if n - i > 2:
    #         text += str[i]['name'] + ", "
    #     elif n - i == 2:
    #         text += str[i]['name'] + " и "
    #     else:
    #         text += str[i]['name']
    # return text

    # return text

spisokImen = [{'name': 'Bart'}]
spisokImen2 = [{'name': 'Bart'}, {'name': 'Lisa'},{'name': 'Maggie'}, {'name': 'David'},{'name': 'Adam'}]

print(format_name_list(spisokImen2))
# lastIndex = len(spisokImen) - 1
# print(spisokImen[lastIndex]['name'])

