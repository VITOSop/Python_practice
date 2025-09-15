
import itertools

l1=[1,2,3]

perms=list(itertools.permutations(l1))
print(perms)
print("All permutations:")
for p in perms:
    print(p)
