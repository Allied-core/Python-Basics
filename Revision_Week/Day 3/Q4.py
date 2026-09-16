numbers = [10, 15, 22, 31, 44, 57, 60]
count = 0

for item in numbers:
    if (item % 2) == 0:
        count += 1

print(f"Even Number Count : {count}")
