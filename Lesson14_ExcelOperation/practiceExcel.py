import pandas as pd
#Task 5
def uniqueProductCategories():
    foodProd = pd.read_excel('food.xlsx', usecols=[3,4])
    uniqueProducts = set()
    for n in foodProd['Product']:
        uniqueProducts.add(n)
    print('Уникальные название продуктов: ')
    for p in uniqueProducts:
        print(p)

    uniqueCategory = set()
    for n in foodProd['Category']:
        uniqueCategory.add(n)

    print('Уникальные название категорий: ')
    for p in uniqueCategory:
        print(p)

if __name__ == '__main__':
    uniqueProductCategories()