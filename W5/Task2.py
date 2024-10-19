correct_password="secret123"
attemp=1
while attemp<=3:
    password = input("Enter a password:")
    if password==correct_password:
        print("Access granted in ", attemp," attemp!")
        break
    else:
        print("Incorrect! ",3-attemp," attemps remaining")
    attemp+=1
print("Error is occured, your account is blocked")