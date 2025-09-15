
def prime(n):
    if (n==2):
        return True
    else:
        i=2
        while i<=n//2:
            if(n%1==0):
                return False
        else: 
            True

print(prime(9))
