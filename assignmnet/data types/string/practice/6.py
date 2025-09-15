
s1=input("Enter string:")

if len(s1)<3:
    print("print should contail atleast 3 character")
else:
    if (s1[-3:]=="ing"):
        s1+="ly"
        
    else:
        s1+="ing"
    print(s1)
