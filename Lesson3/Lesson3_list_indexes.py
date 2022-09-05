#Индекс
myList = [23,5,[23,4,5,3],46,7]
print(myList[3]) #46
print(myList[2][2]) #5
# print(myList[5])

print(myList[-2]) #46
# print(myList[-8]) #Error

myList2 = [23,5,6,76,8,9,10,54,65,7]
print(myList2[2:])

myList3 = myList2[2:]
print(myList2[-4:-1])

print(myList2[::3])
print(myList2[2:7:2])

# text = 'I like icecream'
# text[2] = 'p'
myList2 = [23,5,6,76,8,9,10,54,65,7]
myList2[3] = 88
print(myList2)

myList2[2:7] = [23,4,5,6,7]
print(myList2)

myList2 = [23,5,6,76,8,9,10,54,65,7]
del myList2[-4]
print(myList2)

myList2 = [23,5,6,76,8,9,10,54,65,7]
del myList2[:4]
print(myList2)





