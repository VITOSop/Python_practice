
l1=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(l1)):    
    
    if (i!=l1[-3]):
        li=l1[i:i+3]
        print(li) 
    else:
        break
