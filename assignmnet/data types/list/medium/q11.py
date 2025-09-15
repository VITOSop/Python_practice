
num=int(input("Enter no:"))
l1=[]
i=0
while num>0:
    digit=num%10
    num=num//10
    l1.append(digit)
    i+=1
print(l1)

l1.sort()
l2=[]

for e1 in l1:
    l2.append(str(e1))

print(l2)
print("Min no is:","".join(l2))

l3=l2[::-1]
print("Max no:","".join(l3))

