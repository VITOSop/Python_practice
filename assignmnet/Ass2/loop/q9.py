
import math

x=int(input("Input value of x:"))
n=int(input("Input value of n:"))

sum=0
for i in range(n):
    sum+=pow(x,i)/math.factorial(i)

print(sum)
