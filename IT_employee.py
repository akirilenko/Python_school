from Employee import Employee
class ITEmployee (Employee):
    # def __init__(self,name=None, surname=None, position=None , salary=0):
    #     # Вариант создания  конструктора №1
    #     # self.name = name
    #     # self.surname = surname
    #     # self.position = position
    #     # self.salary = salary
    #     # self.skills =[]
    #     # Вариант создания  конструктора №1
    #     Employee.__init__(self,name, surname, position , salary)
    #     self.skills = []

    # def __init__(self,*args,**kwargs):
    #     Employee.__init__(self,*args,**kwargs)
    #     self.skills=[]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.skills=[]

    def add_skill(self,skill):
        self.skills.append(skill)

if __name__=="__main__" :

    empl = ITEmployee()
    empl.set_name("Elena")
    empl.add_skill("QA")

