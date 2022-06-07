#
import random
import string

#
from person import Person
from money import Money
from date_time import Date

class BankAccount:
    def __init__(self, p : Person, m: Money, vt: Date) -> None:
        self.__customer = p
        self.__account_number = ''.join(random.choices(string.digits, k = 16))
        self.__balance = m 
        self.__valid_till = vt

    #TODO: get and set for all members

    def __str__(self) -> str:
        return "Personal info ----{}\nAccount number ---- {}\nBalance ---- {}".format(self.__customer, self.__account_number, self.__balance)

    def deal(self, m):
        x = self.__balance - m

        if x: 
            self.__balance = x
            print("Deal approved. Your current balance is {}".format(x))
        else:
            print("Sorry. Balance is not enough.")


    def fill_balance(self, m):
        self.__balance += m
        print("Congratulations!!! Balance successfully filled!!!\nYour current balance is {}".format(self.__balance))


    def deposite(self, m, d, p):
        # money, duration, percent
        # TODO: count many after duration with p percent
        pass

    def update(self, n):
        self.__valid_till.add_year(n)

p = Person("Gegham", "Jivanyan", 32, "Gender")
m = Money("USD", 1000)

ba = BankAccount(p, m)
#m1 = Money("RUB", 1500)
#ba.deal(m1)
#ba.fill_balance(m1)
vt = Date(2024, 6, 7)
c = Card(p, m, vt)

print(c)
