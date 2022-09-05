#Task1
#Примите от пользователя любой текст или слово и отобразите ее в обратном
#направлении

print(input('Enter any text: ')[::-1])

#Task2
# Необходимо отобразить на консоли название курса с помощью среза
text = "Я обучаюсь курсу Python Django"
print(text[-13:])  #1-way
print(text[17:])  #2nd-way

#Task3
#УБрать лишние символы

#1-sposob
word1 = '$$$Python@@@'
word1 = word1.lstrip('$')
word1 = word1.rstrip('@')

print(word1)

#2 - sposob
word2 = '$$$Python@@@'
word2 = word2.lstrip('$').rstrip('@')
print(word2)

