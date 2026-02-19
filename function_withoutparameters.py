def calc():
    num1 = eval(input("Enter No 1 :"))
    num2 = eval(input("Enter No 2 : "))
    select = input("What you want ? \n1. Addition \n2. Subtraction \n3. Division \n4. Multiplication \n:")
    if select == "1":
        cal=num1 + num2
    elif select == "2":
        cal=num1 - num2
    elif select == "3":
        cal=num1 / num2
    elif select == "4":
        cal=num1 * num2
    else :
        cal = "Wrong Input!"
    return print(cal)
calc()
    
        