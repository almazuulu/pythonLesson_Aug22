#Task1
""""
Написать программу для конвертации кортежа в string
"""

myTuple = (23,45,4,1,"Hello")
# myTuple = [str(i) for i in myTuple]
# myTuple = tuple(myTuple)

# word = str(myTuple)
# word = " "

# for i in myTuple:
#     word+= str(i)
#     word+=" "

# word = " ".join(myTuple)
# print(word)

word = str(myTuple)
word = word.lstrip('(').rstrip(')')
print(word)

#Task 2
""""
каждый второй элемент кортежа, начиная с третьего.
"""
tup = (3.4, 56, "Some", "Hi", 7, 3.8, 44)
print(tup[2::2])

#Task4

myTuple = (23,55,43.3, 'Hello')

i = 0
while i < len(myTuple):
    print(myTuple[i], end=" ")
    i += 1


