#Task 4

num = [123,4,45,6,7]
num2 = [23,43,54]
num.append(45)
num.append(61)

print(num)

num += [101,23] #num = num + [101,23]
print(num)

result = num + num2
print(result)

num.append([23,43])
print(num)

#Task 4 -2
numList = [21,43,54,6,76,8,34]
# numList.pop()
# numList.pop()
# del numList[-4:]
# del numList[2:5]
# print(numList)

#Task 4 -3
# numList.insert(0,65)
# numList = [65] + numList
numList.insert(3, 65)
print(numList)


#Task 5
myList = [23,43,54,65]
myList2 = myList

print(myList)
print(myList2)

myList2.remove(43)

print(myList)
print(myList2)

myList2.append(77)
print(myList)
print(myList2)

#copy() - shallow copy - поверхностное копирование

print('*'*20)
myList = [23,43,54,65]
myList3 = myList.copy()

print(myList)
print(myList3)

myList3.remove(54)

print(myList)
print(myList3)

myList.pop()

myList = [23,43,54,65,[11,9,54,23]]
myList3 = myList.copy()

# myList3[-1][1] = 13
# myList[-1][1] = 22
myList[1] = 77
print(myList)
print(myList3)

print('*'*20)

#Deepcopy - Глубокое копирование
import copy

#[23, 77, 54, 65, [11, 9, 54, 23]]
myList4 = copy.deepcopy(myList)
print(myList)
print(myList4)

myList[-1][2] = 66
print(myList)
print(myList4)

myList4[-1].append(77)
print(myList)
print(myList4)

#range() - [start, end(не входит в промежуток, step)]
listNum = list(range(1,101))
listNum2 = list(range(0,101,5))

print(listNum)
print(listNum2)







