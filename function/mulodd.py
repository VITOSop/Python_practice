def mulodd(n):
        mul=1
        for i in range(1,n):
            if(i%2!=0):
                mul=mul*i
        print(mul)
def mulodd2():
        res=1
        for i in range(1,100,2):
            res*=i
        print(res)
mulodd(100)
mulodd2()
