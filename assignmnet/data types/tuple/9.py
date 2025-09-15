


t1=(1,2,3,3,4,2,6,1,2)
l1=[]
for e1 in t1:
    c=t1.count(e1)
    if (c>=2) and (e1 not in l1):
        l1.append(e1)

print(t1)
for e1 in l1:
        print(e1,t1.count(e1))
