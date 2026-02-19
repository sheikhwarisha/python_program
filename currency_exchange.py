def usd(pkr):
    pk = pkr * 280
    return pk
def euro(pkr):
    pk = pkr * 330
    return pk
def riyal(pkr):
    pk = pkr * 74
    return pk
def ringit(pkr):
    pk = pkr * 71
    return pk
def pound(pkr):
    pk = pkr * 378    
    return pk
def dirham(pkr):
    pk = pkr * 76    
    return pk
print("=" * 50 , "Currency Exchange" , "=" *50)
cur = eval(input("Enter the Amount of Currency you Have :"))
select = input("Which Currency do you exchange with pakistani rupee : \n1. USD \n2. EURO \n3. RIYAL \n4. RINGIT \n5.POUND \n6. DIRHAM \n:")
if select == "1" :
    print(f"Here is your converted Amount in $ USD : {usd(cur)}")
elif select == "2" :
     print(f"Here is your converted Amount in € Euro : {euro(cur)}")
elif select == "3" :
     print(f"Here is your converted Amount in  ﷼ Riyal : {riyal(cur)}")
elif select == "4" :
     print(f"Here is your converted Amount in RM Ringit : {ringit(cur)}")
elif select == "5" :
     print(f"Here is your converted Amount in £ Pound : {pound(cur)}")
elif select == "6" :
     print(f"Here is your converted Amount in د.إ Dirham : {dirham(cur)}")
else :
    print("Invalid Input")
