
num=int(input("Enter no:"))
l1=[]
i=0
while num>0:
    digit=num%10
    num=num//10
    l1.append(digit)
    i+=1

print(l1[::-1])
