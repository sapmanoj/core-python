#  set is  unordered collection of   qnique elements
# it  cant  add and remove element  from set
#  we  dont have index association with  set
#  set  cant have mutable element like list, set and dictionary

# s=set()
# print(type(s))

# k={1,3,5,6,7,7,3}
# print(type(k))


# s=set([3,5,6])
# s.add(5)
# print(s)


# s=set([3,5,6])
# s.add(55)
# print(s)


# s={2,4,6,8,10}

# for i in range(11,20):
#      if i%2==0:
#             s.add(i)
# print(s)

# s={"manoj","sapkota","ram","shyam","hari"}    
# print(s)

# s.discard("manoj")
# print(s)

# s2={11,13}

# s.update(s2)
# print(s)



# s={3,4,5}
# v=eval(input("eneter"))
# if  v in s:
#      print('true')
# if v not in  s:
#     print('false')

# s={3,4,5}
# print(s)
# s.clear()
# print(s)


# set operations

# from ctypes import Union


# s1={3,4,5,6}
# s2={3,4,7,8}
# print(s2.issubset(s1))

# print(s1.issuperset(s2))

# # union  combine two set in one

# print(s1.union(s2))

# print(s1.intersection(s2))

# print(s1.difference(s2))
# print(s1-s2)
# print(s1.symmetric_difference(s2))





# l=[1,2,3,4,5,6,7,8,9,10]

# def oddnumberfromlistinset(k):
#      x=set(k)
#      for i in k :
#              if i%2==0:
#                     x.discard(i)
#      return x
# print( oddnumberfromlistinset(l))




            
