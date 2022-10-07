import random
def choosePeople(lst:list[str]) -> list[str]:
    """
    У вас есть список из 8 людей:
    listNames = ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat' ]

    Они все желают поехать в горы.
    Вам необходимо создать программу, которая случайным образом удалит 4-х людей
    со списка, так как в легковую машину поместятся только 4 человека (не включая
    водителя).

    Пример исполнения программы:
    Полный список желающих поехать на поход:

    ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat']
    Со списка людей удалили: Elena
    Со списка людей удалили: Timur
    Со списка людей удалили: Murat
    Со списка людей удалили: Adik
    Список тех кто поедут на поход:
    ['Esen', 'Burul', 'Bermet', 'Asan']

    """
    newArr = []
    for i in range(4):
        name = random.choice(lst)
        if len(newArr) <4 and name not in newArr:
            newArr.append(name)
        else:
            continue

    return newArr

def makeListPeople(randomNum: int) -> list[str]:
    """
    Создайте программу, которая составляет список людей со случайной длиной в
    промежутке от 1-го до 15-ти
    """
    newArr = []
    print(f'Случайная длина для вашего списка людей {num}: ')

    for i in range(num):
        nameToAdd = input(f'Введите имя для {i+1} человека: ')
        newArr.append(nameToAdd)

    return newArr

if __name__=='__main__':
    listNames = ['Esen', 'Timur', 'Burul', 'Adik', 'Bermet', 'Asan', 'Elena', 'Murat']
    # print(choosePeople(listNames))
    num = random.randint(1,15)
    print(f'Случайный список из {num} людей: {makeListPeople(num)}')
