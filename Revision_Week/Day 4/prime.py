def prime(number):#Hint: Check whether the number is divisible by numbers between 2 and the number before it.

    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True
        
number = int(input("Enter the number: ")) 
print(prime(number))   
