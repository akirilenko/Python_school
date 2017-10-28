class Employee:
    def __init__(self, name=None, surname=None, position=None, salary=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def full_name (self):
        return  self.name+self.surname

    def set_name (self, name):
        self.name = name

    def set_position (self, position):
        self.set_position = position

    def incime (self,months=0):
        print (self.salary*months)

    def __str__(self):
        return '<Employee:'+ self.full_name()+'>'

if __name__=="__main__" :

    emp = Employee ("Elena", "Pian" , "QA" ,0)
    print(emp)