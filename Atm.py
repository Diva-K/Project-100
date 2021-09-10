class ATM(object):
    def __init__(self, card_number, pin_number, balance):
        self.card_number=card_number
        self.pin_number=pin_number
        self.balance=balance
    def cash_withdrawal(self, amount):
        print("your cash has been withdrawed", amount)
    def balancEnquery(self):
        print("your current palance is", self.balance)
    def cash_deposit(self, amount):
        print("your cash has been deposited", amount)
ATM1=ATM(2345, 1234, 200025)
print(ATM1.card_number)
print(ATM1.pin_number)
print(ATM1.cash_withdrawal(2004))
print(ATM1.balancEnquery())
print(ATM1.cash_deposit(24))


    