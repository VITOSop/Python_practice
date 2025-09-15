

l1=[0,1,2,3,4,5]

print(l1)

i=0
while i<len(l1):
    temp=l1[i]
    l1[i]=l1[i+1]
    l1[i+1]=temp
    
    i+=2
print(l1)
