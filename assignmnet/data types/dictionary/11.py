d1={1:4,2:2.2,3:"a",4:6}

l1=list(d1.values())
print(l1)
mul=1
for e1 in l1:
    if type(e1)==int or type(e1)==float:
        mul=mul*e1
    else:
        pass


print(mul)
#...........................................

result=1

for value in d1.values():
    if type(value)==int or type(value)==float:
        result*=value

print(result)
