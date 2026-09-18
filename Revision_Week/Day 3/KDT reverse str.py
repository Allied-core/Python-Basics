string = str(input("Enter the sentence: "))
new = ''
for slice in string:
    new = slice + new
print(new)
