'''
В качестве повторение пройденных материалов, предлагается выполнить данную программу.
У вас изначально есть следующий словарь ваших сотрудников:
'''
myWorkerDict = {
    "Сотрудник 1":
                    {
                        "ФИО": "Адилет Эшмаматов", 
                        "Возраст": 28,
                        "Род деятельности": "Работник цеха", 
                        "Заработная плата": 25000,
                        "ФИО Супруга/и": "Гульзада Саратова",
                        "Дети": {
                                    "Ребенок 1": "Мухаммад Эшмаматов", 
                                    "Ребенок 2": "Элиза Эшмаматова"
                                },
                        "Транспорт": "Тойота Камри 35",
                        "Адрес проживания": "г. Бишкек, ул. Лев Толстой 77"
                    },
    "Сотрудник 2":
                    {
                        "ФИО": "Эсен Урматов",
                        "Возраст": 30,
                        "Род деятельности": "Работник цеха", 
                        "Заработная плата": 31000,
                        "ФИО Супруга/и": "Тамара Тиленова",
                        "Дети": {
                                "Ребенок 1": "Усон Урматов",
                                },
                        "Транспорт": "Хонда Фит",
                        "Адрес проживания": "г. Бишкек, ул. Чуй 123"
                    },
    "Сотрудник 3":
                    {
                        "ФИО": "Аселя Давлетова",
                        "Возраст": 30,
                        "Род деятельности": "Работник бухгалтерии", 
                        "Заработная плата": 42000,
                        "ФИО Супруга/и": "Сергей Васильев",
                        "Дети": {
                                "Ребенок 1": "Елена Васильева", 
                                "Ребенок 2": "Степан Васильев", 
                                "Ребенок 3": "Марат Васильев",
                        },
                        "Транспорт": "Хонда Одиссей",
                        "Адрес проживания": "г. Бишкек, ул. Токтогула 76"
                    },
    "Сотрудник 4":
                    {
                        "ФИО": "Мария Степанова",
                        "Возраст": 29,
                        "Род деятельности": "Работник маркетинга", 
                        "Заработная плата": 35000,
                        "ФИО Супруга/и": "Олег Кичин",
                        "Дети": {
                                "Ребенок 1": "Василиса Кичина",
                            },
                        "Транспорт": "Пешком",
                        "Адрес проживания": "г. Бишкек, мкр 7 дом 76, кв: 14"
                    },
    "Сотрудник 5":
                    {
                        "ФИО": "Олег Иванов",
                        "Возраст": 45,
                        "Род деятельности": "Генеральный Директор", 
                        "Заработная плата": 70000,
                        "ФИО Супруга/и": "Светлана Валерьева",
                        "Дети": {
                                    "Ребенок 1": "Григорий Иванов", 
                                    "Ребенок 2": "Наталья Иванова", 
                                    "Ребенок 3": "Василий Иванов", 
                                    "Ребенок 4": "Филип Иванов",
                                },
                        "Транспорт": "БМВ X7",
                        "Адрес проживания": "г. Бишкек, мкр 5 дом 16, кв: 102"
                    },
}

def decor():
    ques = input('Хотите продолжить? да/нет ')
    if ques.lower() == 'да':
        functionSelection()
    else:
        print('Спасибо, что посетили наш сервис')

def select1():
    print('Вы выбрали «Поиск сотрудника»')
    name = input('Введите имя сотрудника для поиска: ')
    if name == 'нет':
        return 'Пока'
    for k in myWorkerDict.keys():
        if myWorkerDict[k]['ФИО'] == name:
            print(f'Информация касательно сотрудника - {name}:')
            for key, value in myWorkerDict[k].items():
                if isinstance(value, dict):
                    # print(key, ':', len(value))
                    for x, y in value.items():
                        print(x, y)
                else:
                    print(key, ':', value)

        elif myWorkerDict[k]['ФИО'] != name:
            print(f'Сотрудника с именем {name} - нет в нашей базе')
            print('Введите еще раз! ')
            select1()

def select2():
    print('Вы выбрали опцию «Добавление нового сотрудника»')
    try:
        name = input('Введите ФИО нового сотрудника: ')
        age = int(input('Введите возраст: '))
        work = input('Введите Род деятельности: ')
        salary = int(input('Введите Заработную плату: '))
        nameSpouse = input('Введите ФИО Супруга/и: ')
        amountChild = int(input('Введите кол-во детей: '))
        childNum = [f'Ребенок {i+1}' for i in range(amountChild)]
        nameChild = [input(f'Введите имя {i+1}-го ребенка: ') for i in range(amountChild)]
        kindTransport = input('Вид и модель транспорта:')
        address = input('Введите Адрес проживания: ')
    except BaseException:
        print('Вы ввели неправильные данные, попробуйте еще раз.')
        select2()

    myWorkerDict[f'Сотрудник {len(myWorkerDict)+1}'] = {"ФИО" : name,
                                                        'Возраст': age,
                                                        'Род деятельности': work,
                                                        'Заработная плата': salary,
                                                        'ФИО Супруга/и': nameSpouse,
                                                        'Дети': dict(zip(childNum, nameChild)),
                                                        'Транспорт': kindTransport,
                                                        'Адрес': address,
                                                        }

    print('Коллекция с работниками теперь выглядит так: \n', myWorkerDict)

def select3():
    print('Вы выбрали опцию "Удаление сотрудника".')
    try:
        name = input('Наберите имя сотрудника для удаления с коллекции: ')
        if name == 'нет':
            return 'Пока'
        else:
            for k in myWorkerDict.keys():
                if myWorkerDict[k]['ФИО'] == name:
                    myWorkerDict.pop(k)
                    print(f'Сотрудник с именем {name} был успешно удален с вашей коллекции!')
                    break

    except BaseException:
        print('Произошла какая-то ошибка, повторите еще раз')
        select3()
    finally:
        print('Коллекция с работниками теперь выглядит так: \n', myWorkerDict)

def select4():
    print('Вы выбрали: " Составить список для награждения сотрудников"')
    num = int(input('Сколько человек будут награждены?: '))
    keys = [i for i in myWorkerDict.keys()]
    listWorkers = []
    for i in range(num):
        counter = 0
        name = input(f'Пожалуйста введите имя сотрудника {i+1} для награждения: ')
        for j in keys:
            if myWorkerDict[j]['ФИО'] == name:
                listWorkers.append(myWorkerDict[j]['ФИО'])
                continue
            else:
                counter = counter + 1
        if counter >= len(keys):
            print('Нет данного сотрудника!')
            select4()

    print('Вот список сотрудников, которые будут награждены:', listWorkers, sep='\n')

def select5():
    print('Вы выбрали: "Составить список сотрудников на отпуск"')
    num = int(input('Сколько человек будут отправлены в отпуск?: '))
    keys = [i for i in myWorkerDict.keys()]
    listWorkers = []
    for i in range(num):
        counter = 0
        name = input(f'Пожалуйста введите имя сотрудника {i+1} для отпуска: ')
        for j in keys:
            if myWorkerDict[j]['ФИО'] == name:
                listWorkers.append(myWorkerDict[j]['ФИО'])
                continue
            else:
                counter = counter + 1
        if counter >= len(keys):
            print('Нет данного сотрудника!')
            select5()

    print('Вот список сотрудников, которые будут отправлены в отпуск:', listWorkers, sep='\n')

def select6():
    print('Вы выбрали: "Повышение заработной платы сотруднику"')
    name = input('Укажите имя сотрудника, которому вы собираетесь повысить заработную плату: ')
    salary = 0
    for key in myWorkerDict.keys():
        if myWorkerDict[key]['ФИО'] == name:
            salary = myWorkerDict[key]['Заработная плата']
    print(f'У сотрудника {name}, заработная плата составляет {salary} рублей.')
    money = int(input('На сколько вы хотели бы повысить З-П?:'))
    for key in myWorkerDict.keys():
        if myWorkerDict[key]['ФИО'] == name:
            myWorkerDict[key]['Заработная плата'] = myWorkerDict[key]['Заработная плата'] + money
    print(' Обновленная коллекция работников теперь выглядит следующим образом:', myWorkerDict, sep='\n')

def select7():
    print('Вы выбрали: "Понижение заработной платы сотруднику"')
    name = input('Укажите имя сотрудника, которому вы собираетесь понизить заработную плату: ')
    salary = 0
    for key in myWorkerDict.keys():
        if myWorkerDict[key]['ФИО'] == name:
            salary = myWorkerDict[key]['Заработная плата']
    print(f'У сотрудника {name}, заработная плата составляет {salary} рублей.')
    money = int(input('На сколько вы хотели бы понизить З-П?:'))
    for key in myWorkerDict.keys():
        if myWorkerDict[key]['ФИО'] == name:
            myWorkerDict[key]['Заработная плата'] = myWorkerDict[key]['Заработная плата'] - money
    print(' Обновленная коллекция работников теперь выглядит следующим образом:', myWorkerDict, sep='\n')

def select8():
    print('Вы выбрали: «Отобразить имя сотрудника, получающий максимальную З-П»')
    salary = []
    for key in myWorkerDict.keys():
        salary.append(myWorkerDict[key]['Заработная плата'])
    indexMax = salary.index(max(salary))

    name = myWorkerDict[f'Сотрудник {indexMax+1}']['ФИО']
    money = myWorkerDict[f'Сотрудник {indexMax+1}']['Заработная плата']

    print(f'Имя сотрудника получающий максимальную З-П: {name}, его заработная плата составляет: {money} рублей')

def select9():
    print('Вы выбрали: «Отобразить имя сотрудника, получающий минимальную З-П»')
    salary = []
    for key in myWorkerDict.keys():
        salary.append(myWorkerDict[key]['Заработная плата'])
    indexMax = salary.index(min(salary))

    name = myWorkerDict[f'Сотрудник {indexMax+1}']['ФИО']
    money = myWorkerDict[f'Сотрудник {indexMax+1}']['Заработная плата']

    print(f'Имя сотрудника получающий максимальную З-П: {name}, его заработная плата составляет: {money} рублей')

def select10():
    print('Вы выбрали: «Вывод среднемесячной З-П всех сотрудников»')
    count = 0
    for key in myWorkerDict.keys():
        count = myWorkerDict[key]['Заработная плата'] + count

    print(f'Среднемесячная Заработная плата составляет: {count/len(myWorkerDict.keys())} рублей.»')

def select11():
    print('Вы выбрали: «Вывод суммарной З-П всех сотрудников»')
    count = 0
    for key in myWorkerDict.keys():
        count = myWorkerDict[key]['Заработная плата'] + count

    print(f'Суммарная Заработная плата всех сотрудников составляет: {count} рублей.»')

def select12():
    print('Вы выбрали: «Виды транспорта всех сотрудников»')
    transport = []
    for key in myWorkerDict.keys():
        transport.append(myWorkerDict[key]['Транспорт'])
    transport = set(transport)
    transport = list(transport)
    for i in range(len(transport)):
        print(f'{i+1}-ый транспорт: {transport[i]}')

def select13():
    print('Вы выбрали: «Отобразить имена и кол-во детей всех сотрудников»')
    children = []
    s = []
    for key in myWorkerDict.keys():
        children.append(myWorkerDict[key]['Дети'])
    for child in children:
        for o in child.keys():
            s.append(child[o])
    print(f'Общее количество детей сотрудников составляет: {len(s)} детей')
    for i in range(len(s)):
        print(f'{i+1}-ый ребенок: {s[i]}')

def select0():
    print('Вы завершили программу. До скорой встречи!')

def functionSelection():
    print('Здравствуйте, дорогой Пользователь!\nНаберите определенную цифру из данного меню,\nчтобы получить доступ к нужному Вам функционалу!')
    print(  '1 - Поиск сотрудника',
            '2 - Добавление нового сотрудника',
            '3 - Удаление сотрудника',
            '4 - Составить список для награждения сотрудников',
            '5 - Составить список сотрудников на отпуск',
            '6 - Повышение З-П',
            '7 - Понижение З-П',
            '8 - Отобразить имя сотрудника, получающий максимальную З-П',
            '9 - Отобразить имя сотрудника, получающий минимальную З-П',
            '10 - Подсчет среднемесячной Заработной платы',
            '11 - Вывод суммарной З-П всех сотрудников',
            '12 - Виды транспорта всех сотрудников',
            '13 - Отобразить имена и кол-во детей всех сотрудников',
            '0 - Выход из Программы)', sep='\n')
    
    try:
        select = int(input('Выбор: '))
        if select > 13:
            print('Введите номер функции до 13!')
            functionSelection()
        else:
            startFunction(select)

    except ValueError:
        print('Введите числовое значение!')
        functionSelection()

def startFunction(n: str):
    if n == 0:
        return select0()

    if n == 1:
        select1()
    elif n == 2:
        select2()
    elif n == 3:
        select3()
    elif n == 4:
        select4()
    elif n == 5:
        select5()
    elif n == 6:
        select6()
    elif n == 7:
        select7()
    elif n == 8:
        select8()
    elif n == 9:
        select9()
    elif n == 10:
        select10()
    elif n == 11:
        select11()
    elif n == 12:
        select12()
    elif n == 13:
        select13()
    decor()

def main():
    functionSelection()

if __name__ == '__main__':
    main()
