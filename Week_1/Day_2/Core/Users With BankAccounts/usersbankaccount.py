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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [] 

    def add_account(self, int_rate=0.01, balance=0):
        new_account = BankAccount(int_rate, balance)
        self.accounts.append(new_account)
        return new_account

    def make_deposit(self, account_index, amount):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].deposit(amount)
        else:
            print("Invalid account index")

    def make_withdrawal(self, account_index, amount):
        if 0 <= account_index < len(self.accounts):
            self.accounts[account_index].withdraw(amount)
        else:
            print("Invalid account index")

    def display_user_balance(self, account_index):
        if 0 <= account_index < len(self.accounts):
            print(f"{self.name}'s Account Balance:")
            self.accounts[account_index].display_account_info()
        else:
            print("Invalid account index")

    def transfer_money(self, amount, other_user, account_index):
        if 0 <= account_index < len(self.accounts):
            if self.accounts[account_index].balance >= amount:
                self.accounts[account_index].withdraw(amount)
                other_user.make_deposit(other_user.add_account().balance, amount)  
            else:
                print("Insufficient funds for transfer")
        else:
            print("Invalid account index")


user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")

user1.add_account(int_rate=0.02, balance=100)
user2.add_account(int_rate=0.03, balance=200)

user1.make_deposit(0, 50)
user1.make_withdrawal(0, 30)
user1.display_user_balance(0)

user2.make_deposit(0, 100)
user2.make_withdrawal(0, 50)
user2.display_user_balance(0)

user1.transfer_money(50, user2, 0)

user1.display_user_balance(0)
user2.display_user_balance(0)