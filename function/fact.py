

def fact(n):
    if n==0:
        print(1)
    else:
        res=1
        for n in range(n,0,-1):
            res*=n
        print(res)


def fact_rec(n):
    if n>0:
        res=n*fact_rec(n-1)
        return res
    else:
        return 1

fact(1000)
fact_rec(100)
