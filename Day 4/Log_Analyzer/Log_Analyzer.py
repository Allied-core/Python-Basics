Logs =[]
categories = []
try:
    fname = input("Enter File Name: ")
    file = open(fname, "r")
    for line in file:
        Logs.append(line.strip())
except:
    print("Something went wrong.")

else:
    file.close()

    for log in Logs:
        msg = log.split(" ")
        if msg[2] not in categories:
           categories.append(msg[2])

    def category_count(category):
        count = 0
        for log in Logs:
            msg = log.split(" ")
            if msg[2] == category:
               count += 1
        return count

    def search_msg():
        found = False
        msg = input("Message: ")
        print("--------------------------")
        for log in Logs:
            log_msg = log.split(" ")

            output_msg = []
 
            for i in range(3, len(log_msg)):
                output_msg.append(log_msg[i])

            output = " ".join(output_msg)

            if msg == output:
                print(log)
                found = True
        print("--------------------------")
        if found == False:
            print(" ")
            print("Log Not Found !")
            print(" ")
            print("--------------------------")


    def search_date():
        found = False
        msg = input("Date: ")
        print("--------------------------")
        for log in Logs:
            log_msg = log.split(" ")

            if msg == log_msg[0]:
                print(log)
                found = True
        print("--------------------------")
        if found == False:
            print(" ")
            print("Log Not Found !")
            print(" ")
            print("--------------------------")

    def search_time():
        found = False
        msg = input("Time: ")
        print("--------------------------")
        for log in Logs:
            log_msg = log.split(" ")

            if msg == log_msg[1]:
                print(log)
                found = True
        print("--------------------------")
        if found == False:
            print(" ")
            print("Log Not Found !")
            print(" ")
            print("--------------------------")




    def search_category():
        found = False
        msg = input("Category: ")
        print("--------------------------")
        for log in Logs:
            log_msg = log.split(" ")

            if msg == log_msg[2]:
                print(log)
                found = True
        print("--------------------------")
        if found == False:
            print(" ")
            print("Log Not Found !")
            print(" ")
            print("--------------------------")

    def display_log_stats():
        print(" ")
        print("--------------------------")
        print("===== Log statistics =====")
        print("--------------------------")
        print(f"Total entries: {len(Logs)}")
        print("--------------------------")
        for category in categories:
            print(f"{category} : {category_count(category)>
        print("--------------------------")
        for category in categories:
            print(f"{category} Rate : {round((category_cou>
        print("--------------------------")
        print(" ")

    command = ""

    while True:
        print("--------------------------")
        print("===== Log Analyzer =====")
        print("--------------------------")
        print("1.Show Log Stats")
        print("2.Search Log")
        print("TYPE 'exit' TO EXIT")
        print("--------------------------")
        command = input(">>")
        if command == "exit":
           print("Shutting Down...")
           break
        if command == "1":
           display_log_stats()
           continue
        if command == "2":
           print("--------------------------")
           print("===== Search Log =====")
           print("--------------------------")
           print("1.Date")
           print("2.Time")
           print("3.Category")
           print("4.Message")
           print("--------------------------")
           stype = input("Enter Search Type: ")
           if stype == "1":
              search_date()
           if stype == "2":
              search_time()
           if stype == "3":
              search_category()
           if stype == "4":
              search_msg()
           else:
             print("Invalid Search Type.")
        else:
            print("Invalid Command")
