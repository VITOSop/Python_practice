
num=int(input("Enter no:"))

sum=0
for i in range(1,num):
    if(i%2!=0):
        print(i)
        sum=sum+i

print("Sum is:",sum)


###########################################

num=int(input("Enter no:"))

i=1
sum=0
while i<=num:
    if(i%2!=0):
        print(i)
        sum+=i
    i+=1
print("Sum is:",sum)

