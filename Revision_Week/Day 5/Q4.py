students = { "Amit": 78, "Rahul": 91, "Priya": 65, "Sneha": 88 }
names = []
marks = []


for name in students:
    names.append(name)

for name in names:
    marks.append(students[name])

Li = marks.index(max(marks))
Si = marks.index(min(marks))

avg = sum(marks)/len(marks)

Pn = 0
Fn = 0

for mark in marks:
    if mark >= 50:
       Pn += 1
    else:
       Fn += 1

print("---------------------")
print("       Report")
print("---------------------")
print(f"Highest Scorer : {names[Li]}")
print(f"Lowest Scorer : {names[Si]}")
print(f"Average Score : {avg}")
print(f"Number Passed : {Pn}")
print(f"Number Failed : {Fn}")
print("---------------------")
