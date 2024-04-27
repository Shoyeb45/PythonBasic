class Account:
    def __init__(self, title, balance, ACNumber):
        self.__title = title
        self.__balance = balance
        self.__ACNumber = ACNumber
    
    def getBalance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdrawal(self, amount):
        self.__balance = self.__balance - amount

class SavingAccount(Account):
    def __init__(self, balance, interestRate):
        Account.__init__(balance)
        self.interestRate = interestRate
    
    def interstAmount(self):
        return self.interstRate * self.balance / 100
    
class CurrnetAccount(Account):
    def __init__(self, limit, balance):
        self.limit = limit
        self.__balance =  balance

# acc1 = Account(5000)
# acc1.deposit(500)
# acc1.withdrawal(200)
# print(acc1.getBalance())

x = CurrnetAccount(910000, 90000)

acc1 = SavingAccount(123, 91000, 3.4)
acc2 = Account("Aryan", 12437567832463485798347987, 778602010007627)
print(acc2.title)