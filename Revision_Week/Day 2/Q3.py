try:
    N = int(input("Enter the number(N): "))
except:
    print("Invalid Input.")

total = 0

for i in range(0,N+1):
    total += i
print(f"Sum of N Numbers:{total}")
