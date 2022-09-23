# Отображение элементов ч-з
mySet = {34, 54, 6, 76, 23, 5}
print(mySet)

# myList = [123,43,54,546,6]
# for i in range(len(myList)):
#     print(f'{i+1} -ый элемент: {myList[i]}')

# 1-sposob perechislenie vnutri kollectcii
counter = 1
for n in mySet:
    print(f'{counter}-ый элемент: {n}')
    counter += 1

print('-' * 30)
# 2-sposob perechislenie vnutri kollectcii

for counter, n in enumerate(mySet, 1):
    print(f'{counter}-ый элемент: {n}')

myTuple = (23,43,'s',54,1, 'Hello')

for indx, el in enumerate(myTuple,100):
    print(f'Порядковый номер {el}: {indx}')




