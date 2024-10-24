class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Not enough points to spend.")
            return False
        else:
            self.gold_card_points -= amount
            return True


if __name__ == "__main__":
    user1 = User("John", "Doe", "john@example.com", 30)
    user1.display_info()

    user1.enroll()

    user2 = User("Jane", "Smith", "jane@example.com", 28)
    user3 = User("Bob", "Brown", "bob@example.com", 25)

    user1.spend_points(50)

    user2.enroll()

    user2.spend_points(80)

    user1.display_info()
    user2.display_info()
    user3.display_info()
