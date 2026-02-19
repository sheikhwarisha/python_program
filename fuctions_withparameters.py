def calc(num1, num2 , opr):
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
    return print(f"This is {var} of {num1} and {num2} which is : {cal}")
calc(50,100, "/")
calc(40,50, "*")
calc(60,20 , "+")
calc(20,30, "-")
        
    
