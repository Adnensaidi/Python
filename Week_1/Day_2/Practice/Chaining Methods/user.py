class User :
    def __init__(self,first_name,last_name,age,email) :
        self.first_name = first_name
        self.last_name=last_name
        self.age=age
        self.email=email
        self.gold_card_points=0
        self.is_rewards_member=False


    def display_info(self) :
        print(f"Name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Age : {self.age}")
        print(f"Email : {self.email}")
        print(f"Gold card points : {self.gold_card_points}")
        print(f"Rewards member : {self.is_rewards_member}")
    

    def enroll(self) :
        if  self.is_rewards_member == True :
            print(f"{self.first_name} is already a member")
            return False 
        else :
            self.is_rewards_member = True 
            self.gold_card_points =200
            return True 


    def spend_points(self,amount) :
        if self.gold_card_points > amount :
            self.gold_card_points = self.gold_card_points-amount 
        else : 
            print ("User does not have enough points")  

user_1 = User("Natalia","Jhonson",20,"Natalia.Jhonson@gmail.com")
user_2 = User("Jeremy","Myt",35,"Jeremy.Myt@gmail.com")
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()