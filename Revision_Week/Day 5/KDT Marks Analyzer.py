students = {
    "Amit": 78,
    "Rahul": 91,
    "Priya": 65,
    "Sneha": 88
}

highest = max(students, key=students.get)
lowest = min(students, key=students.get)
print(f"Highest Scorer: {highest}")
print(f"Lowest Scorer: {lowest}")

average = sum(students.values()) / len(students)
print(f"Average: {average}")

total = 0
passed = 0
failed = 0
for name, marks in students.items():
    total += marks
    if not highest or marks > students[highest]:
        highest = name
    if not lowest or marks < students[lowest]:
        lowest = name
    if marks >= 70:
        passed += 1
    else:
        failed += 1
print(f"Passed: {passed}")
print(f"Failed: {failed}")
