

l1=[1,4,7,8]
l2=[2,5,7,23]

sum=0
for i in range(len(l1)):
    val=l2[i]-l1[i]
    sum=sum+val
print(sum)
