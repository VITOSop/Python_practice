
def in_range(a,b,c):
    for i in range(b,c):
        if (i==a):
            return True
            break
    else:
        return False    
print(in_range(3,1,5))
