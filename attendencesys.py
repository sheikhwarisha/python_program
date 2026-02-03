name = input(("Enter Your Name :"))
t_class = int(input("Enter a number of total Class :"))
a_class = int(input("Enter a number of Attendance :"))
per = (a_class /t_class)*100
if per >= 75 :
    print("You are Allowed to sit in Exam ! No Medical")
elif per>=20 and per < 75 :
    print(f" Dear {name} Your Percentage is below 75 %")
    med_c = int(input("Do You Have Medical Certificate ? : \nPress 1. for Yes \nPress 2. for No \n"))
    if med_c == 1 :
        print("Your Medical Certificate is proceed for verification :")
        ver =int(input("Let me know is it signed and stamped ? \nPress 1. for Yes \nPress 2. for No \n"))
        if ver == 1:
            print(f"Dear {name} , Despite your attendance is low , But your Medical Certificate is verified and you are allowed to sit in the exam ")
        elif ver == 2 :
            print(f"Dear {name} , Despite your attendance is low , But your Medical Certificate is not verified and you are not allowed to sit in the exam ")
        else :
            print("Invalid Input")
    else :
        print("You are not allowed to sit in the exam")
else :
    print("Attendance percentage is very low ! you are not allowed to sit in the exam")