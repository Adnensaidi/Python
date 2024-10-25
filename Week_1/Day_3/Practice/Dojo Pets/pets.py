class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping. Energy is now {self.energy}.")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating. Energy: {self.energy}, Health: {self.health}.")

    def play(self):
        self.health += 5
        print(f"{self.name} is playing. Health is now {self.health}.")

    def noise(self):
        print(f"{self.name} makes a noise!")


class Dog(Pet):
    def noise(self):
        print(f"{self.name} barks!")


class Cat(Pet):
    def noise(self):
        print(f"{self.name} meows!")


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is taking {self.pet.name} for a walk.")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}.")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()


my_dog = Dog(name="Buddy", pet_type="Dog", tricks=["roll over", "play dead"])
my_ninja = Ninja(first_name="Naruto", last_name="Uzumaki", treats=5, pet_food="Dog food", pet=my_dog)

my_ninja.feed()
my_ninja.walk()
my_ninja.bathe()

my_cat = Cat(name="Whiskers", pet_type="Cat", tricks=["sit", "high five"])
my_ninja_with_cat = Ninja(first_name="Sakura", last_name="Haruno", treats=3, pet_food="Cat food", pet=my_cat)

my_ninja_with_cat.feed()
my_ninja_with_cat.walk()
my_ninja_with_cat.bathe()