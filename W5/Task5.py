current_balance=100
print("Your current balance is ",current_balance)
while True:
    withdrawal_balance = int(input("How much money you want withdraw ($) ?"))
    if withdrawal_balance<=current_balance:
        current_balance=current_balance-withdrawal_balance
        print("Your new balance is ",current_balance)
        if current_balance==0:
            print("Your balance equals to zero. No more withdrawals.")
            break
    else:
        print("Your balance is not enough for withdrawing! Try again")

