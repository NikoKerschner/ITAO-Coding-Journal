ask = input("Do you think Github is easy?  Yes or No  ")

if ask == "Yes":
    print("Are you sure about that?  Try again  ")
    ask2 = input("Seriously, do you think Github is easy?  Yes or No?  ")
    if ask2 == "Yes":
        print("Ok genius guess you are a coding legend")
    elif ask2 =="No":
        print("Thank you for being honest")
    else:
        print("Guess you messed up the answer man, we'll just assume you're confused")
elif ask == "No":
    print("Glad we are on the same page")
else:
    print("You didn't choose one of the answers bruh")