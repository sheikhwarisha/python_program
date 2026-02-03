print("Welcome to the AI Restaurant")
name = input("Enter your name :")
budget = eval(input("Enter your Budget :"))
csne = int(input(f"Dear {name} \n Select any oe from Below \n1. Pakistani \n2. Chinese \n3. Italian \n4. Korean \n5. Thai \n6. Don't Know , Suggest something special"))
if csne == 1 :
    print("Welcome to the Pakistani Cuisine")
    if budget >= 10000 :
      fav = int(input(f"Dear {name} , /n What you like the most normal days ? \n1. Biryani \n2. Karahi \n3. Creamy Hand \n4. BBQ \n5. All of the above!"))
      if fav == 1 :
        bill = 8500 
        print(f" Dear {name} , \nHave your Special Madni Platter with special dumphukht !along with jumbo Drink  + 4 Yakhni bowls + Raita + Special Salad . Your Total Bill is Rs .8500/- (Including Text)")
        r_amount = budget - bill 
        meetha = int(input(f" Dear {name}, Do you want sweet ? as the remaining amount is {r_amount} /n1. Kunafa /n2. "))
        if meetha ==1 :
            bill2 =500
            print(f"Here is your sweet (Kunafah) \nYour Total bill is {bill2 + bill} \nHere your Remaining Account {r_amount -bill2} ")
        elif meetha == 2 :
            bill2 = 1000
            print(f"Here is your sweet (Choclate Tart) \nYour Total bill is {bill2 + bill} \nHere your Remaining Account {r_amount}")
        elif meetha == 3 :    
            bill2 = 1000
            print(f"Here is the recommended Sweet (Kunafah Chocolate) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
        else :
            print(f" Your Total Bill is {bill} and Remaining Amount is {r_amount}")
              
        elif fav ==2:
             bill=9000
             r_amount = budget - bill
             print(f"Dear {name}, \nHave your Shinwari Karahi with Shamas Special Brain Masala! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
             meetha = int(input(f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Lava chocolate with premim Ice Cream \n2. Brownie \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1200:
                          print(f"Here is Your Sweet (Lava chocolate with premim Ice Cream) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 1500:
                          print(f"Here is Your Sweet (Brownie) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 2000:
                          print(f"Here is the recommended Sweet (Cheese Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
           elif fav == 3 :
               bill = 9500
               r_amount = budget - bill
               print(f"Dear {name}, \nHave your Shinwari Karahi with Shamas Special Brain Masala! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
               meetha = int(input(f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Ice Cake \n2. Three Milk Cake \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1500:
                          print(f"Here is Your Sweet (Lava chocolate with premim Ice Cream) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 2000:
                          print(f"Here is Your Sweet (Brownie) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 3000:
                          print(f"Here is the recommended Sweet (Cheese Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")                 
           elif fav == 5 :
               bill = 20000
               r_amount = budget - bill
               print(f"Dear {name}, \nYour Special Family Platter with special mutton dhumpukht and BBQ Platter ! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
               meetha = int(input(f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Ice Cake \n2. Three Milk Cake \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1000:
                          print(f"Here is Your Sweet () \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 700:
                          print(f"Here is Your Sweet (Brownie) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 1500:
                          print(f"Here is the recommended Sweet (Cheese Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")                 

               
      else :
    elif budget
    
    else:
else :        
           

            