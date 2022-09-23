#Task 2
"""
Создать функцию, которая принимает в качестве параметра неопределенное
количество параметров, а затем находит среднее их значение.
"""

def findavgNums(*nums):
    # print(type(nums))
    # sumNum = 0
    # for i in nums:
    #     sumNum += i
    #
    # avgNums = sumNum/len(nums)

    avgNums = sum(nums)/len(nums)

    print(f'Среднее значения: {avgNums}')

findavgNums(23,43,52,13,4)

myList = [23,4,51,23,4,51]
#Task 3
def findUnique(lst):
    lst = list(set(lst))

    print(f'Список с уникальными числами:  {lst}')

findUnique(myList)

#Task 4
"""
Создать функцию, которая принимает в себя в качестве параметра три целых
числа, функция должна вывести
"""

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

findNegativePos(-5,-1, -3)

#Task 5
"""
Создать функцию, которая принимает в качестве параметра двузначное число,
необходимо найти сумму и произведение его цифр.
"""
def nuMbers():
    a = int(input("Введите:"))

    sotka = a // 100 #2
    desyatka = a // 10 % 10 #5
    edinica = a % 10 #3

    print(sotka)
    print(desyatka)
    print(edinica)

    print("Sum:",sotka + desyatka + edinica) #7
    print("proizvedenie:",sotka * desyatka * edinica) #10


nuMbers()

#Task 1

"""
Создать функцию, которая принимает в себя в качестве параметра трехзначное
число, а затем выводит их в обратном порядке
"""

def reverseNums(a):
    sotka = a // 100  # 2
    desyatka = a // 10 % 10  # 5
    edinica = a % 10  # 3

    num = str(edinica) + str(desyatka) + str(sotka)
    num = int(num)

    print(num)

reverseNums(123)


#Task 6
""""
Переделайте эту программу в качестве функции:
Транспортная компания использует следующий тариф для расчета стоимости (в
долларах) доставки на основе веса посылки (в килограммах). В качестве
передаваемого параметра используйте вес. В качестве возвращаемого результата
вам необходимо вернуть стоимость доставки после проверки через if-else.
• Если вес находится в промежутке между 0 и 2 кг - то расчет за кг идет по
тарифу 3.5$ за кг.
• Если вес находится в промежутке между 3 и 5 кг - то расчет за кг идет по
тарифу 5.5$ за кг.
"""
def findKG(kgNum):

    if kgNum > 0 and kgNum < 2:
        print(f'Вы должны оплатить: {kgNum * 3.5}$')

    elif kgNum > 3 and kgNum < 5:
        print(f'Вы должны оплатить: {kgNum * 5.5}$')

findKG(4)

dictWorker = {
    'Oleg': 50000,
    'Nikolai':70000,
    'Murat': 60000,
    'Elena': 55000,
    'Aisuluu': 58000
}

