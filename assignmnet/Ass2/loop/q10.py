import math

x=int(input("Input value of x:"))
n=int(input("Input value of n:"))

sum=0
for i in range(n):
    num=(pow(x,(2*i+1))*pow(-1,i))
    sum+=num
    print(num)
print("Sum is :",sum)
