

d={}

for i in range(1,6):
    d[i]=i*i

print(d)
#...........................................................
print(dict(map(lambda x:(x,x*x), range(1,6))))
#..........................................................
print(dict((x , x*x) for x in range(1,6)))
