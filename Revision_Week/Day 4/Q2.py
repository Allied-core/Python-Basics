string = "apple banana apple mango banana apple"
temp = string.split(" ")

uniq = []

count = 0

for item in temp:
    if item not in uniq:
        uniq.append(item)

for uitem in uniq:
     for item in temp:
         if uitem == item:
            count += 1
     print(uitem,count)
     count = 0
