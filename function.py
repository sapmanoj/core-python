#function is block of  reusable   code na d logic 

# there is  user define  function  and in build  function

#def keyword is  used to  defined the  function

# funnction  can be  paratmeter   or  not parameter wise
 
#  function may  return value or may not return value
#  non parameter
# def hello():
#     print('hellow')
#     print('wellcome')
    

# hello()
# def  sum():
#     x=eval(input('enter ist number'))
#     y=eval(input('enter 2nd number'))
#     z=x+y
#     print(z)

# sum()

# from audioop import mul


# def interest(p,t,r):
#     i=p*t*r/100
#     print(i)

# interest(20,10,30)


# def inputtaken():
#  a=eval(input('enter principle'))
#  b= eval (input('enter time'))
#  c=eval(input('enter rate'))
#  interest(a,b,c)
# inputtaken()


#x=eval(input('enter the number'))
# def loopsum(x):
#     sumdata=0
#     for i in range(x):
#         sumdata= sumdata+i
#     print(sumdata)
# loopsum(10)
# #loopsum(eval(input('enter the number')))


# returing  valur  from  function
# def multy(x,y):
#     return x*y
# #print(multy( eval(input('enter the number')),eval(input('enter 2nd number'))))

# v= multy(5,6)
# print(v)
# a=v+100
# print(a)

# def evenoddsum(k):
#     evensum=0
#     oddsum=0
#     for  i in range(k):
#         if(i%2==0):
#            evensum=evensum+i
#         else:
#            oddsum= oddsum+i

#     return evensum, oddsum
# a,b= evenoddsum(eval(input('enter value')))
# print('evensum',a, 'oddsum',b)


#  function types  deending upon the  parameter
# types of argurment in  function  call 
  #  we can pass  argrument in function by  4 types
  #   keyword agrument 
  #  default arugment
  #1  python allow  us  to intialied the agrument in function call
   #agrumnet  are  not pass in  function rgument
   #  function by  default a 
def  fullname(name="CT",age=20):
    print("name is  ",name)
    print('age is ',age)
fullname()
fullname('manoj')
fullname('manoj' ,2)
fullname(30)

# variable length argument allows  to pass  random number of argument  at  function  call
def names(*vargs):

    print(len(vargs))

    for i  in  vargs:
        print(i)

names()
names('manoj')
names('ram','Hari')
names('hari','haru','saru','shyam')

#  keyword  argument in function(qwargs)
def detail(** kwargs):
     for k,v in  kwargs.items():
         print("key",k,"values is",v)
detail()       
detail(name='manoj',age=20,address='kathmandu')
#detail(name='manoj',20) ->error positional argument follows keyword argument










  




