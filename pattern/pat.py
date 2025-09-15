

n=int(input("Enter no of lines:"))

nsp=n-1
for nst in range(1,n+1,2):
    print(" "* nsp +"*"*nst)
    #print(" " * (n-nst)+"*" * nst)
    nsp=nsp-2

nsp=2
for nst in range(n-2,0,-2):
    print(" " *nsp+ "*" *nst)
    nsp=nsp+2
   # print(" "*(n-nst)+"*"*nst)
