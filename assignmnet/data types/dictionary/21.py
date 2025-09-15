

d={'1':['a','b'],'2':['c','d']} 
l=[] 
for v in d.values():
    l.append(v)    

for i in l[0]: 
    for j in l[1]:
        print(i+j)
