class point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "x="+str(self.x)+" y="+str(self.y)

    def __add__(self,other):
        print("Addition operator is called...")
        x=self.x + other.x
        y=self.y + other.y
        p=point(x,y)
        return p
    def __sub__(self,other):
        print("Substraction operator is called")
        x=self.x-other.x
        y=self.y-other.y
        p=point(x,y)
        return p

p1=point(10,20)
p2=point(20,20)
p3=p1+p2  #point>__add__(p1,p2)
print(p1)
print(p2)
print(p3)
p4=p1-p2
print(p1)
print(p2)
print(p4)
