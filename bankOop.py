class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            print(f"Withdrawling {amount} dollars")
            self.balance -= amount
        else:
            print(f"Withdraw of {amount} dollars was denied. Current balance is: {self.balance}")

    def display_balance(self):
        print("Balance: " + str(self.balance))


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
 
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.dueDateDay = 7

    # Class override to accept withdrawals up to the overdraft limit
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            print(f"Withdrawling {amount} dollars")
            self.balance -= amount
        else:
            print(f"Withdraw of {amount} dollars was denied. Current balance is {self.balance} and max overdraft limit is {self.overdraft_limit}")

    # Check if balance is negative, which means future charges
    def checkForInvoices(self):
        if self.balance < 0:
            print(f"The invoice value of {-self.balance}$ was found to be due on the {self.dueDateDay}th")
            return -self.balance

# Create instances and demonstrate method overriding
savings_account = SavingsAccount("SA001", 1000.0, 0.05)
checking_account = CheckingAccount("CA001", 500.0, 1000.0)

savings_account.deposit(500.0)
checking_account.deposit(200.0)

savings_account.display_balance()
checking_account.display_balance()

savings_account.apply_interest()
checking_account.withdraw(800.0)

savings_account.display_balance()
checking_account.display_balance()

checking_account.checkForInvoices()
checking_account.withdraw(3000.0)

