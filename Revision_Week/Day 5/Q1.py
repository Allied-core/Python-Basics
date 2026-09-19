numbers = []

for i in range(0,2):
    try:
       a = int(input("Enter the Number: "))
    except:
       print("Invalid Input")
    numbers.append(a)

def evenc():
    count = 0
    for item in numbers:
        if item % 2 == 0:
           count += 1
    return count

def oddc():
    count = 0
    for item in numbers:
        if item % 2 > 0:
           count += 1
    return count


print(f"Largest : {max(numbers)}")
print(f"Smallest : {min(numbers)}")
print(f"Sum : {sum(numbers)}")
print(f"Average : {sum(numbers)/len(numbers)}")
print(f"Even_Count : {evenc()}")
print(f"Odd_Count : {oddc()}")
