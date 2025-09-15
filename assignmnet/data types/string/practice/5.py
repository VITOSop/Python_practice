

s1=input("Enter s1")
s2=input("Enter s2")

if (len(s1)==0) and (len(s2)==0):
    print("Out of bound")
else:
    s3=s1[:2]+s2[2:]
    s4=s2[:2]+s1[2:]
    print(s4+" "+s3)
