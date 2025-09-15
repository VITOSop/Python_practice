
l1=[10,20,30,40]
l2=[10,20]
#x,y=l1  will give error

# using *() is flexible ,can be use anywhere
a,*b,c=l1
x,*y,z=l2
print(a,b,c)
print(x,y,z)

# but cant use multiple *() at single time
#*a,*b,c=l1

