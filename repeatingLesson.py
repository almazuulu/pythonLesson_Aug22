#Task 4
#Find factorial
num = int(input('Напишите число для нахождения факториала: '))

#Factoial
# 5! = 5*4*3*2*1 = 120
# 4! = 4*3*2*1 = 24

fact = 1
for i in range(1, num + 1):
    fact = fact * i
    
print(fact)

#Task 5
name = input('Введите ваше имя: ')
age = int(input('Введите свой возраст: '))
adres = input('Введите свой адрес: ')

# info = {
#     'Имя': name,
#     'Возраст': age,
#     'Адресс': adres
# }

# info = {}
# info['Имя'] = name
# info['Возраст'] = age
# info['Адрес'] = adres
# print(info)