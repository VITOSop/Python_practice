
num1=int(input("Enter num 1:"))
num2=int(input("Enter num 2:"))

if(num1==num2):
    print(num1)

elif num1>num2:
    a=num1%num2
    while a>0:
        a=num2%a
    
