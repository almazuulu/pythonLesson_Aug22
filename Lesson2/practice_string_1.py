#Task 1
#Принятие данных от пользователя

name, age, company_name, family_status, adress = input('Name: '), int(input('Age: ')), \
                                                 input('Company name: '), input('Family Status: '),\
                                                 input('Adress: ')

print(f"Do company have letter 'a' {'a' in company_name}")
print(f"Second index of adderss: {adress[2]}")
print(f"Name of person from 2nd letter: {name[1:]}")
print(f"Company name in reverse order {company_name[::-1]}")

