
l1=[]
l2=[]
for i in range(150,250,2):
    l1.append(i)
print("L1:",l1)
print("Length-",len(l1))

for e1 in l1:
    if(e1%4==0):
        l2.append(e1)
print("L2:",l2)
