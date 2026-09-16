string = input("Enter the String: ")
temp = []
n = len(string)

for i in range(1,n+1):
    temp.append(string[n-i])
   
rstring = "".join(temp)

print(rstring)
