
def perfectno(n):      
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    
    if (sum==n):        
        print("Perfect no")
    else:
        print("Not perfect no")

perfectno(6)
