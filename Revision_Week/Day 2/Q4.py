try:
    num = int(input("Enter the number: "))
except:
    print("Invalid Input.")

count = 0

if num < 0 :
   num = num - (num*2)

if num == 0 :
   count = 1

else:
    while(num > 1):
         num = num / 10
         count += 1

print(f"Digit count: {count}")
