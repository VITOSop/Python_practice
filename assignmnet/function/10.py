
def even(l1):
    l2=[]
    for e1 in l1:
        if (e1%2==0):
            l2.append(e1)
    return l2

l=[1,2,3,4,5,6,7,8,9]
print(even(l))
