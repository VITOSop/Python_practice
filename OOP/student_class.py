
class student:
    def __init__(self):
        self.name=input("Enter name:")                
        self.roll_no=input("Enter roll no:")
        self.mod1_marks=int(input("Enter marks1:"))        
        self.mod2_marks=int(input("Enter maek2:"))
        self.mod3_marks=int(input("Enter maek3:"))
        
    def display(self):        
        print(self.name,self.roll_no,self.mod1_marks,self.mod2_marks,self.mod3_marks)

    def cal_total(self):
        self.total=self.mod1_marks+self.mod2_marks+self.mod3_marks
        print("Total marks are:",self.total)

s1=student()
s1.display()
s1.cal_total()
