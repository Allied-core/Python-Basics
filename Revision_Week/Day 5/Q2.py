import string

word = input("Enter your Password: ")

if word == "":
   print("Empty Input.")

else:
    letter = 0
    lowercase = 0
    uppercase = 0
    digit = 0

    for item in word:
       if item in string.ascii_uppercase:
          uppercase += 1
       elif item in string.ascii_lowercase:
          lowercase += 1
       elif item in string.digits:
          digit += 1

    letter = uppercase + lowercase

    if letter >= 8 and uppercase >= 1 and digit >= 1:
           print("Strong Password.")
    else:
           print("Weak Password.")
