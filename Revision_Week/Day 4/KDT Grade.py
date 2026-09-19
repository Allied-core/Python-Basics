def Grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks < 60:
        return "F"

marks = int(input("Enter the marks: "))
print(Grade(marks))
