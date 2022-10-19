#Task 1
import pandas as pd

#Task 1
def writeToExcelWorkers():
    """
    - Имя
    • Возраст
    • Заработную плату
    • Должность
    """

    workersDataFrame = pd.DataFrame(
        {
            'Имя': ['Asan', 'Uson', 'Tilek', 'Oleg', 'Marina', 'Samat', 'Aisuluu', 'Turat', 'Aiperi'],
            'Возраст': [23, 25, 31, 35, 28, 32, 21, 36, 22],
            'Заработная плата': [20000, 25000, 31000, 36000, 28000, 22000, 18000, 22000, 18000],
            'Должность': ['Стажер', 'Менеджер', 'Бухгалтер', 'Бухгалтер', 'Менеджер', 'Охранник', 'Стажер', 'Охранник', 'Стажер'],
        }
    )
    write = pd.ExcelWriter('workersInfo.xlsx', engine='xlsxwriter')
    workersDataFrame.to_excel(write, sheet_name='Информация о работниках', index = False)
    write.save()

#Task 2
def readExcel():
    cols = [1, 2]
    workersInfo = pd.read_excel('workersInfo.xlsx', usecols=cols)

    print(f'Max Salary: {workersInfo["Заработная плата"].max()}')
    print(f'Min Salary: {workersInfo["Заработная плата"].min()}')
    print(f'Avg Salary: {workersInfo["Заработная плата"].mean()}')

    print(f'Max age: {workersInfo["Возраст"].max()}')
    print(f'Min age: {workersInfo["Возраст"].min()}')
    print(f'Avg age: {workersInfo["Возраст"].mean()}')

#Task 3
def personMaxSalary():
    workersInfo = pd.read_excel('workersInfo.xlsx')
    maxSalary = workersInfo["Заработная плата"].max()

    for n, s in zip(workersInfo["Имя"],workersInfo["Заработная плата"]):
        if s == maxSalary:
            print(f'Человек с максимальной ЗП: {n}')
        else:
            continue

#Task 4
def sortByProfession():
    workers = pd.read_excel('workersInfo.xlsx')
    dict = {}

    for i in range(len(workers)):
        if workers['Должность'][i] in dict.keys():
            dict[workers['Должность'][i]].append(workers['Имя'][i])
        else:
            dict[workers['Должность'][i]] = [workers['Имя'][i]]
    print(dict)

def sortByProfession2():
    workersInfo = pd.read_excel('workersInfo.xlsx')
    dict = {}

    for n, p in zip(workersInfo["Имя"], workersInfo["Должность"]):
        if p not in dict:
            dict[p] = []
        if p in dict:
            dict[p].append(n)

    for p, listNames in dict.items():
        print(f'{p}: {listNames}')


if __name__ == '__main__':
    # writeToExcelWorkers()
    # readExcel()
    # personMaxSalary()
    # sortByProfession()
    sortByProfession2()


