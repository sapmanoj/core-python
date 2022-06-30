d={}
print(d)
print(type(d))
d={"name":"coding","address":"ktm","ward":32}
print(d['name'])
print(d['address'])
print(d['ward'])
w=d["ward"]
print(w)
d['county']='Nepal'
d['ward']=32
print(d)
for i in d:
    print(i ,'....',d[i])
x=dict(Name='manoj',course='python')
for v in x.values():
    print(v)
for  m in x.keys():
     print(m)
l=dict(Name='ramesh',course='java')
del l['course']
print(d)


# d=dict(Name="khusbu",course="python")
# for v in  d.values():
#     print(v)
# for k in d.keys():
#     print(k)

# d=dict(Name='sharada',course="java")
# del d['course']
# print(d)
# d=dict(Name="sharada",course="c++")
# for i in d.items():
#     print(i)
# l=len(d)
# print(l)
# l=[('Name','sharada'),('course','java')] 

# d=dict(l)
# for i in d:
#     print(i,' ',d[i])
# d={}
# d['country']='Nepal' 
# d['ward']=32
# print(d) 
# d=dict(Name='saru pun',course='c#') 
# for x,y in d.items():
#     print(x,y)

# n=str(input("Enter the name"))
# c=str(input("Enter the course"))
# a=str(input("Enter the address"))
# d=dict(name=n,course=c,address=a)
# for v in d.values():
#     print(v)
# for k in d.keys():
#     print(k)    
# print(d)

