s1="restart"
s2=s1[0]

for ch in s1[1:]:
    if ch==s1[0]:
        s2=s2+"$"
    else:
        s2=s2+ch

print(s1,s2)
