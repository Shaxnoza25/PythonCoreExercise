days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day=input("Enter a day (With upper case) :")
if day in days:
    print("Yes, it is a weekday!")
else:
    print("No, it is not a weekday!")
if day not in days[0:5]:
    print("It is a weekend day!")
else:
    print("It is a work day!")