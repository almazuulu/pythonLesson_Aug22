# sumAge = 12
def info(c1, c2, c3, name, address, age, persSpAge, someFunc):
    def sumAgeChildren(ac1, ac2, ac3):

        def multiPly(ca1, ca2):
            return ca1 * ca2

        return ac1 + ac2 + ac3 + multiPly(ac1, ac2)

    # sumAge = 15
    # print(sumAge)
    sumAge = sumAgeChildren(c1, c2, c3)

    print(f'Name: {name}'
          f'\nSum children age: {sumAge}'
          f'\nAdress: {address}'
          f'\nPerson Age: {age}'
          f'\nPerson spouce Age: {persSpAge}'
          f'\nSpouceAge: {someFunc(age,persSpAge )}')

def sumAgeSpouce(pa, psa):
    return pa + psa

personAge = 45
personSpouceAge = 43

c1, c2, c3 = 2,15,9

info(c1, c2, c3, 'Peter', 'B Street 123', personAge, personSpouceAge, sumAgeSpouce)






