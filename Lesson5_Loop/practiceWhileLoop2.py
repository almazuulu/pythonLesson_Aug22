#Task1
names = ['Sergei', 'Valeriy', 'Elena', 'Marat', 'Stepan', 'Uson']

#Task2
nums = [23,45,4,5,12,4,5, 7, 15, 21, 78, 41]

#Task3
words = ['Hello', 'There', 'World', 'Bishkek', 'Tokyo', 'Almaty']

cnt = 0
while cnt < len(words):
    tempWord = words[cnt]
    if 'o' in tempWord:
        words.remove(tempWord)
    cnt += 1

print(words)

