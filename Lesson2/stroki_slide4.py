# favColor = input('Ваш любимый цвет: ')
# floatNumber = float(input('Число с плав точкой: '))
# intNumb = int(input('Любое число: '))

favColor ='Green'
floatNumber = 23.4
intNumb = 33

print('Любимый цвет: '+ favColor + " \nЧисло с плавоющей точко: " + str(floatNumber)
      + "\nЛюбое число: "+ str(intNumb))

print('*'*20)
#format()

print('Любимый цвет: {0}\nЧисло с плавоющей точко: {1} '
      '\nЛюбое число: {2}'.format(favColor,floatNumber,intNumb))

print('*'*20)
print('Любимый цвет: {0}\nПовторяю его любимый цвет {0}\nЧисло с плавоющей точко: {1} '
      '\nЛюбое число: {2}'.format(favColor,floatNumber,intNumb))

print('*'*20)
print('Любимый цвет: {color}\nЧисло с плавоющей точко: {numbfloat} '
      '\nЛюбое число: {numbint}'.format(numbfloat=floatNumber,numbint=intNumb,color=favColor))

print('F строка')
#f - строки
print(f'Любимый цвет: {favColor}\nЧисло с плавоющей точкой: {floatNumber}\nЛюбое число: {intNumb}')

print(f'Любимый цвет: {favColor}\nЧисло с плавоющей точкой: {floatNumber}\nЛюбое число: {intNumb + 20}')

print('Text \t\t\tsecond text') #табуляция

print('Кафе "Фаиза"')
print("Кафе \"Фаиза\"")

#end
# print('Какой-то текст 1')
# print('Какой-то текст 2')

print('Какой-то текст 1', end=" ")
print('Какой-то текст 2', end= " ")
print('Какой-то текст 3')
print('Какой-то текст 4')

print('*' * 20)
print('Какой-то текст 1', end="$")
print('Какой-то текст 2', end= "%")
print('Какой-то текст 3')

print('*' * 20)
print('Какой-то текст 1', end="\t\t")
print('Какой-то текст 2', end= "\t\t")
print('Какой-то текст 3')

print('*' * 20)
print('Какой-то текст 1', end="\n")
print('Какой-то текст 2', end= "\n")
print('Какой-то текст 3')
