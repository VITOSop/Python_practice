
n=int(input("Enter no:"))

for lno in range(1,(n//2)+2):
    print(" "*(n-((2*lno)-1)) + "*"*(2*(lno)-1))

for nst in range((n//2)+1,0,-2):
    print(" "*(n-nst)+"*"*nst)

