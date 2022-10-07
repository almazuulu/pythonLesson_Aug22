#Task 1
def writeLorem():
    content = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
Ipsum has been the industry's standard dummy text ever since the 1500s, when an
unknown printer took a galley of type and scrambled it to make a type specimen
book. It has survived not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised in the 1960s with
the release of Letraset sheets containing Lorem Ipsum passages, and more recently
with desktop publishing software like Aldus PageMaker including versions of Lorem
Ipsum."""
    with open('Lorem.txt', 'w') as f:
        f.write(content)
        print('Файл успешно записан!')

def readLorem():
    with open('Lorem.txt','r') as Lorem:
        for i in Lorem:
            print(i)
def allReadLine():
    with open('Lorem.txt','r') as Lorem:
        for i in Lorem:
            print(i,end=" ")
def ReadArray():
    with open('Lorem.txt','r') as file:
        all=file.readlines()
        print(all)

#Task 2
def fileTextReverse():
    with open('lorem.txt', 'r') as f:
        content = f.read()
        print(content[::-1])
        # s = f.readlines()
        # s.reverse()
        # print(''.join(s))

#Task 3
def writeFile():
    n =  int(input('Сколько строк хотели бы записать? '))
    for i in range(n):
        text = input('Текст: ')
        with open('task3.txt', 'a') as f:
            f.write(f'{text}\n')
    print('Записи успешно добавлены!')

if __name__=='__main__':
    writeFile()
    # fileTextReverse()
    # writeLorem()
    # readLorem()
    # allReadLine()
    # ReadArray()



