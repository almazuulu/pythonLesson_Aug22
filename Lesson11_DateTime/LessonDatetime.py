from datetime import *
import pytz
import datetime
# from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

todayDate = datetime.date.today()
# todayDate = date.today()
print(todayDate)

indDayKg = datetime.date(2023, 8, 31)
print(indDayKg)

print(f'День независимости день: {indDayKg.day}, месяц: {indDayKg.month}, год:  {indDayKg.year}')
print(f'{indDayKg.day}/{indDayKg.month}/{indDayKg.year}')

# motherBirthday = datetime(1970, 5, 1, 5, 45, 15)
motherBirthday = datetime.datetime(1970, 5, 1, 5, 45, 15)
print(motherBirthday.weekday()) # День недели
print(motherBirthday.hour)
print(motherBirthday.minute)

now = datetime.datetime.now()

textData = '2022-25-03'
textData2 = '25/03/22'

print(datetime.datetime.strptime(textData,'%Y-%d-%m'))
somedate = datetime.datetime.strptime(textData2,'%d/%m/%y')
print(somedate)

print(f'Текущяя дата и время: {now.strftime("%d/%m/%Y - %H:%M (%B - %a)")}')

timeDelta = datetime.timedelta(days=10)

timeDelta2 = datetime.timedelta(days=10, hours=2, minutes=30)
dayAfterTenDays = now + timeDelta
dayAfterTenDays2 = now + timeDelta2
print(f'Дата и время через 10 дней: {dayAfterTenDays.strftime("%d/%m/%Y - %H:%M (%B - %A)")}')
print(f'Дата и время через 10 дней 2 часа: {dayAfterTenDays2.strftime("%d/%m/%Y - %H:%M (%B - %a)")}')

deadline = datetime.datetime(2022, 10, 23, 14, 0)
daysLeft = deadline - now

nowBishkek = datetime.datetime.now(pytz.timezone('Asia/Tbilisi'))
print(nowBishkek)
