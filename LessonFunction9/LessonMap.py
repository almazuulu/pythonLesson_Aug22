myList = [23,4,453,45, 6, 8]
#
def checkEven(lst):
    tempList = []
    for i in lst:
        if i % 2 ==0:
            tempList.append(i)
        else:
            tempList.append(False)
    return tempList
#
# print(checkEven(myList))

def checkEvenNum(n):
    if n % 2 == 0:
        return n
    else:
        return False

myList2 = list(map(checkEvenNum,myList))
print(myList2)

print(checkEvenNum(5))

myNums = [1,4,5,6,7,5]

def oper(lst):
    temp = []
    for i in lst:
        temp.append(i * 2 + 100)

    return temp

print(oper(myNums))

myNums2 = list(map(lambda n:n*2 + 100, myNums))

print(myNums2)
def someFunct(collection, option):
    if option == 1:
        return list(map(lambda n: n*3, collection))

    elif option == 2:
        return tuple(map(lambda n: n**2, collection))

myNums = [1,4,5,6,7,5]

cubeNum = someFunct(myNums, 2)
print(cubeNum)

listSome = ['2', '34', '5', 'some']

def checkNum(x):
    if x.isdigit():
        return int(x)
    else:
        return x

listSome2 = list(map(checkNum, listSome))
print(listSome2)








