with open("notes.txt","r") as f:
     temp = f.readlines()
     count = 0
     for item in temp:
         word = item.split(" ")
         for item in word:
             if item != "\n":
                count += 1

     print(f"Word Count: {count}")
