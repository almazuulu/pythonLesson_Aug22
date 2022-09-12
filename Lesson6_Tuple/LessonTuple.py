#Создание кортежей
myTuple = ()
print(type(myTuple))

myTuple2 = tuple()
print(type(myTuple2))

myTuple3 = 23,4,5,'Hello', 'a', 23.4, True, False
print(myTuple3)
print(type(myTuple3))

myTuple4 = tuple(range(10,41,5))
print(myTuple4)

# myTuple4[2] = 32
# print(myTuple4)
# myTuple4.pop()

myListNums = [23,454,12,54,2]
myTupleNums = tuple(myListNums)
# myTupleNums.pop()

#Создание кортежа с одним элементом
listSingle = [10]
print(type(listSingle))

tupleSingle = (23,)
print(type(tupleSingle))
print(tupleSingle)


#Операции
myTuple3 = 23,4,5,'Hello', 'a', 23.4, True, False
print(len(myTuple3))

print(myTupleNums) #(23, 454, 12, 54, 2)

print(max(myTupleNums)) #454
print(min(myTupleNums))
print(sum(myTupleNums))

#Проверка на вхождения
print(100 in myTupleNums) #False
print(100 not in myTupleNums) #True

t1 = (234,45,62)
t2 = (34,54,123)
t3 = t1 + t2
print(t3)

t4 = (23,43,13,5) * 5
print(t4)

print(t3[:3])
print(t3[:-1])
print(t3[2:4])

print(t3)

word = "I love Java"
word = word[:2] + 'like' + word[-5:]
print(word)


#Способ изменения кортежа
#1 sposob
t3 = t3[:2] + (75,) + t3[-3:]
print(t3)

#2 sposob
t3 = list(t3)
t3[2:5] = [100,125,150]
t3 = tuple(t3)
print(t3)

tupleSome = (4,45,[34,54,13,'Hello'],65,1, True)
print(len(tupleSome))
print(tupleSome[2][2]) #13

tupleSome[2][2] = 25
# tupleSome[3] = 71
print(tupleSome)

for i in t3:
    print(i)


listOne = [243,54,6,2,34]
listTwo = listOne
listTwo[1] = 75

print(listOne)
print(listTwo)

tupleOne = (243,54,6,2,34)
tupleTwo = tupleOne

print(tupleOne)
print(tupleTwo)
print(type(tupleTwo))

word = "Hello there!"







