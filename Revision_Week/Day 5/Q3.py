list = []



def add():
   name = input("Name: ")
   price = int(input("Price: "))

   list.append([name,price])


def total():

    temp = []
    for item in list:
            temp.append(item[1])
    price = sum(temp)

    if price >= 1000 :
          discount = price*0.1
    elif price >= 500:
          discount = price*0.05
    else:
          discount = 0

    print("---------------------")
    print("    Total Bill")
    print("---------------------")
    for item in list :
        print(f"   {item[0]} : {item[1]}")
    print("---------------------")
    print(f"Discount : {discount}")

    print(f"Total bill : {price - discount}")

N = int(input("Enter the number of products: "))
for i in range(0,N):
    add()
total()
