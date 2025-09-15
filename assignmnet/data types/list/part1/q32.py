
l1=[1,2,3,4,5,6]
l2=[3,4,26]

t=True
for elem in l2:
    if elem in l1:
        continue
    else:
        t=False
        break
if t:
    print("Sub list")
else:
    print("Not sub list")
