class Account:

    def __init__(self, ag, acc, am):
        self.__ag = ag
        self.__acc = acc
        self.__am = am

    def withdraw(self, value):
        if value <= self.__am:
            self.__am = self.__am - value
        else:
            print('insufficient funds')

    def deposit(self, value):
        self.__am = self.__am + value

    def balance(self):
        print(self.__am)

    @staticmethod
    def transfer(value, origin, target):
        origin.withdraw(value)
        target.deposit(value)

    @property
    def amount(self):
        return self.__am

    @amount.setter
    def amount(self, amount):
        self.__am = amount

    @property
    def acc(self):
        return self.__acc

    @acc.setter
    def acc(self, acc):
        self.__acc = acc

    @property
    def ag(self):
        return self.__ag

    @ag.setter
    def ag(self, ag):
        self.__ag = ag
