

d1={1:10,2:20,3:30,4:40}

d2=dict()
d2=sorted(d1.items())
print(d2)  #..................make list not dictionary
d3=dict(sorted(d1.items()))
print(d3)  #.................make dictionary


#to make dictionary ,sorting need to be wrap in dict()


