try:
    num = int(input("Enter the number: "))
except:
    print("Invalid Input.")

n = len(str(num))
snum = str(num)
temp = []

for i in range(1,n+1):
    temp.append(snum[n-i])


rnum = "".join(temp)

print(f"Reversed number : {rnum}")
