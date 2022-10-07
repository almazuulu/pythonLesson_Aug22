from typing import List, Dict

def countDuplicate(lst:list[int]) -> dict[int:int]:
    """
    Функция, которая принимает в качестве параметра список или кортеж
    и затем возвращает словарь в, которой есть информация о том, какое
    количество раз каждый элемент в списке/кортеже дублируется.

    Args:
        lst: List of int numbers

    Returns:
        Словарь с дубликатами
    """
    myDict = {}
    #1 - sposob
    for i in lst:
        if i not in myDict:
            myDict[i] = 1
        else:
            myDict[i] += 1

    #2 sposob

    myDict2 = {}

    myDict2_gen = {i:lst.count(i) for i in lst}
    for i in lst:
        myDict2[i] = lst.count(i)

    return myDict2_gen

def listVowelCond(w:str) -> list[list]:
    """
        Функция, которая принимает в качестве аргумента строку, эта
        функция должна записать все гласные буквы в отдельный один список, а
        согласные в другой. После чего вам необходимо скомбинировать эти два
        списка.
        Args:
            w: String

        Returns:
            list: Список из списка согласных и не согласных значений
        """

    commonList:List[list] = []
    vowels:str = 'aioeyu'
    vowelList:[str] = []
    condList:[str] = []

    for i in w:
        if i in vowels:
            vowelList.append(i)
        elif i in [' ', ',', '.']:
            continue
        elif i not in vowels:
            condList.append(i)

    commonList.append(vowelList)
    commonList.append(condList)

    return commonList

def findMaxMean(lst:list[list])->int:
    """
    Функция, которая принимает в качестве аргумента список из списков
    и возвращает индекс внутреннего списка у, которой самое большое среднее
    значение.

    Args:
        lst: Список из списков числовых значений
    Returns:
        int: Индекс максимального среднего значения внутреннего списка
    """
    lstAvgNum:list[int|float] = []

    for l in lst:
        avgNum = sum(l)/len(l)
        lstAvgNum.append(avgNum)

    return lstAvgNum.index(max(lstAvgNum))


if __name__ == '__main__':
    #Task 1
    print(countDuplicate([12, 3, 54, 5, 12, 3, 2, 7, 6, 3, 2]))

    #Task 2
    word = "Programming Python"
    print(listVowelCond(word))

    #Task 3
    myList = [
        [3, 4, 5, 12],
        [7, 4, 6, 2],
        [3, 2],
        [5, 6, 7, 10, 3]
    ]
    print(findMaxMean(myList))

    #Help and documentation
    print(help(countDuplicate))
    print(listVowelCond.__doc__)
    print(help(findMaxMean))
