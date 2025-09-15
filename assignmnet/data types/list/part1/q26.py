
l1=[1,2,3,4]
l2=[2,3,4,1]


if len(l1)!=len(l2):
    print("Not circularly identical.")
else:
    temp=l1+l1
    found=False
    for i in range(len(l1)):
        if temp[i:i+len(l1)]==l2:
            found=True
            break

if found:
    print("Circularly identical.")
else:
    print("Not circularly identical.")

