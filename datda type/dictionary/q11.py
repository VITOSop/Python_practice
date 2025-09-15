
d1={1:3,2:400,3:"abc",4:3.3,5:0.5,6:(1,2,3)}

prod=1
for num in d1.values:
    if (type(num)==type(1)) or (type(num)==type(2.2)):
#   if (isinstance(num,int)) or (isinstance(num,float))
        prod=prod*num
print(prod)
