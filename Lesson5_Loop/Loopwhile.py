# name = input('Введите имя: ')
# i = 1
# while i <= 10:
#     print(f'{i}.{name}')
#     i = i + 1

myList = list(range(10,21))
print(myList)

# i = 0
# lenList = len(myList) #11
# lastIndes = len(myList) - 1
# print(lastIndes)
# print(myList[lastIndes])
# print(lenList)

#1 - step
#1) i = 0 < 11
#2) myList[0] = 10 * 2 = 20
#3) i = i + 1 = 1

#2 - step
#1) i = 1 < 11
#2) myList[1] = 11 * 2 = 22
#3) i = i + 1 = 2

#3 - step
#1) i = 2 < 11
#2) myList[2] = 12 * 2 = 24
#3) i = i + 1 = 3

#..
#n - step
#1) i = 11 < 11 -> False
#2) myList[11] =
#
# i = 0
# lenList = len(myList) #11
#
# while i < len(myList):
#     currentNum = myList[i]
#     result = currentNum * 2
#     print(result)
#     i += 1
#
# num = int(input('Num: '))
#
# while num < 30:
#     if num % 2 == 0:
#         print(f'{num} Является четным числом!')
#     else:
#         print(f'{num} НЕ Является четным числом!')
#     num += 1

    # num = int(input('Num: '))
    #
    # if num % 2 == 0:
    #     print(f'{num} Является четным числом!')
    # else:
    #     print(f'{num} Не Является четным числом!')
    #
    #
    # # if num == 0:
    #
    # #     break
    #
    #

numList = [23,43,5,6,23,5,12,20]
print(numList)

lenList = len(numList)
i = 0

while i < lenList :
    if numList[i] %2 == 0:
        print(f'Четное число: {numList[i]}')
    else:
        print(f'НЕ Четное число: {numList[i]}')
    i += 1

i = 1

while i <= 13:
    print(i)
    i += 1

i = 13
#Task 1
while i >= 1:
    print(i)
    i -= 1














