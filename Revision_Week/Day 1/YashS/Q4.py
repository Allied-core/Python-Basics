def check(a):
    if a > 0 :
       print("Positive")
    elif a < 0 :
       print("Negative")
    else :
       print("Zero")


while True:
    try:
       a = int(input("Enter the integer:"))
    except:
       print("Invalid Input")
    print("1. Check Positive/Negative/Zero")
    print("TYPE 'exit' to Exit")
    cmd = input("Enter your choice: ")

    if cmd == "1":
       check(a)
    elif cmd == "exit":
       break
    else:
       print("Invalid Command")
