
 
 # intillizer is used  to intailize a state  of the  object
 #  function  define in class is known as the method\
 # fist parameter of any method is  self
 # self: this method  denoted the instance of class 

  #dynamic varaible
# class EMp:
#      pass 
# e=EMp()
# e.name='manoj'
# e.age=30
# print( 'name',e.name, 'age' ,e.age)


# class Emp:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def detail(self):
#         print(self.name)
#         print(self.age)

# e=Emp('manoj',23)
# e.detail()
# print(e.name)
# print(e.age)
class Emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def detail(self):
        print(self.name,self.age)
    def mydetails(self,gender, education):
        print('name',self.name)
        print('age',self.age)
        print( 'gender',gender)
        print( 'education',education)
        

e=Emp('manoj',23)
e.detail()
e.mydetails('male' ,'BE')
        
