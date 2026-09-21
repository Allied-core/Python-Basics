password = input("Enter password: ")

length = len(password) >= 8
digit = any(dig.isdigit() for dig in password)
upper = any(Upp.isupper() for Upp in password)

if length and digit and upper:
    print("Strong Password")
else:
    print("Weak Password")   
