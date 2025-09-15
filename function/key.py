def neg(n):
    return -n
def rep(n):
    return 1/n

l1=[1,5,2,99,45]

print(sorted(l1, key=neg)) #sorted(l1, key=(lambda n: 1/n))
print(l1)
print(sorted(l1, key=rep)) #sorted(l1, key=(lambda n: -n))
