def searchWorker(nameWorker):
    pass

myWorkerDict = {
  "Сотрудник 1":

          { "ФИО": "Адилет Эшмаматов",
            "Возраст": 28,
            "Род деятельности": "Работник цеха",
            "Заработная плата": 25000,
            "ФИО Супруга/и": "Гульзада Саратова",
            "Дети": { "Ребенок 1": "Мухаммад Эшмаматов",
                      "Ребенок 2": "Элиза Эшмаматова"

          },
            "Транспорт": "Тойота Камри 35",
            "Адрес проживания": "г. Бишкек, ул. Лев Толстой 77"

          },

  "Сотрудник 2":

          { "ФИО": "Эсен Урматов",
            "Возраст": 30,
            "Род деятельности": "Работник цеха",
            "Заработная плата": 31000,
            "ФИО Супруга/и": "Тамара Тиленова",
            "Дети": { "Ребенок 1": "Усон Урматов", },
            "Транспорт": "Хонда Фит",
            "Адрес проживания": "г. Бишкек, ул. Чуй 123"

          },

  "Сотрудник 3":

          {
              "ФИО": "Аселя Давлетова",
              "Возраст": 30,
              "Род деятельности": "Работник бухгалтерии",
              "Заработная плата": 42000, "ФИО Супруга/и":
              "Сергей Васильев",
              "Дети": { "Ребенок 1": "Елена Васильева",
                        "Ребенок 2": "Степан Васильев",
                        "Ребенок 3": "Марат Васильев", },
              "Транспорт": "БМВ X7",
              "Адрес проживания": "г. Бишкек, ул. Токтогула 76"
          },

  "Сотрудник 4":

          {
              "ФИО": "Мария Степанова",
              "Возраст": 29,
              "Род деятельности": "Работник маркетинга",
              "Заработная плата": 85000,
              "ФИО Супруга/и":
              "Олег Кичин", "Дети": { "Ребенок 1": "Василиса Кичина", },
              "Транспорт": "Пешком",
              "Адрес проживания": "г. Бишкек, мкр 7 дом 76, кв: 14"
          },

  "Сотрудник 5":
          {
              "ФИО": "Олег Иванов",
              "Возраст": 45,
              "Род деятельности": "Генеральный Директор",
              "Заработная плата": 70000,
              "ФИО Супруга/и": "Светлана Валерьева",
              "Дети": { "Ребенок 1": "Григорий Иванов",
                        "Ребенок 2": "Наталья Иванова",
                        "Ребенок 3": "Василий Иванов",
                        "Ребенок 4": "Филип Иванов", },
              "Транспорт": "БМВ X7",
              "Адрес проживания": "г. Бишкек, мкр 5 дом 16, кв: 102"
          },
      }

#Task1:

menu = """
  1 - Поиск сотрудника 
  2 - Добавление нового сотрудника 
  3 - Удаление сотрудника 
  4 - Составить список для награждения сотрудников 
  5 - Составить список сотрудников на отпуск 
  6 - Повышение З-П 
  7 - Понижение З-П 
  8 - Отобразить имя сотрудника, получающий максимальную З-П 
  9 - Отобразить имя сотрудника, получающий минимальную З-П 
  10 - Подсчет среднемесячной Заработной платы 
  11 - Вывод суммарной З-П всех сотрудников 
  12 - Виды транспорта всех сотрудников 
  13 - Отобразить имена и кол-во детей всех сотрудников 
  14 - Отобразить всех сотрудников 
  0 - Выход из Программы
"""
option = None
while option != 0:
      print(menu)

      option = int(input('Ввод: '))

      if option == 1:
          nameSearch = input('Вы выбрали меню №1.\nНапишите имя для поиска: ')

          for worker, workerDict in myWorkerDict.items():
              for key, valueWorker in workerDict.items():
                      if valueWorker == nameSearch:
                          for key, valueWorker in workerDict.items():
                              print(key, valueWorker)
      elif option == 2:
          nameInput = input('Вы выбрали меню №2.'
                            '\nНапишите ФИО Сотрудника для добавления: ')

          age = int(input('Возраст: '))
          typeWork = input('Род деятельности: ')
          salary = int(input('Напишите зарплату: '))
          fioWifeHusb = input('Напишите имя супруга/и: ')
          quantChild = int(input('Кол-во детей: '))
          child = {}
          #3 - range(3) - 0,1,2
          for i in range(quantChild):
              childKey = 'Ребенок '+ str(i+1)
              child[childKey] = input(f'Пожалуйста введите '
                                      f'имя для {i+1} ребенка: ')


          nameOfTransport = input('Название транспорта: ')
          address = input('Адрес проживания: ')

          countWorker = len(myWorkerDict) + 1
          countWorkerKey = 'Сотрудник '+ str(countWorker)
          myWorkerDict[countWorkerKey] = {"ФИО": nameInput,
                                                    "Возраст": age,
                                                    "Род деятельности":typeWork,
                                                    "Заработная плата":salary,
                                                    "ФИО Супруга/и":fioWifeHusb,
                                                    "Дети":child,
                                                    "Транспорт": nameOfTransport,
                                                    "Адрес проживания":address
                                                    }

          print('Новый словарь работников теперь выглядит так:')

          for worker, workerDict in myWorkerDict.items():
              print("===================")
              print(f'{worker}:\n'
                    f'===================')
              for key, values in workerDict.items():
                  if key == "Дети":
                      workerNameList = workerDict["ФИО"].split(" ")
                      print(f'Дети {workerNameList[0]}а {workerNameList[1]}а : '
                            f'\n************************')

                      for child, childInfo in values.items():
                          print(f'{child}: {childInfo}')
                      print('************************')
                  if key == "Дети":
                      continue
                  print(f'{key}: {values}')
      elif option == 3:
          nameDelete = input('Вы выбрали меню "Удаление сотрудника"\n'
                             'Напишите имя сотрудника для удаления: ')
          valDelete = None
          for worker, workerDict in myWorkerDict.items():
              for k, v in workerDict.items():
                  if nameDelete in workerDict.values():
                      valDelete = worker

          del myWorkerDict[valDelete]

          print('\nНовый словарь работников теперь выглядит так:')
          if len(myWorkerDict) != 0:
              for worker, workerDict in myWorkerDict.items():
                  print("===================")
                  print(f'{worker}:\n'
                        f'===================')
                  for key, values in workerDict.items():
                      if key == "Дети":
                          workerNameList = workerDict["ФИО"].split(" ")
                          print(f'Дети {workerNameList[0]}а {workerNameList[1]}а : '
                                f'\n************************')

                          for child, childInfo in values.items():
                              print(f'{child}: {childInfo}')
                          print('************************')
                      if key == "Дети":
                          continue
                      print(f'{key}: {values}')
          else:
              print('База сотрудников пуста!')
      elif option == 4:
          listAwardedWorkers = []
          numberAwarded = int(input('Вы выбрали меню №4.\nНапишите кол-во людей для награждения: '))

          for i in range(numberAwarded):
                nameAwarded = input('Имя чел-ка для награждения: ')
                for worker, workerDict in myWorkerDict.items():
                    if nameAwarded == workerDict["ФИО"]:
                        listAwardedWorkers.append(workerDict["ФИО"])
                    else:
                        pass
          print(listAwardedWorkers)
          counter = 1
          for i in listAwardedWorkers:
              print(f'Сотдрудник {counter} -ый для награды {i}')
              counter += 1
      elif option == 5:
          pass
      elif option == 6:
          print('Вы выбрали меню 6 - Повышение З-П')

          nameWorker = input('Введите имя сотруд-ка, для повышение ЗП: ')
          salaryAdd_value = int(input('На сколько повысить ЗП? :'))

          keyWorker = None
          for worker, workerDict in myWorkerDict.items():
              for k, v in workerDict.items():
                  if nameWorker in workerDict.values():
                      keyWorker = worker

          #myWorkerDict[keyWorker]["Заработная плата"] =  int(myWorkerDict[keyWorker]["Заработная плата"]) + salaryAdd_value
          myWorkerDict[keyWorker]["Заработная плата"] += salaryAdd_value

          print(f'Новая ЗП сотрудника {myWorkerDict[keyWorker]["ФИО"]}: {myWorkerDict[keyWorker]["Заработная плата"]}')

      elif option == 7:
          pass
      elif option == 8:
          print('Вы выбрали меню 8 - Отобразить имя сотрудника, получающий максимальную З-П ')
          salaryList = []
          for worker, workerDict in myWorkerDict.items():
              salaryList.append(workerDict["Заработная плата"])
          maxSalary = max(salaryList)

          nameWorker_maxSalary = None
          for worker, workerDict in myWorkerDict.items():
              if workerDict["Заработная плата"] == maxSalary:
                  nameWorker_maxSalary = workerDict["ФИО"]

          print(f'Сотрудник с максимальной ЗП: {nameWorker_maxSalary}')

      elif option == 9:
          pass
      elif option == 10:
          pass
      elif option == 11:
          sumSalary = 0
          salaryList = []
          for worker, workerDict in myWorkerDict.items():
              salaryList.append(workerDict["Заработная плата"])

          print(f'Суммарная З-П всех сотрудников: {sum(salaryList)}')
      elif option == 12:
         pass
      elif option == 13:
         pass
      elif option == 14:
          for worker, workerDict in myWorkerDict.items():
              print("===================")
              print(f'{worker}:\n'
                    f'===================' )
              for key, values in workerDict.items():
                  if key == "Дети":
                      workerNameList = workerDict["ФИО"].split(" ")
                      print(f'Дети {workerNameList[0]}а {workerNameList[1]}а : '
                            f'\n************************')

                      for child, childInfo in values.items():
                          print(f'{child}: {childInfo}')
                      print('************************')
                  if key == "Дети":
                      continue
                  print(f'{key}: {values}')
      if option == 0:
          print('Программа Завершена! Всего Вам хорошего!')
          break

      elif option not in (range(0,15)):
          print('Вы выбрали не правильную опцию! Попытайтесь заново!')




