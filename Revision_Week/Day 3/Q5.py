numbers = [1, 2, 2, 3, 4, 4, 5, 1]
new = []

for item in numbers:
   if item not in new:  
        new.append(item)

print(new)
