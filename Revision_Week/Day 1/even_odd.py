from sys import stdin

print("Enter the number: ", end='', flush=True)
Number = int(stdin.readline())

if Number % 2 == 0:
    print("it is even")

else :
    print("it is odd")
