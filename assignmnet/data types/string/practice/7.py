'''
s1="not so poor"-->good
s1-"poor"--->poor
s1="not not poor"
s1="not poor ...poor..not"
'''

s1=input("Enter string:")

n=s1.find("not")
p=s1.find("poor")

if (n!=-1) and (n<p):   
    s1=s1.replace(s1[n:(p+len("poor"))]," good ")
else:
    pass
print(s1)
