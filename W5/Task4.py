sum=0
while True:
    num=input("Enter a number(or 'stop' to quit):")
    if num=="stop":
        print("Sum of entered numbers :", sum)
        break
    else:
        print("Continuing...")
    sum = sum + int(num)