import sys

x,y,z = map(int, input("Enter the values:").split())


try:
    if x > y and x > z:
        print(f"the largest number is {x}")

    elif y > x and y > z:
        print(f"the largest number is {y}")

    elif z > x and z > y:
        print(f"the largest number is {z}")

except ValueError:
    print("Invalid Error!!")
