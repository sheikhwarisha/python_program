# Nested Decisions in python
# Multi Descisions program
print("\t****Welcome to Netflix****")
name = input("Enter Your Name :")
email = input("Enter Your Email :")
password = input("Enter Your password :")
age = int(input("Enter Your Age :"))
if age >= 18 :
    print(f"Dear {name} , Welcome to netflix !")
    if email == "rafayshaikh633@gmail.com" and password == "Admin123" :
       print(f"Dear {name} , Welcome to the Netflix Session , Please Select Category")
    elif email == "shamas@gmail.com" and password == "Shamas123" :
       print(f"Dear {name} , Welcome to the Netflix Session , Please Select Category")
    elif email == "warisha@gmail.com" and password == "warisha123" :
       print(f"Dear {name} , Welcome to the Netflix Session , Please Select Category")
    elif email == "safia@gmail.com" and password == "safia123" :
       print(f"Dear {name} , Welcome to the Netflix Session , Please Select Category")
    elif email == "kulsoom@gmail.com" and password == "kulsoom123" :
        print(f"Dear {name} , Welcome to the Netflix Session , Please Select Category")
    else :
        print(f"Dear {name} , Your Login Credentials are invalid !")

else :
    print(f"Dear {name} , Please watch pogo")