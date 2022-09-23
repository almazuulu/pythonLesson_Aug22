#Создание функицй

def addTwoNumber(numb1, numb2):
    # addition = numb1 + numb2
    print(f'Результат: {numb1 + numb2}')


numberOne = 20
numberTwo = 55

addTwoNumber(123, 20)
addTwoNumber(50, 70)
addTwoNumber(20, 150)

print('-'*20)
addTwoNumber(numberOne, numberTwo)


# number = 123
# number2 = 20
# addition = number + number2
# print(f'Результат: {addition}')
#
# number = 50
# number2 = 70
# addition = number + number2
# print(f'Результат: {addition}')
#
# number = 20
# number2 = 150
# addition = number + number2
# print(f'Результат: {addition}')

def sayHello():
    print('Hello students!')
    print('We are learninng Python')

def playMusic():
    print('Играет музыка...')

def pauseMusic():
    print('Сейчас музыка на паузе...')


playMusic()
sayHello()
sayHello()
sayHello()

playMusic()
pauseMusic()

# print(numb1 + 10)

numb1 = 10
print(numb1)


def findSquare(n):
    print(f'Квадрат числа {n} равен : {n ** 2}')

myNum = 10
findSquare(myNum)

def findChetNumb(colls):
    print('Четные числа: ')
    for i in colls:
        if i % 2 == 0:
            print(i)

myList = [23,11,45,66,44,32,10,8]
myTuple = (43,5,6,12,76)
mySet = {43,65,3,5,11,44,88,101}
myDictOne = {'One': 1, 'Two': 2, 'Four': 4}

findChetNumb(myList)
findChetNumb(myTuple)
findChetNumb(mySet)
findChetNumb(myDictOne.values())


# # findFactorial(num)
# num = int(input('Введите число для нах-ия факториала: '))
num = 6
if num % 2 == 0:
    def findFactorial(n):
        fact =  1
        for i in range(1, n+1):
            fact *= i

        print(f'Число факториал: {fact}')
else:
    def findFactorial(n):
        print(f'Извините, для нечетных чисел вроде {n} не вычисляем факториал!')

findFactorial(num)


def findSquare(n = 4):
    print(f'Квадрат числа {n} равен : {n ** 2}')

def findSum(a = 10, b = 20):
    print(f'Сумма чисел равна: {a + b}')

findSum(23,43)
findSquare(10)

# findSum(10)
# findSquare()

# myList = list(range(6))
# print(myList)

findSquare()
findSquare(3)
findSum()
findSum(50)

def sayHello(name, cityName = 'Bishkek'):
    print(f'Hello! My name is {name} I love my city {cityName}')

sayHello('Adilet','Tashkent')

def findDifference(name,/,a,b,c):
    print(f'Меня зовут {name} и я нахожду Разницу между числами {a - b - c}')

findDifference('Timur',a = 100,b = 50, c = 20 )
findDifference('Adilet', a = 700, b = 500, c = 20)


# передача неопределенного кол-ва переменных
def findProfit(sm, *filials):
    sumFilials = 0

    for i in filials:
        sumFilials += i

    print(f'ЗП Менеджера: {sm}'
          f'\nСуммарная прибыль: {sumFilials}')

filialOne = 200
filialTwo = 250
filialThree = 310
salaryManager = 50000
findProfit(salaryManager,filialOne, filialTwo, filialThree,500,750, 1200,43,100,123)



