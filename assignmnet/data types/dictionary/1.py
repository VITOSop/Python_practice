
d={'three':3,'one':1,'two':2}

d1=dict(sorted(d.items(), key=lambda item:item[1]))
d2=dict(sorted(d.items(), key=lambda item:item[1],reverse=True))
print(d1)
print(d2)
