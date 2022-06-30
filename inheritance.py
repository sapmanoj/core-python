
# # inheritnace is  the process of  aquaring the parent 
# # class property into the  child  class except private
# class Parentclass:
#     def pinfo(self):
#         print(" this is manoj")
# class Chlidclass(Parentclass):
#     def cinfro( self ):
#          print('from cinfo')
#     def pinfo(self):
#         print(" this is Ram")

# c= Chlidclass()
# x=Parentclass()
# c.pinfo()
# x.pinfo()
# c.cinfro()




class Parentclass:
        def pinfo(self):
              print(" this is manoj")
class Chlidclass(Parentclass):
    def cinfro( self ):
         print('from cinfo')
    def pinfo1(self):
        print(" this is Ram")
class grandchild( Chlidclass):
     def manoj(self):
             print(' my name is manoj')

x= grandchild()
x.cinfro()
x.pinfo()
x.pinfo1()
x.manoj()






     