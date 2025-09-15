l1=[100,200,300,400,500]


for i in range(len(l1)):
    if l1[i]>350:
        print(l1[i])
#### Store all no greater than 350 in l2

l2=[]
for i in range(len(l1)):
    if l1[i]>350:
        l2.append(l1[i])
print(l2)

#### using list comprehension

l3=[l1[i] for i in range(len(l1)) if l1[i]>350]
print(l3)

####----------- create new list to store aquare of all elements in l1

l4=[]
for i in range(len(l1)):
        l4.append(l1[i]**2)
print(l4)

l4=[l1[i]**2 for i in range(len(l1))]

print(l4)       


#####-----------

l5=[l1[i] if l1[i]>350 else None for i in range(len(l1))]

print(l5)
