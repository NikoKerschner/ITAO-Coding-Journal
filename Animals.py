class Pet:
    def __init__(self, name, age, color, breed):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed

    def intro(self):
        print(f"Hello, my name is {self.name}, I am a {self.color} {self.breed}, and I am {self.age} years old")

class Fish(Pet):
    def speak(self):
        print("Blub Blub Blub")

class Lion(Pet):
    def speak(self):
        print("ROAR!!!!")

class Dog(Pet):
    def speak(self):
        print("Woof!")

Daisy = Pet("Daisy",2,"Yellow", "Goldador")


