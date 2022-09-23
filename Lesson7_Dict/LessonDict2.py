studentList = {
    "Oleg":"Moscow", "Stepan": "Novosibirsk", "Olga":
"Ekaterenburg", "Murat":"Bishkek", "David":"New Yourk"
}


#
# print(studentList > studentList2) Error
# print(studentList < studentList2) Error
# print(studentList >= studentList2) Error
# print(studentList <= studentList2) Error
studentList2 = {
    'Aisuluu': 'Naryn', 'Tilek': 'NY', 'Marat': 'Kazan'}

studentList3 = studentList2 | studentList

print(studentList3.get('Elena'))

#метод setdefault
print(studentList3.setdefault('Elena'))
print(studentList3)

studentList = {
    "Oleg":"Moscow", "Stepan": "Novosibirsk", "Olga":
"Ekaterenburg", "Murat":"Bishkek", "David":"New Yourk"
}

print(studentList3.setdefault('Adam', 'San-Francisco'))
print(studentList3)

print(studentList3.setdefault('Aisuluu', 'JA'))
print(studentList3)

studentList.pop('Oleg')
print(studentList)

#Метод popitem() - List-> pop()
studentList.popitem()
print(studentList)

