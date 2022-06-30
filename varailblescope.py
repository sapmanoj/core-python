#variable scope:
from ast import Lambda
from tkinter.messagebox import YESNO


s=10
def messum():
    global s
    print(s)
    # t=50
#     s=20
#     print('local name',s)
# messum()
# print(s)
#print(t)

#  recursion is  process of  defining  something its self

# def fact(x):
#     if x==1:
#          return 1
#     else:
#         return (x*fact(x-1))
# y=fact(5)
# print(y)

#lambda  is anonymous  function having  no name  we  used the  lambda  function  for fastest  performation
# argument is the values pass in  function  call  and
#   at the time function defination and the 
#  signature as values supply  to that is  knows  as parameter
det=lambda:(print('this  is manoj'))
det()

s=lambda x:(x+10)
print(s(5))

k=lambda x,y:((x+y),(x*y))
x,y=k(30,30)
print(x)
print(y)
# for i in k:
#  print(i) namela ni tarika


    

