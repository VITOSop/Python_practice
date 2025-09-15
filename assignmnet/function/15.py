
def alfa(s):
    s=s.replace("-",",")

    l1=s.split(",")
#    print(l1)
    print(sorted(l1))

    s2=" ".join(l1)
    s2=s2.replace(" ","-")
   
    return s2


s="green-red-yellow-black-white"
print(alfa(s))

