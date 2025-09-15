
s1=input("Enter no:")

l1=s1.split(" ")
l2=[]
for e1 in l1:
    if e1 not in l2:
        l2.append(e1)
        print("count of",e1,"is",l1.count(e1))
    else:
        pass
