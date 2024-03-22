class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance 


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate = 0):
        Account.__init__(title)
        super().__init__(balance)
        self.interestRate = interestRate
    
mark = Account("Mark", 5000)


mark = SavingsAccount("Mark", 5000, 5)
print(mark.interestRate)
