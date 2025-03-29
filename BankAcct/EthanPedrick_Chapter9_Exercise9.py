# This program stores the bank account information associated with a specific user. Ethan Pedrick / Chapter 9 Assignment 9


class BankAccount:
    def __init__(self, name, accNum, bal, interest):
        self.name = name
        self.accNum = accNum
        self.bal = bal
        self.interest = interest

    def __str__(self):
        return (f"Account Owner: {self.name}, "
                f"Account Number: {self.accNum}, "
                f"Current Balance: {self.bal}, "
                f"Current Interest Rate: {self.interest}")

    def deposit(self, amount):
        self.bal = self.bal + amount
        return;

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal = self.bal - amount
        else:
            print("The account does not have a high enough balance to withdraw this much!")
        return;

    def getBalance(self):
        return self.bal;

    def getInterest(self):
        return self.interest

    def setInterest(self, interest):
        self.interest = interest

    def calculateInterest(self, days):
        bal = self.bal
        interest = self.interest

        return (bal + (bal * (interest * days/365)))





# ---------------------------------- END OF BANK ACCOUNT CLASS -------------------------------------------

def test():
    account = BankAccount("Ethan", 1234, 10000, 0.05)

    account.deposit(5000)

    account.withdraw(50)

    print("Balance: " + str(account.getBalance()))

    print(account.__str__() + "\n")

    print(account.calculateInterest(365))

    account.setInterest(0.07)

    print(account.calculateInterest(365))

    account.withdraw(14951)

test()