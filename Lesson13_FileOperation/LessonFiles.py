import os
import csv
import chardet #получить информацию о кодировке

def csvFileRead():
    # with open('username.csv', 'r') as csfFile:
    #     reader = csv.reader(csfFile)
    #     for line in reader:
    #         print(line)

    with open('username.csv', 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        encoding = result['encoding']
        print(encoding)


def tellSeek():
    with open('pythonLesson.txt') as f:
        tellMe = f.tell()
        print(tellMe)

        seekTell = f.seek(0,0)

def renameFile():
    os.rename('fileLesson.txt', 'pythonLesson.txt')

def writeToFile():
    # sFile = None
    # try:
    #     sFile = open('fileLesson.txt', 'a')
    #     try:
    #         sFile.write('Дополнительная информация')
    #         print('Записали информацию!')
    #     except BaseException:
    #         print('Не удалось записать в файл!')
    #     finally:
    #         sFile.close()
    # except BaseException:
    #     print('Не удается прочесть файл или такого файла нету')

    with open('fileLesson.txt', 'a') as f:
        # 1 sposob
        f.write('\nНовая информация2')
        # 2 sposob
        # print('\nНовая информация3', file=f)

def fileRead():
    with open('fileLesson.txt', 'r', encoding='utf-8') as f:
        #readLine считывает линию за линией
        # content = f.readline()
        # content2 = f.readline()

        # print(content)
        # print(content2)
        # print(f.readline())
        # for i in f:
        #     content = f.readline()
        #     print(content)
        # for l in f:
        #     print(l, end=' ')

        # content = f.read()
        # print(type(content))

        # contentList = f.readlines()
        # # print(contentList)
        # for i in contentList:
        #     print(i, end='')

        content = f.read()
        print(content)

if __name__ == '__main__':
    # fileRead()
    # renameFile()
    # tellSeek()
    csvFileRead()
