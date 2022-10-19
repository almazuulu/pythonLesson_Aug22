import pandas as pd
def writeToExcel():

    schoolInfo = {
        'Teachers': ['Elena Stapanovna', 'Sergei Mihalych', 'Valentina Grigorievna'],
        'Lessons': ['Geography', 'Mathematics', 'Chemistry']
    }

    teachersData = pd.DataFrame(
        schoolInfo)
    #1 - sposob записи в экзель файл
    write = pd.ExcelWriter('teachersInfo.xlsx', engine='xlsxwriter')
    teachersData.to_excel(write, sheet_name='Teachers lessons')
    # write.save()
    print('Данные успешно записались!')
    # 2 - sposob записи в экзель файл

    write2 = pd.ExcelWriter('teachersInfo2.xlsx', engine='xlsxwriter')
    friendsData = pd.DataFrame(
        {
            'Oleg': ['Stepan', 'Marat', 'Tilek'],
            'Alena': ['Elena', 'Marina', 'Aiperi']
        }
    )

    friendsData.to_excel(write2, sheet_name='Friends Data', index=False)
    write2.save()

def readFile():
    foodInfo = pd.read_excel('food.xlsx')
    print(foodInfo)
    #чтение первых n- строк
    print(foodInfo.head(5))

    #Чтение определенных колонок
    print(foodInfo['Product'])
    print(foodInfo[['Product', 'Category', 'Region']])

    # Чтение последних n строк
    print(foodInfo.tail(10))

    foodsProduct = foodInfo['Product']
    print(foodsProduct[12:34])

    foodsProductCategory2 = foodInfo[['Product', 'Category', 'Region']]
    print(foodsProductCategory2[15:])

    #Статистическая информация
    print(foodInfo.describe())

    #Отображение информации по индексу
    for n in foodsProduct:
        print(n)

    listProduct = [n for n in foodsProduct]
    print(listProduct)
    print(foodInfo.iloc[152])

def readcols():
    # cols = [1,2,4,7]
    foodInfo = pd.read_excel('food.xlsx', usecols=[1,2,4,7])
    print(foodInfo['Product'])
    print(type(foodInfo))

    # print(foodInfo['TotalPrice'])

if __name__ == '__main__':
    # writeToExcel()
    # readFile()
    readcols()
