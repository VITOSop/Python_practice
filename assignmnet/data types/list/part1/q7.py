
l1=[1,3,5,3,4]
l2=[]
for i in range(len(l1)):
    if i in l2:
        pass
    else:
        l2.append(l1[i])
print(l1)
print(l2)

#####################

l1=[1,3,4,1,5,3]
l2=[]

for elem in l1:
    if elem in l2:
        pass
    else:
        l2.append(elem)

print(l1)
print(l2)
