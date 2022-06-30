class A:
     def printhelloA(self):
         print('hello A')
class B(A):
      def printhelloB(self):
         print('hello B')
class C(A):
     def printhelloc( self):
         print('heedlo  c')
x=B()
y=C()
x. printhelloA()
y.printhelloA()
x.printhelloB()
y.printhelloc()