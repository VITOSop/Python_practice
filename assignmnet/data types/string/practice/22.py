

s1=input("Enter string:")
l1=s1.split(" ")
#print(sorted(s2))
n=len(l1)
for i in range(n):
    for j in range(0,n-(i+1)):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1]+l1[j]

res=''.join(l1)
print(s1)
print(res)
