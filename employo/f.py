# mode of    file handing  tey  are :
# read  r 
#  write w
# append a
# file =open('manoj.txt','w')
# file.write('this is fist line \n')
# file.write('this is second line \n')

# manoj="hello  world"
#file.write(manoj)


# file=open('manoj.txt','r')
# print(file)
# print(file.read())
# file.close()
file= open('manoj.txt','a')
file.write("\nhello manoj\n")
file.close()