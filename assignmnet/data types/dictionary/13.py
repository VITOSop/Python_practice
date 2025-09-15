

l1=[1,2,3,4]
l2=["one","two","three","four"]

#....for equal length
d1=dict(zip(l1,l2))
print(d1)

#....for unequal length
d2=dict()
for i in range(len(l1)):
    d2[l1[i]]=l2[i]

print(d2)

