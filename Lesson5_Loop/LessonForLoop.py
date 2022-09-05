myList = list(range(15,31))
print(myList)

myList2 = list(range(10)) #0...9
print(myList2)

#0 1 2 3
i = 0
while i < 4:
    print(i)
    i += 1

for j in range(4):
    print(j)

numList = []
#Получить все числа, кот деляться только на 5 в пром от 5 до 100
for i in range(5,101):
    if i % 5 == 0:
        numList.append(i)

print(numList)

cnt = 15
sumNum2 = 0
lenght2 = 0
while cnt < 30:
    lenght2 += 1
    sumNum2 += cnt
    cnt += 1
print(sumNum2/lenght2)


sumNum = 0
lenght = 0
for i in range(15,30):
    sumNum += i
    lenght += 1

print(sumNum / lenght)

#5! = 5 * 4 * 3 * 2 * 1 =  120
#6! = 6 * 5 * 4 .. 1 * 0=  720
n = int(input('Num to find factorial: '))
factorial = 1

for cur in range(1,n+1):
    factorial *= cur #factorial = factorial * i

print(factorial)

word= "Welcome"
for i in word:
    if i!='l':
        print(i)

j = 0
while j < len(word):
    if word[j]!='l':
        print(word[j])
    j += 1


myList3 = list(range(10,30,2))
print(myList3)

for i in myList3:
        print(i*2, end=" ")

# print(myList3)

# for i in range(len(myList3)): #range(9) 0,1,2,3,4...8
#     myList3[i] *= 2 #myList3[i] = myList3[i] * 2 #1 = myList3[1] = 12 * 2
#
# print(myList3)







