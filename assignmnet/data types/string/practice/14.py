
s1=input("Enter string seperated by comma:")

l1=s1.split(",")
print(l1)
l2=[]
for e1 in l1:
    if e1 not in l2:
        l2.append(e1)


print(l2)
