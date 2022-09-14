#Создание словарей
#1 способ
myDict = {}
print(type(myDict))
print(myDict)

#2 способ
myDict2 = dict()

# 3способ
listWorkers =[
    ['Askar Adylov', 'Lev Tolstoy 12'],
    ['Marat Nurmatov', 'Panfilov 12'],
    ['Elena Timoshing', 'Bokonbaeva 23'],
]

tupleWorkers = (
    ('Askar Adylov', 'Lev Tolstoy 12'),
    ('Marat Nurmatov', 'Panfilov 12'),
    ('Elena Timoshing', 'Bokonbaeva 23'),
)

#3 Способ
dictWorker = dict(listWorkers)
print(dictWorker)
print(type(dictWorker))

dictWorker2 = dict(tupleWorkers)
print(dictWorker2)
print(type(dictWorker2))

#4 способ
listCities = ['Bishkek', 'Osh', 'JA', 'Talas', 'IK', 'Naryn', 'Batken']
codesCities = ["0312", "03222", "3227", "03244", "03255", "03655", "03257"]

dictCitiesCodes = dict(zip(listCities, codesCities))
print(dictCitiesCodes)
print(type(dictCitiesCodes))

#Создание словарей со значениями
contacts = {
    "Tilek-buhgalter": "+996509123243",
    "Akmat": "+7232132312312",
    "Ainura kollega": "+11232321321312",
    "Papa": "+9965551232131",
    "Mama": "+996772435465",
    "Kanat santehnik": "+996500213435"
}

print(contacts["Papa"])
print(contacts["Mama"])

#Добавить новые элементы
contacts["Murat odnokl"] = "+996700345678"
contacts["Tamara"] = "+721132131234"
print(contacts)

print(contacts["Tamara"])

#Удаление элементов
#1 sposob
del contacts["Ainura kollega"]
print(contacts)

#2 sposob
contacts.pop("Akmat")
print(contacts)

#3 способ
contacts.clear()

#4 способ
# del contacts


# del contacts["Samat"]
# contacts.pop("Samat", "Неизвестный контакт")
# print("Hello world")

#Проверка на вхождения
print("Tamara" in contacts) #True
print("Samat" not in contacts) #True

print('+721132131234' in contacts)


#Конвертация из словарей в список
contacts = {'Tilek-buhgalter': '+996509123243',
            'Papa': '+9965551232131', 'Mama': '+996772435465',
            'Kanat santehnik': '+996500213435',
            'Murat odnokl': '+996700345678', 'Tamara': '+721132131234'}

listNames = list(contacts)
print(listNames)


contacts2 = {'Tilek-buhgalter': '+996509123243',
             'Mama': '+996772435465',
            'Murat odnokl': '+996700345678', 'Papa': '+9965551232131',
             'Tamara': '+721132131234',
             'Kanat santehnik': '+996500213435',
             }

print(contacts == contacts2)

#Изменение данных словаря
contacts['Tamara'] = "+99650021312433"
print(contacts)


#Ключи - они уникальные, а значения разными, одинкаовыми

contacts = {'Tilek-buhgalter': '+996509123243',
            'Papa': '+9965551232131', 'Mama': '+996772435465',
            'Kanat santehnik': '+996500213435',
            'Murat odnokl': '+996700345678', 'Tamara': '+721132131234',
            'Papa2': '+9965551232131'}

print(contacts)

print(contacts.get("Murat odnokl"))
print(contacts.get("Samat", 'Неизвестный пользователь'))


# contacts.clear()
# del contacts
print(contacts)

contacts2 = {'Uson': '+9965034223424', 'Esen': '+9974343243243', 'Masha': '+78343424324324'}
contacts.update(contacts2)
print(contacts)

contacts3 = contacts.copy()
print(contacts3)

#Можно использовать tuple в качестве ключа


contacts = {'Tilek-buhgalter': '+996509123243',
            'Papa': '+9965551232131', 'Mama': '+996772435465',
            'Kanat santehnik': '+996500213435',
            ('Student1', 'Student2', 'Student3'): '+996509314567',
            'Murat odnokl': '+996700345678', 'Tamara': '+721132131234',
            'Papa2': '+9965551232131'}

print(contacts[('Student1', 'Student2', 'Student3')])
# print(contacts[['Adma', 'Peter','Oleg']]) #Error

#Перебор словаря
print(contacts.keys()) #Получение ключей
print(contacts.values()) #Получение значений
print(contacts.items()) #Получение значений


# Отображение всех ключей с пом цикла for
for name in contacts.keys():
    print(f'Имя: {name}')

print('-'*20)
# Отображение всех значений с пом цикла for
for telnum in contacts.values():
    print(f'Телефон: {telnum}')

print('-'*20)
# Отображение всех данных (ключ и значений) с пом цикла for
for name, telnum in contacts.items():
    print(f'Имя чел-ка: {name}, его телефон: {telnum}')

#Комплексный словарь - nested
personInfo = {
    'Oleg Tinkof':{
        'company name': 'Tinkoff',
        'age': 43,
        'country': 'Russia',
        'children number': 3
    },

    'Elon Mask':{
        'company name': 'Tesla',
        'age': 51,
        'country': 'USA',
        'children number': 5
    },

    'Jordan Belfort':{
        'company name': 'NY Birzha',
        'age': 48,
        'country': 'USA',
        'children number': 5
    },

    'Bill Gates':{
        'company name': 'Microsoft',
        'age': 63,
        'country': 'Canada',
        'children number': 5,
        'children names': ['Alfred Gates', 'Mary Gates', 'Adam Gates']
    }
}

listSome = [23,43,[34453,545,546],54]
print(listSome[2][1])
print(personInfo["Jordan Belfort"] ["company name"])
print(personInfo["Bill Gates"]["children names"][1])

#Измерение длины
print(len(contacts))
print(len(personInfo))

numbers = {1: "One", 2:'Two'}


dictNumbers = {}

for i in range(7):
    pass
    #code




