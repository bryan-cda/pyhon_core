import random


class NuAccount:

    def __init__(self, ag, cc, am):
        self.ag = ag
        self.cc = cc
        self.am = am

    def get_acc(self):
        print("Welcome to NuBank \n Agency: {}, Current Account {}, Amount {}. ".format(self.ag, self.cc, self.am))

    def withdraw(self, value):
        self.am = self.am - value

    def deposit(self, value):
        self.am = self.am + value

    def balance(self):
        print(self.am)

    def pix(self, value, origin, target):
        origin.withdraw(value)
        target.deposit(value)
        print(origin.am)
