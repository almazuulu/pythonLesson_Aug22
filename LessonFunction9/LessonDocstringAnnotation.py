print(help(max))
print(help(range))
print(help(print))

print('='*30)
print(max.__doc__)
print(print.__doc__)
print(range.__doc__)

print('='*30)
def sumTwoNums(n1, n2):
    'Функция, которая складывает два числа\n n1 - Первое число \n n2 - Второе числа'
    return n1 + n2

def sumTwoNums2(n1, n2):
   """
    Функция, которая складывает два числа
        n1 - Первое число
        n2 - Второе числа
   """
   return n1 + n2

print(help(sumTwoNums))
print('='*30)
print(sumTwoNums.__doc__)
print(sumTwoNums2.__doc__)

#Annotation
n: int = 12
n = 20
print(n + 29)

name:str = 'Askar'
numFloat:float = 23.4
numFloat = [23,4,34]

#Annotation collection
from typing import List, Set, Dict, Tuple, Union, Optional

myNumList: List[int] = [23,43,432,23]
myNumList.append('s')

myTuple: Tuple[int, int, int, int] = (23,34,12,3)
# myTuple = 's'
myTuple2: Tuple[int, ...] = (23,43,2,34,5)
myTuple2 = 23


def info(age:int, name:str) -> str:
    # print(f'Age: {age}'
    #       f'\nName: {name}')
    #
    # print(age + 20)

    info = f'Age: {age} \nName: {name}'
    # num = 23
    return info

# info('23', 'Peter') #Error
print(info(23, 'Adam'))

# print(info.__annotations__)
# num:Optional[int] = None
# num2:Optional[None] = 23
num2: int|None|str = 23
num3: Union[int, None, str] = 24

# num = 23
# num = None
# num = 'Text'
num3 = [2324,43,4]

num2 = 'Text2'
num2 = [23,31,123]

def info(age:int|str, name:str) -> str:
    print(age)
    return 's'

myList: list[str|int] = ['s', 'Name', 'Adam']
myList.append(23)
myList.append([23,43,4233])











