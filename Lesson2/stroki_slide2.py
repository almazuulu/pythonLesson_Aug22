text = 'Some text' #0 1 2 3 4 5 6 7 8
#0 1 2 3 4 5 6 7 8
#-9 -8 -7 -6..-1
print(len(text)) #len(text) - 1 = 9 - 1 = 8 - это последний индекс

print(text[1]) #o
print(text[5]) #t
# print(text[11]) - Error

print(text[6])
print(text[-3])
print(text[-1])
# print(text[-10]) -Error

text2 = "I like Python"
print(text2[2] + text2[3] + text2[4] + text2[5])

#Срезы
print(text2[2:6]) #var_name[start:end(не вход в промежуток)] like
print(text2[7:13]) #Python
# print(text2[-1:-7])

print(text2[0:7]) #I like
print(text2[:6]) #I like
print(text2[7:]) #Python

print(text2[-6:])
print(text2[:]) #= print(text2)

#reverse
print(text2[::-1])
print(text2[::2])
print(text2[::3])
print(text2[::4])

text3 = "I like Programming very much"
print(text3[2:18:2]) #lk rgamn - var_name[start:end(не вход в промежуток):step(шаг)]

print(text3[0])
# text3[0] = 'U'
print(text3)

someText = 'hello'
# someText = 'hello2'
# print(someText)

langText = 'I like PHP'
#langText = langText[:6] + " Python"
langText = langText[:2] + "don't like " + langText[7:]
print(langText)















