# num = int(input("Enter a number of table you want to print :"))
# a = 1 
# while a <= 10 :
# 	print(f"{num} * {a} = {num * a}")
# 	a = a + 1

# num = int(input("Enter a number of table you want to print :"))
# a = 10 
# while a >= 1 :
# 	print(f"{num} * {a} = {num *  a}")
# 	a = a - 1

# while True :
# 	user_id = input("Enter your user ID :")
# 	password = input("Enter your Password :")
# 	if (user_id == "123" or user_id == "1234" or user_id == "000") and (password == "abcd") :
# 		print("Welcome to the System :")
# 		break 
# 	else :
# 		print("This is a wrong password or user name .")
# 		rerun = input("Do you want to try Again ?").lower()
# 		if rerun ==  "no" :
# 			break
# 		else :
# 			print("Ok !")
# 			continue 
			
control=True
while control:
    card=int(input("Insert your Card: \n1. Card inserted \n2. Card error : "))
    if card==1:
        chance=3
        while chance>=0:
            pin=int(input("Enter Your Pin to proceed:"))
            if pin==1234:
                control=False
                print("Welcome to the ATM")
                balance = 50000
                select = input("Select any option \n1. Fast Cash \n2. Cash withdrwal \n3. Balance Inquiry \n4. Type anything for exit \nSelect Any Above")
                if select == 1 :
                    print("Proceeding to Fast Cash")
                elif select == 2:
                    print("Proceeding to Cash Withdrawl")
                elif select == 3 :
                    print("Proceeding to Balance Inquiry")
                else :
                    print("Exiting")
                
                break
            else:
                print(f"you have {chance} chances left! ")
                chance=chance-1
                continue
        else:
            print("Card has been captured!")
            break
        
    else:
        print("Card Error")
        rerun=int(input("Do you want to insert card again? \n1. yes \n2. NO:"))
        if rerun==1:
            continue
        else:
            print("Thank you for visiting us!")
            break
        

              

            
