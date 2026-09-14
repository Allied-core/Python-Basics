def check(a):
    if a % 2 >= 0 :
       print("Odd")
    else :
       print("Even")


while True:
    try:
       a = int(input("Enter the integer:"))
    except:
       print("Invalid Input")
    print("1. Check Even or Odd ")
    print("TYPE 'exit' to Exit")
    cmd = input("Enter your choice: ")

    if cmd == "1":
       check(a)
    elif cmd == "exit":
       break
    else:
       print("Invalid Command")
