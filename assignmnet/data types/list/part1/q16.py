

l1=[]
i=1
while i>0:
    sq=i**2
    if(sq<30):
        l1.append(sq)
    else:
        break
    i+=1
print("All square are:",l1)
print("First 5 elements are:",l1[:5])
print("Last 5 elements are:",l1[-1::-1])
