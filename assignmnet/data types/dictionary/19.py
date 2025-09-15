


d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}

d3={}

for k,v in d1.items():
    if k in d2.keys():
        d3[k]=v+d2[k]
    else:
        d3[k]=v

for k,v in d2.items():
    if k not in d3:
        d3[k]=v

print(d3)

