cityName = ['Moscow', 'Bishkek', 'NY', 'Tashkent', 'Almaty', 'Talas', 'NY']
del cityName[1:3]

# cityName.remove('Bishkek')
# cityName.remove('NY')

print(cityName)
#
# cityName.insert(-2, 'Tokyo')
# cityName.insert(-2, 'LA')

cityName.insert(5, 'Tokyo')
cityName.insert(5, 'LA')
print(cityName)

# cityName.clear()
# print(cityName)
#
# del cityName
# print(cityName)

workerName = ['Sergei', 'Marat', 'Olga', 'Stepan']
# deleteName = input('What name to delete? : ')
workerName.remove(input('What name to delete? : '))
print(workerName)

