class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        self.balance = self.balance - amount

class SavingAccount(Account):
    def __init__(self, balance, interestRate):
        Account.__init__(balance)
        self.interestRate = interestRate
    
    def interstAmount(self):
        return self.interstRate * self.balance / 100

acc1 = Account(5000)
acc1.deposit(500)
acc1.withdrawal(200)
print(acc1.getBalance())