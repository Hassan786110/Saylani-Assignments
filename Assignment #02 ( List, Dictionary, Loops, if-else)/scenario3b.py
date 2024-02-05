password = input("Enter your password\n\nPassword should be at least 8 characters long\nPassword should contain at least one digit\nPassword should contain at least one letter")
level = 2

if len(password) >= 8:
    level += 1

if password.isalpha() or password.isdigit():
    level -= 1

if level == 1:
    print("Password Strength: Very Weak")
elif level == 2:
    print("Password Strength: Weak")
elif level == 3:
    print("Password Strength: Strong")