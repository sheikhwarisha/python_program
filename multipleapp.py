print("***Multiple App Player ***")
select = eval(input("Select an App you want to work : \n1. Calculator \n2. Student Marksheet \n3. Clothing Store \n :"))
if select ==1:
    method = input("What your wanto do ? : \n1. Addition \n2. Subtraction \n3. Division \n4. Mutiply \n:")
    num1 = eval(input("Enter number 1 to proceed:")) 
    num2 = eval(input("Enter number 2 to proceed :")) 
    if method == "1":
      print(f" This is your Addition : {num1+ num2}")
    elif method == "2" :
        print(f"This is your Subtraction : {num1 -num2}")
    elif method == "3" :
        print(f"This is your Division : {num1 /num2}")
    elif method == "4" :
        print(f"This is your Multiply : {num1 * num2}")
    else :
        print("invalid Input")
elif select == 2 :
    name = input("Enter Your Name :")
    islamiat = eval(input("Enter your Marks in Islamiat :"))
    physics = eval(input("Enter Your Marks in Physics :"))
    english = eval(input("Enter Your Marks in English :"))
    urdu = eval(input("Enter Your Marks in Urdu :"))
    maths = eval(input("Enter Your Marks in Maths :"))
    obtain_mark = islamiat + physics + english + urdu + maths
    total = 500
    percentage = (obtain_mark /total)* 100
    if percentage >= 90 and percentage <= 100:
        print(f"Dear {name} , Your Obtain Marks is {obtain_mark} and Percentage is {percentage} , your grade is A++ ")
    elif percentage >= 80 :
        print(f"Dear {name} , Your Obtain Marks is {obtain_mark} and Percentage is {percentage} , your grade is A")
    elif percentage >= 70 :
        print(f"Dear {name} , Your Obtain Marks is {obtain_mark} and Percentage is {percentage} , your grade is  B")
    elif percentage >= 60 :
        print(f"Dear {name} , Your Obtain Marks is {obtain_mark} and Percentage is {percentage} , your gradeis c ")
    else :
         print("Invalid Input ")
elif select == 3 :
    name = input("Enter Your Name :")
    budget = eval(input("Enter your Budget :"))
    if budget >= 1000 and budget <= 2000:
        print(f"Dear {name} , Welcome To the Formal Wear  ")
    elif budget >= 2100 and budget <= 3000 :
        print(f"Dear {name} , Welcome to the Party Wear ")
    elif budget >= 3100 and budget <= 4000 :
        print(f"Dear {name} , Welcome to the Casual Wear ")
    elif budget >= 900 :
        print(f"Dear {name} , Welcome to the BAcha Party Wear ")
    else :
         print("Insufficient Balance  ")

else :
    print("Invalid Input :")