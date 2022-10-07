# import random
# from random import random, randint, randrange, shuffle, choice
from random import *
import math

# from math import *
n = random() # 0.0 .. 1.0 пример: 0.5347955167268388
print(n)

# n2 = random.random() * 100 # Рандомные значения от 0 ... 99 пример: 27.571352336670905
# print(n2)

n2 = random() * 100 # Рандомные значения от 0 ... 99 пример: 27.571352336670905
print(n2)

# n_int_rand = random.randint(20, 500) #Число в пром - ке от 20 до 200,  пример: 188
# print(n_int_rand)

n_int_rand = randint(20, 500) #Число в пром - ке от 20 до 200,  пример: 188
print(n_int_rand)

n_int_randrange = randrange(100, 1000, 2)

print(n_int_randrange)
#
lst = list(range(1,11))
print(lst)

lstShuffled = lst.copy()
shuffle(lstShuffled)
print(lstShuffled)

list_doctors = ['Sergei', 'Oleg','Nikita', 'Murat', 'Adyl', 'Aisuulu', 'Olga']
name_doct =  choice(list_doctors)

print(name_doct)

########### Module Math ###################
print(math.pow(12,2))
print(math.sqrt(144))

num = 12.2575 #13
print(math.ceil(num))
print(math.floor(num))
print(math.factorial(5))

print(math.cos(math.radians(360)))
print(math.sin(math.radians(180)))

print(math.log(8,2)) #3
print(math.log(144,12)) #2
print(math.log10(1000)) #3

print(math.pi)

num = 12.3575 #13
print(round(num))

#Число по модулю
print(math.fmod(10,3))
print(math.e)













