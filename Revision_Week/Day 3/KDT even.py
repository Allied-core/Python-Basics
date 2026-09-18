numbers = [10, 15, 22, 31, 44, 57, 60]
even = []
for selected in numbers:
    if selected % 2 == 0:
        even.append(selected)

print(len(even))        
