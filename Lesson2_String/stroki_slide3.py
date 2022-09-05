#upper(), lower(), isdigit(), isalpha(), strip(), just()

text = 'i love python'
print(text.upper())
text = text.upper()
print(text)

text2 = "I LOVE PYTHON"
text2 = text2.lower()
print(text2)

text3 = 'i love python'
text3 = text3.capitalize()
print(text3)

text3 = 'i love python and you also like ' \
        'python and my friend also likes python'
print(text3.count('o'))
print(text3.count('python'))
print(text3.count('pythons'))

print(text3.count('o',1,12)) #2
print(text3.find('friend'))
print(text3[46:])

print(text3.find('and',17))
print(text3[39:])

print(text3.find('z'))

# print(text3.index('z'))

text3 = text3.replace('python', 'java')
print(text3)

#isalpha = состоит ли наша строка полностью из букв
print(text3.isalpha())
text4 = 'Ilovepython'
print(text4.isalpha())
text5 = 'Ilovepython4'
print(text5.isalpha())

#isdigit = состоит ли наша строка полностью из цифр
number_text = '45'
print(number_text.isdigit()) #True
number_text2 = '45 age'
number_text3 = '-100'
print(number_text2.isdigit()) #False
print(number_text3.isdigit()) #False

helloText = 'hello'
print(helloText.rjust(7))
print(helloText.ljust(7))

print(helloText.rjust(10,'$'))
print(helloText.ljust(10,'$'))

text_spaces = '         hello          '
print(text_spaces)
# text_spaces =text_spaces.lstrip()
print(text_spaces.lstrip())
# text_spaces =text_spaces.rstrip()
print(text_spaces.rstrip())
print(text_spaces.strip())

textSome = '$$$$$$hello$$$$$'
print(textSome.lstrip('$'))
# textSome = textSome.rstrip('$')
print(textSome.rstrip('$'))
print(textSome.strip('$'))

textSome2 = '$$$$$$hello@@@@'
textSome2 = textSome2.rstrip('@')
textSome2 = textSome2.lstrip('$')
print(textSome2)

textSome3 = '$$$$$$hello@@@@'
textSome3 = textSome3.rstrip('@').lstrip('$')
print(textSome3)

name = input('Name: ').upper()
print(name)






















