from Park import *
from Animals import *

answer = input("Do you want to come to my zoo? Please put yes or no").lower()

if answer == "no":
    print("well screw you, please leave!!!!")
elif answer == "yes":
    print("Nice!  What animals would you like to see?")
    firstAnimal = input("Please decide what animal you would like to see first:  Your options are Fish,Shark, Dog, Bear, Lion ").lower()
    if firstAnimal == "shark":
        jaws = Shark("Jaws", 10, "Grey", "Hammerhead")
        print("The shark says")
        jaws.speak()
    elif firstAnimal == "dog":
        coop = Dog("Cooper", 2, "Golden", "Retriever")
        print("the dog says")
        coop.speak()
    elif firstAnimal == "fish":
        finn = Fish("Finn", 28, "Blue", "Beta fish")
        print("the fish goes")
        finn.speak()
    elif firstAnimal == "lion":
        simba = Lion("Simba", 13, "Yellow", "Lion")
        print("The lion goes")
        simba.speak()
    elif firstAnimal == "bear":
        smokey = Bear("Smokey", 100, "Brown", "Grizzly Bear")
        print("The bear goes")
        smokey.speak()
    else:
        print("You didn't choose an animal!!!  Guess you left my zoo")
else:
    print("Guess you didn't really want to see the animals")


