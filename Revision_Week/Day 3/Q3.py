numbers = [12, 45, 7, 89, 23]
temp = numbers[0]

for item in numbers:
    if temp < item:
       temp = item
print(temp)
