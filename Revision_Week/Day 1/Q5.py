a = float(input("Enter Number1 :"))
b = float(input("Enter Number2 :"))
c = float(input("Enter Number3 :"))

if a>=b and a>= c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c

print("Largest is :", largest) 