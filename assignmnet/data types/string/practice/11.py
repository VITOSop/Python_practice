s1=input("Enter no:")

l1=list(s1)
i=1
while i<len(l1):
    if(i%2!=0):
        l1.remove(l1[i])
    i+=1
s2="".join(l1)
print(s2)
