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

while True :
	user_id = input("Enter your user ID :")
	password = input("Enter your Password :")
	if (user_id == "123" or user_id == "1234" or user_id == "000") and (password == "abcd") :
		print("Welcome to the System :")
		break 
	else :
		print("This is a wrong password or user name .")
		rerun = input("Do you want to try Again ?").lower()
		if rerun ==  "no" :
			break
		else :
			print("Ok !")
			continue 
			
	
	
	
