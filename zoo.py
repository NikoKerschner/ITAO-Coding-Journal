from Park import *
from Animals import *

answer = input("Do you want to come to my zoo? Please put yes or no" ).lower()

if answer == "no":
    print("well screw you, please leave")
elif answer == "yes":
    print("Nice!  What animals would you like to see?")
    firstAnimal = input("Please decide what animal you would like to see:  Your options are Fish,Shark, Dog, Bear, Lion").lower()
    if firstAnimal == "shark":
        jaws = Shark("Jaws", "10", "Grey", "Hammerhead")
        jaws.speak()

