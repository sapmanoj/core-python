d=open('manoj.txt','r')

lines=d.readlines()
c=0
for line in lines:
    c=c+1
    print(' {} {}'.format(c,line.strip()))

