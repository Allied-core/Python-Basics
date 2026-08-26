products = [
    ("book",25,5),
    ("water-bottle",10,0),
    ("bag",50,5),
    ("pen",5,0)   
]

def add_product():
    print(" ")
    name = input("Enter the Product Name: ")
    price = int(input("Enter the Product Price: "))
    quantity = int(input("Enter the Product Quantity: "))
    products.append((name,price,quantity))

def update_product():
    print(" ")
    key = input("Enter the Product Name:")
    index = -1
    print(" ")
    for product in products:
        if key == product[0]:
            print("Product Found:")
            print("-------------")
            print(f"Name: {product[0]}")
            print(f"Price: {product[1]}")
            print(f"Quantity: {product[2]}")
            print("-------------")
            index = products.index(product)
        else:
            continue
    if index == -1 :
        print(" ")
        print("Product Not Found")
    print(" ")
    name = input("Enter the Product Name: ")
    price = int(input("Enter the Product Price: "))
    quantity = int(input("Enter the Product Quantity: "))
    products[index] = (name,price,quantity)
    
def add_stock():
    print(" ")
    key = input("Enter the Product Name:")
    index = -1
    print(" ")
    for product in products:
        if key == product[0]:
            print("Product Found:")
            print("-------------")
            print(f"Name: {product[0]}")
            print(f"Price: {product[1]}")
            print(f"Quantity: {product[2]}")
            print("-------------")
            index = products.index(product)
            quantity = int(input("Enter the quantity:"))
            products[index] = (product[0],product[1],product[2]+quantity)     
        else:
            continue
    print(" ")
    print("Product Not Found")    
   
def remove_product():
    print(" ")
    key = input("Enter the Product Name:")
    index = -1
    print(" ")
    for product in products:
        if key == product[0]:
            print("Product Found:")
            print("-------------")
            print(f"Name: {product[0]}")
            print(f"Price: {product[1]}")
            print(f"Quantity: {product[2]}")
            print("-------------")
            index = products.index(product)
        else:
            continue
    if index == -1 :
        print(" ")
        print("Product Not Found")
    products.remove(products[index]) 
    print(" ")
    print("Product Removed.")    
    
def show_out_of_stock():
    count = 0
    print(" ")
    print("Out of Stock List :")
    print("-------------")
    
    for product in products:
        if product[2] == 0 :
            print(f"Name: {product[0]}")
            print(f"Price: {product[1]}")
            print("-------------")
            count += 1
        else:
            continue
    if count == 0:
        print("None")
        print("-------------")
        
    
  
def search_product():
    print(" ")
    key = input("Enter the Product Name:")
    for product in products:
        if key == product[0]:
            print("Product Found:")
            print("-------------")
            print(f"Name: {product[0]}")
            print(f"Price: {product[1]}")
            print(f"Quantity: {product[2]}")
            print("-------------")
            return
        else:
            continue
    print(" ")
    print("Product Not Found")


def display_products():  
    print(" ")
    print("Products: ")
    print("------------")
    for product in products:
        print(f"Name: {product[0]}")
        print(f"Price: {product[1]}")
        print(f"Quantity: {product[2]}")
        print("-------------")
    
command = ""  
   
while True :
    print(" ")
    print("INVENTORY MANAGEMENT")
    print("-------------")
    print("1.Add Product")
    print("2.Update Product")
    print("3.Remove Product")
    print("4.Search Product")
    print("5.Add Stock")
    print("6.Show Out of Stock Products")
    print("7.Show all Products")
    print("TYPE 'exit' to EXIT ")
    print("-------------")
    command = input(">>")
    
    if command == "1":
        add_product()
    elif command == "2":
        update_product()
    elif command == "3":
        remove_product()
    elif command == "4":
        search_product()
    elif command == "5":
        add_stock()
    elif command == "6":
        show_out_of_stock()
    elif command == "7":
        display_products()
    elif command == "exit":
        print("Shutting Down...")
        break
    else:
        print("Invalid command!")
        
