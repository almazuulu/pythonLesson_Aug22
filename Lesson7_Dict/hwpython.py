#Task 3

"""
votersDict = {
"Denis”:32,
“Sergei”:21,
“Elena”:18,
“Timur”:17,
“Oleg”: 27
}

Создать программу, которая в зависимости от возраста того или
иного человека из словаря votersDict решает кого допускать, а кого
не допускать к голосованию.
"""
votersDict = {
"Denis":32,
"Sergei":15,
"Elena":18,
"Timur":17,
"Oleg": 27
}

for name, age in votersDict.items():
    if age >= 18:
        print(f"Вас зовут {name}, вам {age} года и вы можете голосовать")
    else:
        print(f"Вас зовут {name}, вам {age} года и вы НЕ можете голосовать")

#Task 4

"""
Ваша задача попросить ввести имя человека и в зависимости от его
имени удалить от этого словаря. После удаления отобразите
словарь, чтобы убедится что конкретный человек был удален из
словаря
"""
#1 sposob

studentList = {
    "Oleg":"Moscow", "Stepan": "Novosibirsk", "Olga":
"Ekaterenburg", "Murat":"Bishkek", "David":"New Yourk"
}

nameDel = input('Введите имя студента для удаления: ')
# studentList.pop(nameDel)

# print(studentList)

#2 sposob
booleanFound = False
for name in studentList.keys():
    if nameDel == name:
        booleanFound = True

if booleanFound == True:
    del studentList[nameDel]
else:
    print('Этот пользователь не найден среди учащихся!')

print(studentList)






