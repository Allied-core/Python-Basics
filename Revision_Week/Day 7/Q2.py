numbers = [10, 20, 30, 40, 50]

try:
   n = int(input("Enter the index: "))
except:
   print("Invalid Input Error")

if n > len(numbers) - 1:
   print("Index Not Found")
else:
   print(f"Number: {numbers[n]}")
