

d1={1:10,2:20}
d2={3:30,4:40}

d3=d1 | d2
print(d3)


print(dict(list(d1.items())+list(d2.items())))
