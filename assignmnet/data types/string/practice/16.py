

s1=input("Enter string:")
s2=input("Enter another string:")
print( s1[:(len(s1)//2)] + s2[:] + s1[((len(s1))//2):])
