class Animal:
    def __init__(self, name, age, color, breed):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed

    def intro(self):
        print(f"Hello, my name is {self.name}, I am a {self.color} {self.breed}, and I am {self.age} years old")

class Fish(Animal):
    def speak(self):
        print("Blub Blub Blub")

class Lion(Animal):
    def speak(self):
        print("ROAR!!!!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

Daisy = Animal("Daisy",2,"Yellow", "Goldador")

class Bear(Animal):
    def speak(self):
        print("Growllll")

class Shark(Animal):
    def speak(self):
        print("Chomp Chomp Chomp")

