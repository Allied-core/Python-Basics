numbers = [12, 45, 7, 89, 23]
largest = numbers[0]
for current in numbers:
    if largest < current:
        largest = current
print(largest)        
