class Mylist:
    def __init__(self,l):
        print("In init, assigned list..")
        self.l=l

    def __add__(self,other):
        s1=set(self.l)
        s2=set(other.l)
        s3=s1.union(s2) #join 2 sets
        m=Mylist(list(s3))
        return m
    def __sub__(self,other):
        print("in substraction..")
        s1=set(self.l)                 
        s2=set(other.l)
        s3=s1.symmetric_difference(s2) #s1^s2 
        m=Mylist(list(s3))
        return m
    
    def __truediv__(self,other):
        s1=set(self.l)                 
        s2=set(other.l)
        s3=s1 & s2 
        m=Mylist(list(s3))
        return m
    
    def __str__(self):
        return str(self.l)

m1=Mylist([1,2,3,4])
m2=Mylist([4,5,6,12])
print(m1+m2)    #[1,2,3,4,5,6,12]
print(m1-m2)    #[1,2,3,5,6,12]
print(m1/m2)    #[4]
