someName = 'Adyl'


def findNegativePos(num1, num2,num3):
    listNumNeg = []
    listPos = []

    # for i in [num1, num2,num3]:
    #     if i >= 0:
    #         listPos.append(i)
    #     else:
    #         listNumNeg.append(i)

    countNeg = 0
    countPos = 0

    for i in [num1, num2, num3]:
        if i >= 0:
            countPos += 1
        else:
            countNeg += 1

    print(f'Кол-во позитивных значений: {countPos}'
          f'\nКол-во отрицательных значений:  {countNeg}')