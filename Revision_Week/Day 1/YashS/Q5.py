def check(a,b,c):
    if a > b & a > c :
       print(f"Largest Number: {a}")
    elif b > a & b > c :
       print(f"Largest Number: {b}")
    elif c > b & a < c :
       print(f"Largest Number: {c}")
    else:
       print("Duplicates Found")


while True:
    try:
       a = int(input("Enter the integer:"))
       b = int(input("Enter the integer:"))
       c = int(input("Enter the integer:"))    
    except:
       print("Invalid Input")
    print("1. Check Largest Number")
    print("TYPE 'exit' to Exit")
    cmd = input("Enter your choice: ")

    if cmd == "1":
       check(a,b,c)
    elif cmd == "exit":
       break
    else:
       print("Invalid Command")
