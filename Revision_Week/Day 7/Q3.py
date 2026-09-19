fname = input("Enter the file_name: ")

try:
   with open(fname,"r") as f:
        data = f.read()
except:
   print("File Not Found.")
