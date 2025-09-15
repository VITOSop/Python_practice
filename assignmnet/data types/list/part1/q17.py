
l1=[]
n=int(input("Enter no of terms in list:"))

for i in range(n):
    a=int(input("Enter no:"))
    l1.append(a)

print(l1)

t=True
for elem in l1:
    i=2
    while i<=elem/2:
        if(elem==0)|(elem==1)|(elem%i==0):
            t=False
            break
        i+=1
    if t==False:
        break

if t==True:
    print("Prime")
else:
    print("Not prime")
