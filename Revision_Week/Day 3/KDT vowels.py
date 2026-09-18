string = str(input("Enter the sentence: "))

box = []

for vowels in string:
    if 'a' == vowels:
        box.append('a')
        
    elif 'e' == vowels:
        box.append('e')

    elif 'i' == vowels:
        box.append('i')

    elif 'o' == vowels:
        box.append('o')

    elif 'u' == vowels:
        box.append('u')


print(len(box))
