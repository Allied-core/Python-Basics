temp = [
"Rahul 85 \n",

"Amit 72 \n",

"Priya 91 \n",

"Sneha 66 \n"
]

try:
   with open("student.txt","w") as f:
        f.writelines(temp)
except:
   print("Error while opening file.")

try:
   with open("student.txt","r") as f:
        entry = f.readlines()
except:
   print("Error while reading file.")

marks = []

for line in entry:
    D = line.split(" ")
    marks.append(int(D[1]))

Average = sum(marks)/len(marks)
Hm = max(marks)
Lm = min(marks)

print(f"Average : {Average}")
print(f"Highest Marks : {Hm}")
print(f"Lowest Marks : {Lm}")
