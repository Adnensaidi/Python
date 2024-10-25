class BankAccount:
    int_rate = 0.01 
    balance = 0
    def init(self, int_rate, balance): 
        self.int_rate= int_rate 
        self.balance =balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("insufficient funds : Charging a $5 fee")
            self.balance=self.balance-5
        return self

    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        return self 
    def yield_interest(self):
        if self.balance > 0 :
            self.balance = self.balance+(self.balance * self.int_rate)
        return self 
user_1 = BankAccount(0.3,300)
user_2= BankAccount(0.4,100)
user_1.deposit(50).deposit(100).deposit(30).withdraw(300).yield_interest().display_account_info()
user_2.deposit(20).deposit(40).withdraw(50).withdraw(100).withdraw(60).withdraw(100).yield_interest().display_account_info()
0 commit comments
Comments
0
 (0)