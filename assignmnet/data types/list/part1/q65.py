

l1=[1,2,8,0,7,0,3,0,8]
l2=[]

for e1 in l1:
    if(e1==0):
        l1.remove(e1)
        l2.append(e1)

print(l1)
print(l2)

for e2 in l2:
    l1.append(e2)
print(l1)
