age=int(input("Enter your age: "))
height=float(input("Enter your height: "))
if age>=12 and height>=140:
    print("You can ride the coaster!")
elif age>=12 or height>=140:
    print("You can ride the coaster with an adult!")
else:
    print("Unfortunately you cannot ride the coaster")