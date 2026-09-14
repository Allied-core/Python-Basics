def check(a,b):
    if not (isinstance(a,int) & isinstance(b,int)):
        print("Invalid Output.")
        return False

    else:
        return True

def add(a,b):
   if check(a,b) :
      return a + b

def div(a,b):
   if check(a,b) :
      if b <= 0 :
        print("Division by Zero.")
      else:
        return a / b

def mul(a,b):
   if check(a,b) :
      return a * b

def sub(a,b):
   if check(a,b) :
      return a - b

def rmd(a,b):
   if check(a,b) :
      return a % b

while True:
    try:
       a = int(input("Enter the First integer:"))
       b = int(input("Enter the Second integer:"))
    except:
       print("Invalid Input")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("TYPE 'exit' to Exit.")
    cmd = input("Enter your choice: ")
  
    if cmd == "1":
       print(add(a,b))
    elif cmd == "2":
       print(sub(a,b))
    elif cmd == "3":
       print(mul(a,b))
    elif cmd == "4":
       print(div(a,b))
    elif cmd == "5":
       print(rmd(a,b))
    elif cmd == "exit":
       break  
    else:
       print("Invalid Command")
