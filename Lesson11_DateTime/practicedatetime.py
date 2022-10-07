from datetime import *

day = input(f'Введите день: ')
month = input(f'Введите Месяц: ')
year = input(f'Введите Год: ')

result = day + '-' + month + '-' + year
resultTime = datetime.strptime(result,'%d-%m-%Y')
print(resultTime)
print(resultTime.strftime('%Y/%d/%m'))
print(f'{resultTime.day}.{resultTime.month}.{resultTime.year}')


#2-part
'''
2.Необходимо выяснить дату от сегодняшнего дня через неделю и 2 часа?
'''
f_t_day= timedelta(weeks=1, hours=2)
now= datetime.now()
after= now+f_t_day
print(after)

#""" 3.Выясните какая дата была 10 дней назад от сегодняшней даты? """
timepastdelta = timedelta(days = 10)
print(datetime.now() - timepastdelta)
