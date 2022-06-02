from person import Person
from money import Money
from date_time import DateTime

class BankAccount:
    def __init__(self, p : Person, m: Money, d: DateTime): -> None
        self.customer = p
        self.account_number = '' #TODO: generate random 16-len string from digits
        self.balance = m 
        self.valid_till = d
        #TODO: add other data members if you need

    def __str__(self):
        return ""

    def deal(self, m):
        #TODO: make transaction , check if balance is enough
        pass

    def fill_balance(self, m):
        #TODO: fill your balance

    def deposite(self, m, d, p):
        # money, duration, percent
        # TODO: count many after duration with p percent




