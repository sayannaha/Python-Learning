class Animal:
    def __init__(self, species):
        self.species = species
    def describe(self):
        print(f"I am a {self.species}.")
class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog") # Call parent constructor
        self.name = name
    def bark(self):
        print(f"{self.name} says Woof!")
dog = Dog("Buddy")
dog.describe()
dog.bark()