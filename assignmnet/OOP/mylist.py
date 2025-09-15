class mylist:
    
    def __init__(self,l):
        self.l=l

    def __add__(self,other):
        s1=set(self.l)
        s2=set(other.l)
        s3=s1 | s2
        m=mylist(list(s3))
        return m
    def __sub__(self,other):
        s1=set(self.l)
        s2=set(other.l)
        s3=s1.symmetric_difference(s2)
        m=mylist(list(s3))
        return m
    def __truediv__(self,other):
        s1=set(self.l)
        s2=set(other.l)
        s3=s1 & s2
        m=mylist(list(s3))
        return m

    def __str__(self):
        return str(self.l)

m1=mylist([2,3,4,5])
m2=mylist([4,5,6,7])
print(m1+m2)
print(m1-m2)
print(m1/m2)
