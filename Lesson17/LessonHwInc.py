class BanckAccount:
    def __init__(self, id, balance):
        self.__id = id
        self.__balance = balance

    def display(self):
        print(f'Банковский аккаунт #{self.__id}'
              f'\nВаш текущий баланс: {self.__balance}\n')

    def withdraw(self, money):
        if money > self.__balance or self.__balance == 0:
            print('Недостаточный баланс!')
            return

        # self.__balance = self.__balance - money
        self.__balance -= money
        print(f'Вы сняли {money} из вашего баланса '
              f'\nи теперь ваш баланс выглядит сл.образом: ')
        self.display()

    def deposit(self, money):
        if money == 0:
            print('Невозможно пополнить нулевым балансом!')
        # self.__balance = self.__balance - money
        self.__balance += money
        print(f'Вы добавили {money} к вашему баланса '
              f'\nи теперь ваш баланс выглядит сл.образом: ')
        self.display()

ba1 = BanckAccount('12312329213123', 50000)
ba2 = BanckAccount('12312329280992', 70000)

ba1.display()
ba2.display()

ba1.withdraw(20000)
ba2.withdraw(15000)

ba1.deposit(50000)

ba1.withdraw(120000)






