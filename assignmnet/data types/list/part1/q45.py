
l1=[]
l2=[]
l3=[]
num=int(input("Enter no of terms:"))

for i in range(num):
    a=int(input("Enter no:"))
    l1.append(a)

print("L1",l1)

for elem in l1:
    if elem not in l2:
        l2.append(elem)

print("L2",l2)
l2.sort()
print("L3",l2)
