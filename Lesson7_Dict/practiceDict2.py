#Task 3
""""
В переменной country_city есть страны с их столицами.
Программе на вход будет поступать название города в переменную city . И
ваша задача найти какой стране принадлежит введенный город. Если страна
успешно найдена, необходимо вывести сообщение.

"""
country_city = {
    'Germany': 'Berlin',
    'Russia': 'Moscow',
    'Japan': 'Tokyo',
    'Kazakhstan': 'Astana',
    'Kyrgyzstan': 'Bishkek',
    'Uzbekistan': 'Tashkent'
}

cityName = input('Введите название города: ')

for country, city in country_city.items():
    if cityName != city:
        continue
    elif cityName == city:
        print(f'{cityName} находится в стране с названием {country}')
        break


