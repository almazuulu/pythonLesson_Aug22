currency = {
    "рубль": 1.5,
    "доллар": 85,
    "евро": 92,
    "тенге": 0.72,
    "сум": 0.0074
}

dengi = int(input('Введите сумму для конвертации: '))
print()
for i,v in currency.items():
    print(f'{dengi} {i} в сомах будет: {v * dengi} сомов')

country_city = {
    'Russia': 'Moscow',
    'USA': 'Washington',
    'England': 'London',
    'Germany': 'Berlin',
    'Japan': 'Tokyo',
    'China': 'Beijing',
    'India': 'Deli'
}

city = input('Введите название города: ')
for k, v in country_city.items():
    if city in v:
        print(f'{city} находится в стране с названием {k}')
        break
    elif city not in v:
        print(f'{city} извините этого города в нашем списке нет')
        break
