try:
   a = int(input("Enter the I number: "))
   b = int(input("Enter the II number: "))
except:
   print("Invalid Input!")
def add(a,b):
    return a + b

print(f"Result : {add(a,b)}")
