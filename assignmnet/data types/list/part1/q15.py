import random

print("Without removing:")
l1=[2,4,5,1]
l2=[]

for elem in l1:
    l2.append(random.choice(l1))

print(l1)
print(l2)

######################################
print("With removing:")

l1=[1,4,6,8]
l2=[]


while l1:
    elem=random.choice(l1)
    l2.append(elem)
    l1.remove(elem)

print(l1)
print(l2)


