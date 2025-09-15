

d1={1:10,2:20,3:10,4:40,5:20}
d2=dict()
for key,values in d1.items():
    if values not in d2.values():
        d2[key]=values
    else:
        pass
print(d2)


#........................

