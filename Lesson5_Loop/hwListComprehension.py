#Task1
""""
Необходимо сгенерировать список, возведенных вквадрат в
промежутке между 1 и 10
"""
myList = [i ** 2 for i in range(10,21)]

myList2 = []
for i in range(10,21):
    myList2.append(i**2)

print(myList)
print(myList2)

#Task 2
"""
Есть текст со словом “I love programming so much and I would like to
improve my skills”, вам необходимо из части этого текста
сгенерировать список с буквами следующего вида:
['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'r', 'o', 'g', 'r',
'a', 'm', 'm', 'i', 'n', 'g']
"""

text = "I love programming so much and I would like to improve my skills"
# print(text[:18])
letterList = [l for l in text[:18]]
print(letterList)

#Task 3
"""
Примите от пользователя любое слово и сгенерируйте новый
список, состоящий только из согласных букв принятого от
пользователя слова.
"""

# glasnye = "aiyoeu"
charList = [c for c in input('Введите текст: ') if c not in "aiyoeu"]
print(charList)

charList2 = []
for c in input('Введите текст: '):
    if c not in "aiyoeu":
        charList2.append(c)

print(charList2)

#Task 4
# if 21 % 2==0:
#     print(True)
# else:
#     print(False)

l1 = [2,3,4,5]
l2 = [20,41,28,56]

lst = [True if j % i == 0 else False for i in l1 for j in l2]
print(lst)








