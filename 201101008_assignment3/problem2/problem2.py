import fnmatch
import os
import sys
s1=sys.argv[1]
s2=sys.argv[2]
rootPath=s1
pattern='*'
si=0
for root,dirs,files in os.walk(rootPath):
	for filename in files:
		#print os.path.join(root,filename)
		si=si+os.path.getsize(os.path.join(root,filename))
		f=open(os.path.join(root,filename))
		for i in f:
			#print i,
			open(s2,"a+b").write(i)
	for dirname in dirs:
		si=si+os.path.getsize(os.path.join(root,dirname))
a= os.path.getsize(s2)
si=si/(1024.0*1024)
a=a/(1024.0*1024)
#a1=sys.getsizeof(s2)
#a1=os.path.getsize(s1)
#print "Size of "+s1+" : "+str(si)+"MB"
print "Size of "+s1+" : %.3f"%(si)+"MB"
print "Size of "+s2+" : %.3f"%(a)+"MB"
#print a
#print a1
		#str=myfile.read()
		#print str
	#myfile.close()
		#my=open("tr","a")
		#for line in str:
			#my.write(line)
	#my.close()
