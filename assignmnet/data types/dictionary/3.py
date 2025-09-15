
d1={1:10,2:20}
d2={4:40,3:30}
d3={6:60,5:50}


r1=dict()
for d in (d1,d2,d3):
    r1.update(d)
print(r1)

#.................................
r2=d1 | d2 | d3
print(r2)

#...................................

l1=list(d1.items())
l2=list(d2.items())
l3=list(d3.items())

r3=dict(l1+l2+l3)
print(r3,type(l1))
