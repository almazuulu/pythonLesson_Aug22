import calendar

c = calendar.TextCalendar(calendar.SATURDAY)
strCalendar = c.formatmonth(2022,10)
print(strCalendar)

cHtml = calendar.HTMLCalendar(calendar.SATURDAY)
hStrCalendar = cHtml.formatmonth(2022, 10)
print(hStrCalendar)

for d in cHtml.itermonthdays(2022,10):
    print(d)

nameMonths = [mn for mn in calendar.month_name if mn != '']
print(nameMonths)

nameDays = [dn for dn in calendar.day_name if dn != '']
print(nameDays)

for m in range(1, 13):
    month = calendar.monthcalendar(2022, m)
    print(month[1])


