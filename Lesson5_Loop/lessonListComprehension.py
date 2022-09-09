myList = []
for i in range(10,21): #10 - 19
    myList.append(i * 3)

print(myList)

print('===LH:===')
myList2 = [i * 3 for i in range(10,21)]
print(myList2)
print()
#primer 1 is slaida
lst1 = []
for i in range(10):
    lst1.append(0)

print(lst1)
print('===LH:===')
lst1_gen = [0 for i in range(10) ]
print(lst1_gen)

#primer 2 is slaida
lst2 = []
for i in range(1,15):
    lst2.append(i)
print(lst2)
print('===LH:===')
lst2_gen = [i for i in range(1,15)]
print(lst2_gen)

#primer 3 is slaida
kvList = []
for i in range(10):
    kvList.append(i**2)
kvList_gen = [i**2 for i in range(10)]
print(kvList)
print(kvList_gen)

#primer 4 is slaida
lst3_gen = [i%4 for i in range(1,21)]
print(lst3_gen)

letterList = []
word = 'Hello'
for c in word:
    letterList.append(c*2)

letterList_gen = [c*2 for c in word]

print(letterList)
print(letterList_gen)

myListNum = list(range(15,45))
print(myListNum)

evenNumsList = []
for n in myListNum:
    if n % 2 == 0:
        evenNumsList.append(n)
    else:
        evenNumsList.append('ne chet')


number = 10
result = " "
if number % 2 == 0:
    result = 'chet'
else:
    result = 'ne chet'
print(result)
print('===')

result2 = 'chet' if number % 2 == 0 else 'ne chet'
print(result2)

evenNumsList_genLst = [n if n % 2 == 0 else 'ne chet' for n in myListNum]
print(evenNumsList)
print(evenNumsList_genLst)


myListNum2 = [15, -16, 17, 18, -19, 20, 21, -22, 23, -24, 25, 26]
myListNum2_gen = [n for n in myListNum2 if n%2==0 and n>=0]
print(myListNum2_gen)


#Primer iz HW - Task1
nums = input('Введите числа, отделяя каждую из них пробелом: ').split()

print('====Home Work List====')
for n in nums:
    for j in range(int(n)):
        print('*', end=' ')
    print()

nums2 = [int(n) for n in input('Введите числа, отделяя каждую из них пробелом: ').split()]
print(nums2)

for n in nums2:
    for j in range(n):
        print('*', end=' ')
    print()

print('==== Nested Loop (Вложенные циклы) ====')

nestedList = []
for i in 'abc':
    for j in [1,2,3]:
        nestedList.append([i,j])

nestedList_gen = [[k,t] for k in 'abc' for t in [1,2,3]]

print(nestedList)
print(nestedList_gen)



