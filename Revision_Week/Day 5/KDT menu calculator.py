from sys import stdin
print("X = ", end= '', flush= True)
x = int(stdin.readline())
print("Y = ", end= '', flush= True)
y = int(stdin.readline())

def add():
    return x + y

def sub():
    return x - y

def mul():
    return x * y


def div():
    return x / y

#menu
while True:
    print("\n ")
    print("\n Calculator")
    print("---------------")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
   
    print("exit or EXIT")

    command = input(">>")

    if command == "1":
        print(add())

    elif command == "2":
        print(sub())

    elif command == "3":
        print(mul())

    elif command == "4":
        print(div())

    elif command == "exit" :
        print("\n EXITED FROM CALCULATOR!!\n")
        break
    else:
        print("INVALID command!!")
