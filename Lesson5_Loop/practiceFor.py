#Task 1
"""
Есть следующий список слов
[‘apple’, ‘banana’, ‘orange’, ‘pineapple’, ‘cherry’]

"""
wordsList = ['apple', 'banana', 'orange', 'pineapple', 'cherry']
for w in wordsList:
    print(w.capitalize())

#Task 2 - Изменить каждое слово на верхний регистр

for i in range(len(wordsList)):
    wordsList[i] = wordsList[i].upper()
    print(wordsList[i], end=" ")

print()
print(wordsList)

#Task 3
sumNum = 0
for i in range(5,58):
    # if i==34 or i==46 or i==52:
    #     continue

    if i in [34,46,52]:
        continue
    print(i)

    sumNum += i

    # if i!= 34 and i!= 46 and i!=52:
    #     sumNum += i
    # if i not in [34,46,52]:
    #     sumNum += i

print(sumNum)