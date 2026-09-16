try:
    num = int(input("Enter the number: "))
except:
    print("Invalid Input.")

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
