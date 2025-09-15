

yr=int(input("Enter year:"))

if(yr%4==0):
    if(yr%100==0):
        if(yr%400==0):
            print("Leap year !")
        else:
            print("Not leap year !")
    else:
        print("Leap year !")
else:
    print("Not leap year !")


for i in range(2000,2100):
    if((i%4==0) and (i%100!=0)) or (i%400==0):
        print(i,"Leap")
    else:
        print(i,"Not leap")
