try:
    a = int(input("a = "))
    if a > 0 :
        print("Positive number")
    elif a < 0 :
        print("Negatie number")
    elif a == 0 :
        print("Zero")

except ValueError:
   print("invalide input!!")
