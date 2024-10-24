class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self  

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5 
        return self  

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")
        return self  

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self    

    @classmethod
    def print_all_accounts_info(cls, accounts):
        for account in accounts:
            account.display_account_info()


account1 = BankAccount(int_rate=0.05)
account2 = BankAccount(int_rate=0.03)

account1.deposit(100).deposit(50).withdraw(30).yield_interest().display_account_info()

account2.deposit(200).deposit(100).withdraw(50).withdraw(30).withdraw(20).withdraw(10).yield_interest().display_account_info()

BankAccount.print_all_accounts_info([account1, account2])