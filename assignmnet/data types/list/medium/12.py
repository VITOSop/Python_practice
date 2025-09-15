
num=int(input("Enter no:"))

#l1=list(str(num))....for making string list
l1=[]
l2=[]
i=0
while num>0:
    digit=num%10
    num=num//10
    l1.append(digit)
print(l1)
for e1 in l1:
    if(e1%2!=0):
        l2.append(e1)
print(l2)
