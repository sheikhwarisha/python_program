def calc():
    while True :
        num1 = int(input("Enter Number 1 :"))
        num2 = int(input("Enter Number 2 :"))
        opr =input("Enter operator : + , - , / , * :")
        if opr == "+":
            cal=num1 + num2
            var = "Addition"
        elif opr == "-":
            cal=num1 - num2
            var = "Subtraction"      
        elif opr == "/":
            cal=num1 / num2
            var = "Division"
        elif opr == "*":
            cal=num1 * num2
            var = "Multiplication"
        else :
            cal = "Wrong Input"
        print(f"This is {var} of {num1} and {num2} which is : {cal}")
        rerun =input("Do you want to continue ? : (yes/no) :").lower()
        if rerun == "yes" :
            continue
        else :
            break
        print(f"This is {var} of {num1} and {num2} which is : {cal}")    
calc()