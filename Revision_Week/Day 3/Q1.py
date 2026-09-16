string = input("Enter the String: ")
vowel = ["a","e","i","o","u"]

count = 0

for chr in string:
    if chr in vowel:
        count += 1

print(f"Vowel count: {count}")
