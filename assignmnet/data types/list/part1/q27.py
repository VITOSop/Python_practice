'''
                                    SORTING
l1=[4,2,6,1]
print("List before sorting:",l1)
l1.sort()
print("List after sorting:",l1)

print("Second smallest no will be:",l1[1])

'''
'''                                  POP

l1=[4,2,6,1,4]
l2=[]

for e1 in l1:
    if e1 not in l2:
        l2.append(e1)

print(l1)
print(l2) 

e2=max(l2)
l2.remove(e2)

e3=max(l2)
print(e3)

                                   DANGER
'''

s=float("inf")
s2=float("inf")

for e1 in l1:
    if e1<s:
        s2=s
        s=e1
    elif (e1<s2) and (e1>s):
        s2=e1
print(s2,s)
