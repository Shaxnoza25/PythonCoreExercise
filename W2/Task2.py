try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    divide=number1/number2
    print("Quotient= ", divide)
except ZeroDivisionError:
    print("Cannot divide to zero")
except ValueError:
    print("Please enter integer numbers")
finally:
    "Finished"