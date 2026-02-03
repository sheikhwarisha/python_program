# Assignment
totalclasses = int(input("Enter Total number of classes :"))
no_class_att =  int(input("Enter Number of Classes Attend (Only 5 Absent are Allowed) :"))
medical_cer = input("Do You Have Medical Certificate ?(Yes / No):").lower()
if totalclasses == 30 :
    if no_class_att >= 25 and medical_cer == "no":
        print("You Are Allowed to Sit in the Exam ")
    elif no_class_att >= 25 and medical_cer == "yes" :
        print("You have Extra Special Permission Because you have Medical Certificate ")
    else :
        print("You are not Allowed to Sit in the Exam ")
elif totalclasses == 40 :
    if no_class_att >= 35 and medical_cer == "no":
        print("You Are Allowed to Sit in the Exam ")
    elif no_class_att >= 35 and medical_cer == "yes" :
        print("You have Extra Special Permission Because you have Medical Certificate ")
    else :
        print("You are not Allowed to Sit in the Exam ")
elif totalclasses == 50 :
    if no_class_att >= 45 and medical_cer == "no":
        print("You Are Allowed to Sit in the Exam ")
    elif no_class_att >= 45 and medical_cer == "yes" :
        print("You have Extra Special Permission Because you have Medical Certificate ")
    else :
        print("You are not Allowed to Sit in the Exam ")
else :
    print(" Try Again !")

