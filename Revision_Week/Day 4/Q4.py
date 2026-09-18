num = int(input("Enter the Number: "))

def check(num):
    count = 0
    for i in range(2, num):
         if num % i == 0:
              count += 1

    if count == 0:
        print("is_Prime")
    else:
        print("Not_Prime")

check(num)
