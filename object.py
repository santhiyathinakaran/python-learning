class Student:
    def calculateGrade(self):
        self.total=self.m1+self.m2
        if self.total<100:
            self.grade='o'
        else:
            self.grade='a'
            print(f'grade of {self.name} is {self.grade}')
    def __init__(self,name,age,m1,m2):
        self.name=name
        self.age=age
        self.m1=m1
        self.m2=m2
s=Student('santhiya',1,100,100)
s.calculateGrade()
    
