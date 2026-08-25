import string
import random


chars = string.ascii_letters + string.digits + string.punctuation
users = []
command = ""


def set_admin_pass():
  admin_pass = input("Set a Admin Password: ")
  print("\033[1A\033[2K", end="")
  return admin_pass

admin_pass = set_admin_pass()

def check_admin_pass():
  password = input("Enter Admin Password: ")
  if password == admin_pass:
    return True
  else:
    return False



def check_clone(username):
  for user in users:
    if username == user:
      return True

  else:
    return False

def credential_generator():
  password = ""
  user = input("Enter the user-name: ")
  try:
    length = int(input("Enter the length of password: "))
  except ValueError:
    print("Please enter a number.")
    return
  if length <= 0:
    print("Password length must be greater than 0.")
    return


  for i in range(length):
    password += random.choice(chars)

  if check_clone(user):
    print("Username already exists!")
    return

  users.append({
    user: password
})


  print(" ")
  print(f"User : {user}")
  print(f"Password : {password}")


def show_credential(users):
  if check_admin_pass() == False:
    print("Invalid Credentials!!!!")
  else:
    if len(users) <= 0:
      print(" ")
      print("No users")
      print(" ")
    else:
      print("------------------")
      for user in users:
        print(user)
        print("------------------")


if admin_pass == "":
    set_admin_pass()
while command == "exit":
     print(" ")
     print("Password Generator and Storage")
     print("-------------------")
     print("1.Credential Generator")
     print("2.Show Credential")
     print("TYPE 'exit'  to close the program")
     command = input(">>")
     if command == "1":
        credential_generator()
     elif command == "2":
        show_credential(users)
     elif command == "exit":
        break
     else:
        print("Invalid command")
        continue
