
def unique_list(l1):
    l2=[]
    for e1 in l1:
        if  e1 not in l2:
            l2.append(e1) 
    
    return l2

l1=[1,2,3,3,3,3,4,5]
print(unique_list(l1))
