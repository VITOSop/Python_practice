'''
Take list,take no from user to be searched in list print found or nor
'''

l1=[21,45,12,11,6,53]
print(l1)
num=int(input("Enter no:"))

if num in l1:
    print("Present")
else:
    print("Absent")

##################################

l1=[21,45,12,11,6,53]

num=int(input("Enter no:"))
i=l1.index(num)

if i != None: # if absent  
    print("Present")
else:
    print("Absent")

##############################

l1=[21,45,12,11,6,53]

num=int(input("Enter no:"))

for i in range(len(l1)):
    if(num==l1[i]):
        print("Present")
        break
else:
    print("Absent")
