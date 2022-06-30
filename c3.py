class Employee:
    company='CT'

    def __init__(self,n,s):
       self.name=n
       self.salary=s
    def edetail(self):
       print(self.name,' ',self.company,' ',self.name)
    def incresalary(self,s,i):
         return i, s+i*s/100
e=Employee('python',20000)
e.edetail()
a,b=e.incresalary(e.salary ,20)
print(' incresed by', a,'%',' total  salary ',b)


