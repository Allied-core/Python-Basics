try :
    a = int(input("Enter the I number: "))
    b = int(input("Enter the II number: "))
except:
    print("Invalid Input Error.")

def div(a,b):
    if b == 0:
       print("Division By Zero.")
    else:
       print(f"Result: {a/b}")

div(a,b)
