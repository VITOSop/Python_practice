

def prime(n):     
    i=2   
    while i<=n//2:    
        if(n%i==0):
            return 0
            break
        i+=1
    else:          
        return 1     
n=int(input("Enter no"))
print(prime(n))         
