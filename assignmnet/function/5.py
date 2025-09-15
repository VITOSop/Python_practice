
def fact(n):
    fact=1
    i=n
    while i>0:
        fact=fact*i
        i-=1
    return fact

print(fact(5))
