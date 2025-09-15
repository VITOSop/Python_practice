
class Employee:
    company_name="CR7 pvt ltd."
    def __init__(self):
        self.empid=int(input("Enter emp id:"))
        self.name=input("Enter emp name:")
        self.designation=input("Enter designation:")
        self.__salary=int(input("Enter salary:"))
        self.project_ids_assigned=set(input("Enter project id:"))
        self.skills=list(input("Enter skills:"))

    def display_projectids(self):
        print("Project ids are:",self.project_ids_assigned)

    def display_identity(self):
        print("IDENTITY:",Employee.company_name,self.empid,self.name,self.designation)
    
    def check_relevant_skill(self,skill):
        
        if skill in self.skills:
            print("Found.")
        else:
            print("Not found.")
    @classmethod
    def display_company_name(cls):
        print(Employee.company_name)

    def __str__(self):
        return str(self.empid)+self.name+\
        self.disignation+\
        str(self.project_ids_assigned)+\
        str(skill)

print("\t---Enterv 3 employee details:---\t")
e1=Employee()
e2=Employee()
e3=Employee()
print("\t---Project ids:---\t")
e1.display_projectids()
e2.display_projectids()
e3.display_projectids()
print("\t---IDENTITY---\t")
e1.display_identity()
e2.display_identity()
e3.display_identity()


if e1.check_relevant_skill("python")==True:
    e1.display_id()
if e2.check_relevant_skill("python")==True:
    e2.display_id()
if e3.check_relevant_skill("python")==True:
    e3.display_id()

print("\t---COMPANY DETAILS---\t")
Employee.display_company_name()

print("\t---Employee Detail USing __str__---\t")
print(e1)
