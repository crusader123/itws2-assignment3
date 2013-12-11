import sys
a=open(sys.argv[1])
l1=a.readline()
nrow,ncol=l1.split()
nrow1=(int)(nrow)
ncol1=(int)(ncol)
m=map(lambda x:x,map(lambda x: a.readline().split(),range(nrow1)))
l1=a.readline().split()
nrow2,ncol2=(int)(l1[0]),(int)(l1[1])
v=map(lambda x:x,map(lambda x:a.readline().split(),range(nrow2)))
m1=map(lambda i:map(lambda j:reduce(lambda x,y:x+y,map(lambda k:(int)(m[i][k])*(int)(v[k][j]),range(nrow2))),range(ncol2)),range(nrow1)) 
l=[]
map (lambda x:map(lambda y:l.append(m1[x][y]),range(ncol2)),range(nrow1));
f=len(l)
def pr(a,x,nco):
	if(x%nco==(nco-1)):
		print a[x]
	else:
	 	print a[x],
map(lambda x:pr(l,x,ncol2),range(f)) 
