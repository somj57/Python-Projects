addition = lambda a,b: a+b
substraction = lambda a,b: a-b
multliplication = lambda a,b: a*b
division = lambda a,b: a/b

while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = int(input("Enter your choice : "))
    if choice < 1 or choice > 5:
        print("Not a vaid option ")
        continue
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))

    if choice == 1:
        print(addition(num1,num2))
    elif choice == 2:
        print(substraction(num1,num2))
    elif choice == 3:
        print(multliplication(num1,num2))
    elif choice == 4:
        if num2 == 0:
            print("Zero Division error")
            continue
        print(division(num1,num2))
    elif choice == 5:
        break
    else:
        print("invalid Choice")