transactions = [
    ("salary",10000,"1/05/2026","income"),
    ("car",500,"2/05/2026","expense"),
    ("groceries",300,"2/05/2026","expense"),
    ("rent",1000,"10/05/2026","expense"),
    ("fees",800,"8/05/2026","expense"),
    ("clothes",100,"17/05/2026","expense"),
    ("other",200,"12/05/2026","expense"),
    ("rent",1000,"5/06/2026","expense"),
    ("car",50,"2/06/2026","expense")   
]

def add_income():
    print(" ")
    category = input("Category: ")
    amount = int(input("Amount: "))
    date = input("Date: ")
    transactions.append(
    (category,amount,date,"income")
    )

def add_expense():
    print(" ")
    category = input("Category: ")
    amount = int(input("Amount: "))
    date = input("Date: ")
    transactions.append(
    (category,amount,date,"expense")
    )

def total_expense():
    total = 0
    for transaction in transactions:
        if transaction[3] == "expense":
            total += transaction[1]
    return total

def total_income():
    total = 0
    for transaction in transactions:
        if transaction[3] == "income":
            total += transaction[1]
    return total
    
def check_overspending():
        expense = total_expense()
        income = total_income()
        if (income - expense) >=0:
            print("Flase")
            return False
        else:
            return True

def current_income():
        expense = total_expense()
        income = total_income()
        current = income - expense
        return current
    

def category_date(month):
    print(" ")
    print("--Date--   --Amount--  --Category--")
    for transaction in transactions:
         date = transaction[2].split("/")
         if transaction[3] == "expense":
             if date[1] == month and transaction[1] >=100 and transaction[1] < 1000:
                 print(f"{transaction[2]}    -{transaction[1]}         {transaction[0]}")
             if date[1] == month and transaction[1] < 100:
                 print(f"{transaction[2]}    -{transaction[1]}          {transaction[0]}")
             if date[1] == month and transaction[1] >= 1000:
                 print(f"{transaction[2]}    -{transaction[1]}        {transaction[0]}")
         if transaction[3] == "income":
             if date[1] == month and transaction[1] >=100 and transaction[1] < 1000:
                 print(f"{transaction[2]}    +{transaction[1]}         {transaction[0]}")
             if date[1] == month and transaction[1] < 100:
                 print(f"{transaction[2]}    +{transaction[1]}          {transaction[0]}")
             if date[1] == month and transaction[1] >= 1000:
                 print(f"{transaction[2]}    +{transaction[1]}        {transaction[0]}")                 
                 
def category_expense():
    print(" ")
    print("--Date--   --Amount--  --Category--")    
    for transaction in transactions:
         if transaction[3] == "expense":
             if transaction[1] >=100 and transaction[1] < 1000:
                 print(f"{transaction[2]}    -{transaction[1]}         {transaction[0]}")
             if transaction[1] < 100:
                 print(f"{transaction[2]}    -{transaction[1]}          {transaction[0]}")
             if transaction[1] >= 1000:
                 print(f"{transaction[2]}    -{transaction[1]}        {transaction[0]}")
    
def category_income():
    print(" ")
    print("--Date--   --Amount--  --Category--")    
    for transaction in transactions:
         if transaction[3] == "income":
             if transaction[1] >=100 and transaction[1] < 1000:
                 print(f"{transaction[2]}    +{transaction[1]}         {transaction[0]}")
             if transaction[1] < 100:
                 print(f"{transaction[2]}    +{transaction[1]}          {transaction[0]}")
             if transaction[1] >= 1000:
                 print(f"{transaction[2]}    +{transaction[1]}        {transaction[0]}")
    
            
def display_transaction():   
     print(" ")
     print("--Date--   --Amount--  --Category--")    
     for transaction in transactions:
         if transaction[3] == "expense":
             if transaction[1] >=100 and transaction[1] < 1000:
                 print(f"{transaction[2]}    -{transaction[1]}         {transaction[0]}")
             if transaction[1] < 100:
                 print(f"{transaction[2]}    -{transaction[1]}          {transaction[0]}")
             if transaction[1] >= 1000:
                 print(f"{transaction[2]}    -{transaction[1]}        {transaction[0]}")
         if transaction[3] == "income":
             if transaction[1] >=100 and transaction[1] < 1000:
                 print(f"{transaction[2]}    +{transaction[1]}         {transaction[0]}")
             if transaction[1] < 100:
                 print(f"{transaction[2]}    +{transaction[1]}          {transaction[0]}")
             if transaction[1] >= 1000:
                 print(f"{transaction[2]}    +{transaction[1]}        {transaction[0]}")                 
                 
command = ""                 
                 
while True :
    print(" ")
    print("Expense Manager")
    print("-----------------")
    print("1.Add Income")
    print("2.Add Expense")
    print("3.Categorized Transaction History")
    print("4.Show Current Balance")
    print("5.Show Transaction History")
    print("6.Show Total Income")
    print("7.Show Total Expense")
    print("8.Check OverSpending")
    print("TYPE 'exit' TO EXIT")
    command = input(">>")
    if command == "1":
        add_income()
        continue
    if command == "2":
        add_expense()
        continue
    if command == "3":
        print(" ")
        category = input("Select Category(date,income,expense): ")
        if category == "date":
            print(" ")
            category_date(input("Enter the month:"))
            continue
        if category == "income":
            print(" ")
            category_income()
            continue
        if category == "expense":
            print(" ")
            category_expense()
            continue
        else:
            print("Invalid Category.")
        continue
    if command == "4":
        print(" ")
        print(f"Current Balance: {current_income()}")
        continue
    if command == "5":
        display_transaction()
        continue
    if command == "6":
        print(" ")
        print(f"Total Income: {total_income()}")
        continue
    if command == "7":
        print(" ")
        print(f"Total Expense: {total_expense()}")
        continue
    if command == "8":
        print(" ")
        print(f"Is OverSpending: {check_overspending()}")
        continue
    if command == "exit":
        print("Shutting Down...")
        break
    else:
        print("Invalid Command.")
    

