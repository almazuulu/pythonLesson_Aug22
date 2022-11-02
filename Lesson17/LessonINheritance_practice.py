class BanckAccount:
    def __init__(self, id, balance):
        self.__id = id
        self.__balance = balance
        self.__limit = 10000
        self.__discount = 0.1

    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount

    def display(self):
        print(f'Банковский аккаунт #{self.__id}'
              f'\nВаш текущий баланс: {self.__balance}\n')

    def withdraw(self, money):
        if money > self.__balance or self.__balance == 0:
            print('Недостаточный баланс!')
            return

        if money > self.limit:
            print('Вы превысили лимит для снятия денег!')
            return

        # self.__balance = self.__balance - money
        self.__balance -= money
        print(f'Вы сняли {money} из вашего баланса '
              f'\nи теперь ваш баланс выглядит сл.образом: ')
        self.display()

    def service(self, purchAmount):
        #0.1 - 10% discount
        purchAmount = purchAmount - (purchAmount * self.discount)
        self.__balance -= purchAmount

    def deposit(self, money):
        if money == 0:
            print('Невозможно пополнить нулевым балансом!')

        if money > self.limit:
            print('Вы превысили лимит для пополнение баланса!')
            return

        # self.__balance = self.__balance - money
        self.__balance += money
        print(f'Вы добавили {money} к вашему баланса '
              f'\nи теперь ваш баланс выглядит сл.образом: ')
        self.display()

class Premium_account(BanckAccount):
    def __init__(self, id, balance):
        self.set_id(id)
        self.balance = balance
        self.limit = 50000
        self.discount = 0.3

    # def __init__(self, id, ):

class Vip_account(BanckAccount):
    def __init__(self, id, balance):
        self.set_id(id)
        self.balance = balance
        self.limit = 100000
        self.discount = 0.5

ba1 = BanckAccount('12312329213123', 50000)
ba2 = BanckAccount('12312329280992', 70000)

ba1.display()
ba2.display()

ba1.withdraw(20000)
ba2.withdraw(15000)

ba1.deposit(50000)

# ba1.withdraw(120000)

ba1.service(5000)
ba1.display()

pa1 = Premium_account('2342434343242342', 120000)
pa1.withdraw(40000)
pa1.deposit(30000)

# pa1.display()

# print(pa1.get_id(), pa1.balance, pa1.limit)
