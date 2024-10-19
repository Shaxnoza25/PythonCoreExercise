try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    divide=number1/number2
    print("Quotient= ", divide)
except ZeroDivisionError as e:
     with open("error_log.txt", "a") as file:
         file.write(f"{e}+\n")
         print("Zero division Error occured")
except ValueError as e:
     with open("error_log.txt", "a") as file:
         file.write(f"{e}+\n")
         print("Value Error occured")

except OverflowError as e:
     with open("error_log.txt", "a") as file:
         file.write(f"{e}+\n")
         print("Result is very big")