#Task 2
"""
Ваша задача добавить в переменную cityname слово “city” и получить
результат через метод rjust.
"""
cityname = 'Bishkek'
#city
newCity = cityname.rjust(8,' ')
newCity = newCity.rjust(9,'y')
newCity = newCity.rjust(10,'t')
newCity = newCity.rjust(11,'i')
newCity = newCity.rjust(12,'c')

print(newCity)
newCity2 = 'city ' + cityname
print(newCity2)

#Task 4
text = 'I like living in Bishkek'
newText = text[7:]
print(newText)


