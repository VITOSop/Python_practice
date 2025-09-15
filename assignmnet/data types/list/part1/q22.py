
l1=[1,2,3,4]

num=int(input("Enter no:"))

for i in range(len(l1)):
    if(num==l1[i]):
        print(i)
        break
    else:
        continue

##############################


num=int(input("Enter no:"))

if num in l1:
    i=l1.index(num)
    print("At index:",i)
else:
    print("Not found")
