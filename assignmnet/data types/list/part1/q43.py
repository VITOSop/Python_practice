
print("Without slicing...!!!")
l1=[12,23,34,45,56,67]
l2=[]
l3=[]

for i in range(len(l1)):
    if(i<(len(l1)//2)):
        l2.append(l1[i])
    else:
        l3.append(l1[i])

print(l1)
print(l2)
print(l3)

#################################
print("With slicing!!!!")
l1=[12,23,35,45,56,67,99]

l2=l1[:len(l1)//2]
l3=l1[len(l1)//2:]

print(l1)
print(l2)
print(l3)


