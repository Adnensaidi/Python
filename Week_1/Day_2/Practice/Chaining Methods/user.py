class User:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.enrolled = False

    def display_info(self):
        print(f"User: {self.name}, Points: {self.points}, Enrolled: {self.enrolled}")
        return self

    def enroll(self):
        self.enrolled = True
        print(f"{self.name} has enrolled.")
        return self

    def spend_points(self, points):
        if self.points >= points:
            self.points -= points
            print(f"{self.name} spent {points} points.")
        else:
            print(f"{self.name} does not have enough points to spend.")
        return self
    
user1 = User("Alice")
user2 = User("Bob")


user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()