with open("log.txt","r") as f:
     lines = f.readlines()
     info = 0
     error = 0
     warning = 0
     for line in lines:
         word = line.split(" ")
         if word[0] == "INFO":
            info += 1
         elif word[0] == "ERROR":
            error += 1
         elif word[0] == "WARNING":
            warning += 1
     print("---------------------")
     print(" Category Count")
     print("---------------------")
     print(f"INFO : {info}")
     print(f"ERROR : {error}")
     print(f"WARNING : {warning}")
