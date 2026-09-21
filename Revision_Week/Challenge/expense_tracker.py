def add_expense():
    temp = []
    n = int(input("Number of products: "))

    for i in range(0,n):
          print("---------------------")
          name = input("Name: ")
          price = int(input("Price: "))
          category = input("Category: ")
          print("---------------------")
          temp.append(f"{name} {price} {category} \n")

    with open("expenses.txt","a") as f:
         f.writelines(temp)

def view_expense():
    temp = []

    with open("expenses.txt","r") as f:
         temp = f.readlines()
    print("---------------------")
    print("   Expense List")
    print("---------------------")

    for item in temp:
         line = item.split(" ")
         print(f"Name: {line[0]}")
         print(f"Price: {int(line[1])}")
         print(f"Category: {line[2]}")
         print("---------------------")

def total():
    temp = []
    category = []
    price = []
    sum = 0
    total = 0

    with open("expenses.txt","r") as f:
         temp = f.readlines()

    for item in temp:
         line = item.split(" ")
         if line[2] not in category:
                category.append(line[2])
     
    print("---------------------")
    print("     Total List")
    print("---------------------")
    for name in category:
         for item in temp:
             line = item.split(" ")
             if name == line[2]:
                    sum += int(line[1])
         print(name,":",sum)
         total += sum
         sum = 0
    print("---------------------")
    print(f"Total: {total}")
    print("---------------------")



while True:
    print("---------------------")
    print("  Expense Tracker")
    print("---------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("TYPE 'exit' to Exit.")
    cmd = input("Enter your choice: ")

    if cmd == "1":
       add_expense()
    elif cmd == "2":
       view_expense()
    elif cmd == "3":
       total()
    elif cmd == "exit":
       print("Closing...")
       break
    else:
       print("Invalid Command")
