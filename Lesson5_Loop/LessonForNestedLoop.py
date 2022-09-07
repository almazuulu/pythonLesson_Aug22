for i in range(3): #0..2 - 3 raza
    for j in range(5): #0..4 - 5 raz
        print('$', end=" ")
    print()

print('='*25)

for i in range(3): #0..2 - 3 raza
    for j in range(5): #0..4 - 5 raz
        print(f'{i}', end=" ")
    print()

print('='*25)

for i in range(3): #0..2 - 3 raza
    for j in range(5): #0..4 - 5 raz
        print(f'{j}', end=" ")
    print()

print('='*25)
for i in range(3): #0,1,2 - 3 raza
    for j in range(5): #0,1,2,3,4 - 5 raz
        print(f'{i*j}', end=" ")
    print()

print('='*25)
for i in range(5): #0,1,2,3,4 - 5 ryadow
    for j in range(i): #for j in range(4) 0..3
        print(f'{j}', end=" ")
    print()

print('='*25)
myListNum = [
    [12,4,54,6,2],
    [2,43,5,2],
    [23,4,5],
    [23,54,6,76,3]
]

for row in myListNum:
    for n in row:
        print(n, end=" ")
    print()

print()
for row in myListNum:
    for n in row:
        if n==23:
            break
        elif n%2 == 0:
            print('Ч', end=" ")
        else:
            print('НЧ', end=" ")
    print()
