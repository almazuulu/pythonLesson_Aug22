#Использование return

def addTwoNums(n1, n2):
    sum = n1 + n2
    sumNum1 =  n1 + 10
    return sum,sumNum1

addTwoNums(12,45)

print(type(addTwoNums(20,30)))
# result = addTwoNums(12,45) + 100
result2 = addTwoNums(12,45) * 10
print(result2)
strNumSum = str(addTwoNums(12,45))
# print(result)
# print(result2)
print(addTwoNums(23,4))
print(strNumSum)

print(max(addTwoNums(123,4)))

def findavg(lst):
    return sum(lst)/len(lst)

avgNum = findavg([23,4,454,65,34,5])
print(findavg([324,45,54,34,5]))
print(avgNum)


def get_message(text):
    if len(text) > 5:
        return
    else:
        return f'Ваш текст: {text} \n и длина вашего текста меньше 5 букв!'

    print('Test')

someText = get_message('Olaasdasda!') #+ ' and computer'

print(someText)
print(type(get_message('I love programming!')))

def findUnique(lst):
    lst = list(set(lst))
    print(f'Список с уникальными числами:  {lst}')

uniqueNums =  findUnique([23,43,23,11,43,23])

def sayHello():
    print('Hello world!')

sh = sayHello()
# sh()


def do_operation(num1, num2, funct):
    result = funct(num1,num2)  #substrion(25,5)

    print(f'Result: {result}')

def sumNums(num1, num2):
    return num1 + num2

def division(n1, n2):
    return n1 / n2

def substrion(n1,n2):
    return n1 - n2 #20

do_operation(25, 5, substrion)


#*args, *kwargs
# funcAvg(23,435,56)
def functAvgKwargs(**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    lstNums = list(kwargs.values())
    return sum(lstNums)/len(lstNums)



dictNums = {
    'One': 100,
    'Two': 200,
    'Three':300
}
print(functAvgKwargs(**dictNums))  #One = 100, Two = 200, Three = 300


def funcAvg(*args, name):
    #print(type(args))
     return args, name

print(funcAvg(23,54,6,1, name = 'Askar'))

# def sumNums2(n1, n2, n3):
#     return n1 + n2 + n3  + n5

def sumNums2(**kwargs):
    # return sum(list(kwargs.values()))
    words = ''
    for k,v in kwargs.items():
        # print(k, v)
        words += f'Имя переменной: {k} и значение {v}\n'
    return words

print(sumNums2(n2 = 12, n3 = 4, n1 = 3, n5 = 23))


