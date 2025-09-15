
l1=[1,4,2,2,1,6,1]
print(l1)
l2=[]

for elem in l1:
    if elem not in l2:
        l2.append(elem)

for elem in l2:
    print("Count of ",elem,"i",l1.count(elem))
