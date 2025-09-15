
l1=[(2,9),(3,0)]
l2=[]
l3=[]

for e1 in l1:
    l2.append(e1[0])
    l3.append(e1[1])
print("l2",l2,"l3",l3)

l4=[]
for e1 in l1:
    s1=str(e1[0])+str(e1[1])
    l4.append(s1)
print(l4)
