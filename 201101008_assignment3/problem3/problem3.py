import csv
import sys
f=open(sys.argv[1],'rb')
sy=(int)(sys.argv[2])
l=csv.reader(f)
li=list(l)
a=len(li)
li2= map(lambda i:(int)(li[i][1]),range(a))
li1= map(lambda i:(int)(li[i][0]),range(a))
print reduce(lambda x,y:x+y,filter(lambda x:x>sy,li2))
print reduce(lambda x,y:x+y,li1)
