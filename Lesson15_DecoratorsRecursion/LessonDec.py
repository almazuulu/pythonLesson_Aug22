# def textFunction():
#     print('Результата данной функции:')
#     print('программа завершена!')
#
# def addTwoSum(a, b):
#     # textFunction()
#     print(a+b)
#
# def multiply(a, b, c):
#     print(a * b * c)
#
#
# def division(a, b):
#     textFunction()
#     print(a / b)

def bread(fun):
    def wrapper():
        print('˜˜˜˜˜˜˜˜˜˜˜˜˜')
        fun()
        print('˜˜˜˜˜˜˜˜˜˜˜˜˜')

    return wrapper

def tomato(fun):
    def wrapper():
        print('@@@@@@@@@@@@')
        fun()
        print('@@@@@@@@@@@@')

    return wrapper

def cucumber(fun):
    def wrapper():
        print('&&&&&&&&&&&')
        fun()
        print('&&&&&&&&&&&')

    return wrapper

def souce(fun):
    def wrapper():
        print('--CETCHUP--')
        fun()
        print('--CHEESE---')
    return wrapper

@cucumber
@bread
@tomato
def meat():
    print('====MEAT====')

@bread
def fish():
    print('===FISH===')

@bread
@cucumber
@souce
def chicken():
    print('===CHICKEN===')


def decoratio_with_args(fun):
    def wrapper(*args, **kwargs):
        print(f'Добро пожаловать Гость!\nПожалуйста представьтесь: ')
        fun(*args, **kwargs)

        print(f'Приятно с вами познакомиться! {args[0]} {args[1]}'
              f'\nЖелаем удачи команде {args[3]}!')

    return  wrapper

@decoratio_with_args
def showFullname(fName, sName, country, fkClub):
    print(f'Меня зовут {fName} {sName}')


if __name__ == "__main__":
    # textFunction()
    # meat()
    # print()
    # chicken()
    showFullname('Lionell', 'Messi', 'Argentina', 'PSG')

