text = "some text"
text2 = 'some text'

print(text)
print(text2)

poem = "Белеет парус одинокой \nВ тумане моря голубом!..\nЧто ищет он в стране далекой? \nЧто кинул он в краю родном?.."
print(poem)
print()
poem2 = '''
    Белеет парус одинокой
    В тумане моря голубом!..
    Что ищет он в стране далекой?
    Что кинул он в краю родном?..
    
    Играют волны — ветер свищет,
И мачта гнется и скрыпит…
    Увы! он счастия не ищет
    И не от счастия бежит!
    
    Под ним струя светлей лазури,
    Над ним луч солнца золотой…
    А он, мятежный, просит бури,
    Как будто в бурях есть покой!
'''

print(poem2)
print('*'*20)
number = 0
someString = ''
someString2 = ""
someString3 = " "
someString+= "Hello there"
someString+=" my friend"
print(someString)

# s = 'Hello' * 100
# print(s)

#len() - измеряет длину
helloText = "Hello World my friend!"
print(len(helloText))

lengthText = len(helloText)
print(lengthText + 10)

print(type(lengthText))

#Проверка на вхождения
print("World" in helloText ) #True
print("Worlds" in helloText ) #False
print("l" in helloText)
print("!" in helloText)

#Проверка на не вхождения
print('*' * 20)
print("World" not in helloText ) #False
print("Worlds" not in helloText ) #True
print("l" not in helloText) #False
print("!" not in helloText) #False
print("Peace" not in helloText) #True

#срвнение
print('*' * 20)
a = 'a'
a2 = 'A'

name = 'Adilet'
name2 = 'adilet'

b = 'b'
c = 'c'

print(a > a2)#True
print(name < name2)#True

print(a < b) #True
print(b < c) #True



