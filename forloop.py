# i =0
# while i <= 10:
#     for j in range(1,5):
#         print(f"{i} , {j}")
#         i +=1
#         
# for i in range(5):
#     for j in range(i+1):
#         print("*" , end="#") #end method used for horizontally printing
#     print()

for i in range(1,6):
    for j in range(1,i*3,2):
        print(j,end="")
    print()