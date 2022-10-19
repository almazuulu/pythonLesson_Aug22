#Task 1
import random
def readLastLines():
    # num = int(input('Сколько линий хотели бы прочесть с конца? '))

    with open('someFile.txt', 'r') as f:
        lstContent = f.readlines()
        print(lstContent)
        # print(lstContent[-num:])
        # for l in f.readlines()[-num:]:
        #     print(l)

        randomLine = random.choice(lstContent)
        print(randomLine)

#Task 4
def writeWorkers():
    # arrayWorkers=input("Напишите список 10 работников: ").split()
    # num = int(input('Num workers: '))
    num = 10
    arrayWorkers = []
    # for i in range(num):
    #     arrayWorkers.append(input('Имя человека: '))

    with open("workers.txt","w")as w:
        for i in range(num):
            name = input('Имя человека: ')
            w.write(f'{name}\n')

def findLongestWord():
    with open('textFile.txt', 'r') as f:
        content = f.read()
        # maxWord = len(max(content, key = len))
        # print(maxWord)
        listWords = content.split()
        lenWord = 0
        print(listWords)

        for i in listWords:
            if len(i) > lenWord:
                lenWord = len(i)
        maxWordsList = [word for word in listWords if len(word) == lenWord]
        print(maxWordsList)



if __name__ == '__main__':
    # readLastLines()
    # writeWorkers()
    findLongestWord()