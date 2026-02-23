def rafay():
    select=input("What you Want to Use? \n1. calc \n2. marksheet \n3. nothing")
    if select=="calc":
        num1=int(input("Enter a number 1:"))
        num2=int(input("Enter a number 2:"))
        print(f"This is Addition:{num1+num2} \nThis is Subtraction:{num1-num2} \nThis is Multiplication:{num1*num2} \nThis is Division:{num1/num2}")
    elif select=="marksheet":
        obtain=int(input("Enter your obtain marks:"))
        total=500
        per=(obtain/total)*100
        if per>=70:
            grade="A+"
        else:
            grade="Fail"
            print(grade)
def store():
    select=int(input("What you Want to  wear clothes types? \n1. Formal \n2. Casual \n3. Party wear"))
    if select == 1 :
        print("Welcome to the Formal Wear and your budget is maximum 3000")
    elif select == 2 :
        print("Welcome to the Casual Wear and your budget is maximum 4500")
    elif select == 3 :
        print("Welcome to the Party Wear and your budget is maximum 9800")
    else :
        print("Invalid input")
def tableprinting():
    num = int(input("Enter a  number of table you want to print : "))
    a = 1
    while a <= 10 :
        print(f"{num} * {a} = {num * a}")
        a = a + 1
        
        
    
    
     

    


        
        
    
    
    
