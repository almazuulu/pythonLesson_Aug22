from datetime import *

#Task1
def parsingDate(d):
    """
    Примите от пользователя дату в следующем формате d-m/yyy-(H:M:S)
    Создайте на основе принятого от пользователя времени новую дату
    """
    dateUser = datetime.strptime(d, '%d-%m/%Y-(%H:%M:%S)')
    return dateUser

def makeFormatDate(d):
    """
    Созданную дату из задания No1 переделайте в следующий формате
    «день-название месяца полностью-(день недели)-год с двумя цифрами -
    Часы:Минута»

    Пример: 23-August - Wed - 22 - 6:30
    """
    print(d.strftime("%d-%B - %a - %y - %H:%M"))

def findDate():
    """
    Выясните какое будет время спустя:
    • 2 месяца от текущей даты?
    • через 2 Года?
    • Через год и 2 дня?
    • Через 3 месяца и 3 дня?
    И отобразите эти значения на экране
    """
    now = datetime.now()
    print(f'2 Месяца спустя сегодняшней даты: {now + timedelta(days = 30 * 2)}')
    print(f'2 Года спустя сегодняшней даты: {now + timedelta(days = 365 * 2)}')
    print(f'Через 2 Года и 2 дня от сегодняшней даты: {now + timedelta(days=365 * 2 + 2)}')
    print(f'Через 3 Месяца и 3 дня от сегодняшней даты: {now + timedelta(days = 30 * 3 + 2)}')


if __name__=='__main__':
    # user_date = input('Введите дату в формате d-m/yyy-(H:M:S): ')
    # formatedDate = parsingDate(user_date)
    #
    # makeFormatDate(formatedDate)
    findDate()
