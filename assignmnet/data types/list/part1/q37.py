

l1=[2,2,5,7,9]
l2=[1,2,4,9]

l3=[]

for elem in l1:
    if (elem in l2 ) & (elem not in l3):
        l3.append(elem)
        print(l1)
print(l2)
print(l3)
