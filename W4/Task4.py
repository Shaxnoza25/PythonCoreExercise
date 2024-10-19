account_balance=float(input("Enter your account balance: "))
withdraw_amount=float(input("Enter your withdrawal amount: "))
if withdraw_amount<10 and withdraw_amount>500:
    print("Error massage")
elif account_balance>=withdraw_amount:
    print("You can make transaction")
elif withdraw_amount>account_balance:
    print("Insufficient funds")