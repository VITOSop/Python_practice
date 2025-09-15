
l1=[1,3,5,7,9,10]
l2=[2,4,6,8]
l3=l1[::]
for i in l3:
   if(i==l1[-1]):
        l3.remove(i)
        for j in l2:
           l3.append(j)
print(l1)
print(l2)
print(l3) 
