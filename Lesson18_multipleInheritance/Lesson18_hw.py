"""
1) Класс Xerocopy имеет атрибуты в конструкторе: nameModel, nameDoc,
copyQuantity, copyLimit

Также имеется метод Copy() , в котором копируется тот или иной документ.
Пример реализации метода:
«Модель xerox_copy123 скопировал документ «Мой отчет» в количестве 4 шт,
осталось 15 листов»

Если краски на копирования не остается, то выводится сообщение:
«Не осталось листов в копировальном аппарате!»

Также есть дополнительный метод addLists() для заполнения бумаги, то есть
увеличения атрибута copyLimit.

Реализация для метода copyLimit( ) выглядит следующим образом:
«У вас на копировальном аппарате было 0 листов, после пополнения стало 20
листов»

-----
2) Класс Printer имеет атрибуты в конструкторе: nameModel, nameDoc,
printQuantity, printLimit

Также имеется метод PrintColored() , в котором печатается тот или иной
документ.

Пример реализации метода:

«Модель printer_brandLux123 расспечатал документ «Мой отчет» в ЦВЕТНОМ
варианте в количестве 4 шт, осталось 15 листов»

Также имеется метод PrintBlacked() , в котором печатается тот или иной
документ.
Пример реализации метода:

«Модель printer_brandLux123 распечатал документ «Мой отчет» в количестве 4
шт, осталось 15 листов»
Если краски на распечатывание не остается, то выводится сообщение:
«Не осталось листов в печатном аппарате!»
Также есть дополнительный метод addLists( ) для заполнения бумаги, то есть
увеличения атрибута printLimit.

Реализация для метода addLists( ) выглядит следующим образом:
«У вас на печатном аппарате было 0 листов, после пополнения стало 20 листов»
------
3)
Класс LGTech содержит объединение двух предыдущих классов. То есть
LGTech это техника 2 в 1, где содержится и Принтер и Сканнер.
В этом классе, как и в предыдущих классах, вам нужно создать конструктор для
принятия значений как для копирования, так и для печати.
"""

class Xerocopy:
    def __init__(self, nameModel, nameDoc, copyQuantity, copyLimit):
        self.nameModel = nameModel
        self.docName = nameDoc
        self.copyQuant = copyQuantity #для краски
        self.copyLimit = copyLimit #для бумаги

    def copy(self, quntCopy):
        if self.copyLimit >= quntCopy:
            self.copyLimit -= quntCopy
            self.copyQuant = self.copyQuant - quntCopy//5

            print(f"Модель {self.nameModel}  скопировал документ "
                  f"{self.docName} в количестве {quntCopy}, осталось "
                  f"кол-во листов лимита: {self.copyLimit}")
        else:
            print('Недостаточно бумаги! Идет пополнение бумаги')
            print('Повторите операцию копирования вновь!')
            self.addList(quntCopy)


    def addList(self, quantAdd):
        self.copyLimit += quantAdd

    def limitIncrease(self, quantList, quantPaint):
        if self.copyLimit == 0 and self.copyQuant == 0:
            self.copyLimit += quantList
            self.copyQuant += quantPaint

            print(f'У вас бумаги в коп апарате было 0 и краски тоже 0, '
                  f'после пополнения стало бумаги {self.copyLimit} '
                  f'и краски: {self.copyQuant}')

        elif self.copyLimit == 0:
            self.copyLimit += quantList
            print(f'У вас бумаги в коп апарате было 0, '
                  f'после пополнения стало бумаги {self.copyLimit}')

        elif self.copyQuant == 0:
            self.copyQuant += quantPaint

            print(f'У вас бумаги в коп апарате было 0, '
                  f'после пополнения стало краски {self.copyQuant}')

class Printer:
    def __init__(self, nameModel, nameDoc, printQuantity, printLimit):
        self.nameModel = nameModel
        self.docName = nameDoc
        self.printQuantity = printQuantity #для краски
        self.printLimit = printLimit #для бумаги

    def printColored(self, quantPrint):
        if self.printLimit >= quantPrint:
            self.printLimit -= quantPrint
            self.printQuantity = self.printQuantity - quantPrint // 2

            print(f"Модель {self.nameModel} распечатал документ "
                  f"{self.docName} в цветном виде в количестве {quantPrint}, "
                  f"осталось кол-во листов бумаг: {self.printLimit}")
        else:
            print('Недостаточно бумаги! Идет пополнение бумаги')
            print('Повторите операцию копирования вновь!')
            self.addList(quantPrint)

    def printBlack(self, quantPrint):
        if self.printLimit >= quantPrint:
            self.printLimit -= quantPrint
            self.printQuantity = self.printQuantity - quantPrint // 5

            print(f"Модель {self.nameModel} распечатал документ "
                  f"{self.docName} в черном белом цвете "
                  f" в количестве {quantPrint}, осталось "
                  f"кол-во листов бумаг: {self.printLimit}")
        else:
            print('Недостаточно бумаги! Идет пополнение бумаги')
            print('Повторите операцию копирования вновь!')
            self.addList(quantPrint)

    def addList(self, quantAdd):
        self.printLimit += quantAdd

    def limitIncrease(self, quantList, quantPaint):
        if self.printLimit == 0 and self.printQuantity == 0:
            self.printLimit += quantList
            self.printQuantity += quantPaint

            print(f'У вас бумаги в коп апарате было 0 и краски тоже 0, '
                  f'после пополнения стало бумаги {self.printLimit} '
                  f'и краски: {self.printQuantity}')

        elif self.printLimit == 0:
            self.printLimit += quantList
            print(f'У вас бумаги в коп апарате было 0, '
                  f'после пополнения стало бумаги {self.printLimit}')

        elif self.printQuantity == 0:
            self.printQuantity += quantPaint

            print(f'У вас бумаги в коп апарате было 0, '
                  f'после пополнения стало краски {self.printQuantity}')

class LgTech(Xerocopy, Printer):
    def __init__(self, nameModel, nameDoc, cpLimit, cpQuant, prLimit, prQuant):
        super().__init__(nameModel,nameDoc, cpLimit, cpQuant)
        Printer.__init__(self,nameModel,nameDoc, prLimit, prQuant)

    def addList(self, quantAdd):
        if self.copyLimit == 0:
            super().addList(quantAdd)
        elif self.printLimit == 0:
            Printer.addList(self,quantAdd)

if __name__ == '__main__':
    # xc = Xerocopy('Toshiba', 'Отчет.doc', 20, 50)
    # xc.copy(30)
    # print(xc.copyLimit)
    # # xc.copy(35)
    # # xc.copy(35)
    # # xc.copy(30)
    # print(xc.copyQuant)
    # print(xc.copyLimit)
    # # xc.copyLimitIncrease(40, 10)

    # pr1 = Printer('Samsung', 'Кв отчет.doc', 40, 100)
    # pr1.printBlack(30)
    # pr1.printColored(30)
    #
    # print(pr1.printLimit)
    # print(pr1.printQuantity)

    lgTech = LgTech('LG 1232UX', 'PythonLesson.doc', 30, 50, 30, 50)
    # lgTech.copy(40)
    # lgTech.printBlack(50)
    lgTech.printBlack(50)
        # lgTech.addList(30)
    print(lgTech.printLimit)
    lgTech.addList(30)
    print(lgTech.printLimit)
    print(lgTech.copyLimit)

    # print(lgTech.copyLimit)


























