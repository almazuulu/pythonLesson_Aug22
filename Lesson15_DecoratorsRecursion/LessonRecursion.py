def factorial(n):
    factNum = 1
    for i in range(1,n+1):
        factNum*=i

    return factNum

def recursion_factorial(n):
    if n == 1:
        return n
    return n * recursion_factorial(n-1)

def findEvenNumber(n):
    if n < 2:
        return n % 2 == 0
    else:
        return findEvenNumber(n-2)

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#5! = 5*4*3*2*1
if __name__=='__main__':
    # print(factorial(1))
    # print(recursion_factorial(5))
    """"
    20 - True
    19 - False
    18 - True
    ..
    1 - False
    """
    n = int(input('Number: '))
    # if (findEvenNumber(n) == True):
    #     print('Четное число')
    # else:
    #     print('Не Четное число')

    print('Последовательность фибоначчи: ')
    for i in range(n):
        print(fibonacci(i), end=' ')

