weather = input('Which weather is outside?: ')

if weather == 'Its raining':
    print('I am going to street with umbrella')
else:
    print('I am not going to take umbrella')


age = int(input('What age? :'))

if age >=25 and age<=40 and age==20 and age == 17: #False and True - > False
    print('наняты на работу')
else:
    print('НЕ наняты на работу')

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))


if num1 == num2:
    num1 += 10 #num1 = num1 + 10
    num2 += 10
elif num1 > num2:
    num1 = num1 - num2
    num2 -= 5
elif num2 > num1:
    num2 = num2 - num1
    num1 -= 5
else:
    num1 *= 2
    num2 *= 2

print(num1)
print(num2)

age  = int(input('Какой ваш возраст?: '))

if age >= 18:
    if age == 18:
        print('Вам полагается подарок!')
    elif age >= 70:
        print('Вы можете голосовать из дома!')
    print('Вы можете голосовать!')
elif age <=17:
    pass
elif age <=15:
    pass

elif age <=13:
    pass

else:
    print('Ваш возраст не подходит!')

name = 'Askar'
# result = ''

if len(name) == 5:
    result = 'Длина имени 5 букв'
else:
    result = 'Длина имени более 5 букв'

result = 'Длина имени 5 букв' if len(name) == 5 else 'Длина имени более 5 букв'
print(result)

num1 = int(input('..'))
num2 = int(input('..'))


