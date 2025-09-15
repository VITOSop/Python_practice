

num=int(input("Enter no:"))

i=0
sum=0
while num>0:
    digit=num%10
    print(digit)
    num=num//10
    sum=sum+digit
    i+=1
print("Sum is:",sum)
