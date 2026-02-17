attempts = 1
while True :
    guessing_num = int(input("Enter a number between 1 to 50: "))
    number = 27
    if attempts == 1 :
        print("It is Your First Attempt")
        if guessing_num < number :
            print("Your Guessing number is Too Low ")       
        elif guessing_num > number :
            print("Your Guessing Number is Too High ")      
        elif guessing_num == number :
            print("*****Congratulations you are correct Guess Number !*****")
        else :
            print("Try Again ")
        attempts +=1       
    elif attempts == 2:
        print("It is your Second Attempt ")
        if guessing_num < number :
            print("Your Guessing number is Too Low ")       
        elif guessing_num > number :
            print("Your Guessing Number is Too High ")      
        elif guessing_num == number :
            print("*****Congratulations you are correct Guess Number !*****")
        else :
            print("Try Again ")
        attempts +=1      
    elif attempts == 3 :
        print("*****It is Your Third Attempt*****")
        if guessing_num < number :
            print("Your Guessing number is Too Low ")       
        elif guessing_num > number :
            print("Your Guessing Number is Too High ")      
        elif guessing_num == number :
            print("*****Congratulations you are correct Guess Number , Excellent Choice!!*****")
        else :
            print("Try Again ")
        break
    print()

    

    

    
    

