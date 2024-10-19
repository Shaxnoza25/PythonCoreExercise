import random
number_to_guess=random.randint(1,10)
attemp=0
while number_to_guess:
    num = int(input("Guess the number(1-10)"))
    attemp+=1
    if num > number_to_guess:
        print("Your number is too high enter lower one")
    elif num < number_to_guess:
        print("Your number is too low enter higher one")
    else:
        print("You are correct, you found in ", attemp," attemp")
        break
