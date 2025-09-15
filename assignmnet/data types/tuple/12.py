
# you cant remove element from tuple
# caz tuple is immutable

t1=(1,2,3,5)
n=t1.index(3)
print(t1[:n]+t1[n+1:])

############

l1=list(t1)
l1.remove(3)
t2=tuple(l1)
print(t2)
