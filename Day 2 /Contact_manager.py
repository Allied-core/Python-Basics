import sys
from sys import stdin 

contact_book = [(932544795,"Krishna"),(94207546,"Kishor"),(99212856,"Home"),(21648589,"xrit")] 

def Add_contact():
    Number = []
    print("Enter New Number:", end='', flush=True)
    Number = int(stdin.readline())

    name = []
    print("Enter the name:", end='', flush=True)
    name = str(stdin.readline())

    contact_book.append((Number,name))

    print("Contact Saved.")
    
   
def Update_contact():

    New = input("Enter the name:")
    index = -1
    print(" ")

    for ind, contact in enumerate(contact_book):
        if New == contact[1]:
            index = contact
            print("Details:")
            print(f"name- {contact[1]}")
            print(f"Number- {contact[0]}")
            index = contact_book.index(contact)

        
    if index == -1:
        print("Contact Not found!!")
        print(" ")

        Number=input("Enter the number:")
        name=input("Enter the name:")

        contact_book.append((Number,name))



def Search_contact():

    search =  input("Search contact list:")
    index = -1
    print(" ")

    for ind, contact in enumerate(contact_book):
        if search == contact[1] or search == str(contact[0]):
            index = ind
            print("contact found:")
            print(f"name- {contact[1]}")
            print(f"Number- {contact[0]}")

    if index == -1:
        print("Contact Not Found!!!!")    

def Delete_contact():  

    Deleting = input("Enter number or name to delete: ")   
    index = -1
    print(" ")

    for ind, contact in enumerate(contact_book):
        if contact[1] == Deleting or str(contact[0]) == Deleting :
            index = ind
            print(f"contact deleted- {contact[0], contact[1]}")

    if index == -1:  
        print("Contact Not found.") 

    else:
        contact_book.pop(index)    


def Display():
    print("\n")
    print(" all contact info.")
    for i, contact in enumerate(contact_book):
        print(f"{contact[0]} - {contact[1]}")

   
    #MENU
while True:
    print("\n ")
    print("\n CONTACT MANAGER")
    print("---------------")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Delete Contact")
    print("4.Update Contact")
    print("5.Display All Contact")
    print("exit or EXIT")

    command = input(">>")

    if command == "1":
        Add_contact()

    elif command == "2":
        Search_contact()

    elif command == "3":
        Delete_contact()

    elif command == "4":
        Update_contact()

    elif command == "5":
        Display()

    elif command == "exit" :
        print("\n EXITED FROM CONTACT MANAGER !!\n")
        break
    else:
        print("INVALID command!!")
