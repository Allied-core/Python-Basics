import random
import sys 
from sys import stdin 

while True:
    try:
        print("Enter the initial number of the range: " , end='', flush = True)
        start = int(stdin.readline())

        if start > 0 :
            break
        print("ERROR: Number must be positive")
    except ValueError:
        print("your input is invalid,Enter new input: ")

while True:
    try:
        print("Enter the last number of the range: ", end='', flush=True)
        last = int(stdin.readline())

        if last >= start :
            break
        print("ERROR: The last number must be greater that starting number")
    except ValueError:
        print("your input is invalid,Enter new input: ")

print(f"you entered the range between {start} to {last}")

number = random.randint(start, last)

while True:
    try:
        print("Please Enter your guessing number:", end='', flush = True)
        guess = int(stdin.readline())
            
        if start > guess or last < guess :
            print(f"Your guessed number is must be in the range between {start} to {last}")

        else:
            break
    except ValueError:
        print("your input is invalid , please enter the input!!")

guesses = 1
#loop
while number != guess:
    if number > guess:
        print(f"HINT: HIGHER — between {guess} and {last}")
    elif guess > number:
        print(f"HINT: LOWER — between {start} and {guess}")

    while True:
        guesses += 1
        print(f"Guess #{guesses}: ", end='', flush=True)
        try:
            guess = int(stdin.readline())
            if start <= guess <= last:
                break
            else:
                print(f"ERROR: Must be between {start} and {last}")
        except ValueError:
            print("ERROR: Invalid input, enter a valid integer.")

print(f"Congrats!! You got it in {guesses} guesses.")   
