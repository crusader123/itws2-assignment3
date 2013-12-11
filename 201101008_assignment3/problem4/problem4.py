import re
import collections
from sets import Set
import sys

def checpat(pat): 
	
	return re.findall('[a-zA-Z\']+', pat) 



def capital(w):
	w = w[0].upper()+w[1:]
	return w
	
pattern = "abcdefghijklmnopqrstuvwxyz\'"
def hash(lf):
    table = collections.defaultdict(lambda: 1)
    for fi in lf:
        table[fi] = table[fi]+1
    return table

fp = open('words.txt','r')
p=checpat(fp.read())


dic = hash(p)


def union(a):
	b=list(a)
	l=map(lambda x:capital(x),b)
	#l= set(l)
	b=b+l
	return set(b)
	

def level1(word):
   spl=[]
   swp=[]
   change=[]
   app=[]
   spl = [(word[:i], word[i:]) for i in range((len(word)+1),0,-1)]
   deletes = [a + b[1:] for a, b in spl if b]
   swp = [a + b[1] + b[0] + b[2:] for a, b in spl if len(b)>1]
   change  = [a + c + b[1:] for a, b in spl for c in pattern if b]
   app  = [a + c + b     for a, b in spl for c in pattern]
   l= set(deletes+swp+change+app)
   return l 		
   


def level2(w):
    	L=[]
	for it1 in level1(w):
		it5=capital(it1)
		for it2 in level1(it1):
			if it2 in dic:
				L.append(it2)
		for it6 in level1(it5):
			if it6 in dic:
				L.append(it6)
	return set(L)

def level3(w):
    	L=[]
	for it3 in level2(w):
		#it7=capital(it3)
		for it4 in level2(it3):
			if it4 in dic:
				L.append(it4)
		#for it8 in level2(it7):
			#if it8 in dic:
				#L.append(it8)
	return set(L)

def yes(w1): 
	l = set(w for w in w1 if w in dic)
	return l

def check(w):
    co=1
    c1 = yes([w])
    if len(c1) == 1:
	print "The word is correctly spelt."
	exit(0)
    else :
    	c2 = yes(level1(w))
   
    	c3 = level2(w) 
    
    	c4 = level3(w)
    #print c4
    	s1=c1.copy()
    	s2=c2.copy()
    	s3=c3.copy()
    #s4=c4.copy()
    	li=[]
    	if co < 5:
    		print "The word is incorrectly spelt . The nearest options are :"
    		c2=c2 | c1
		s2=c2.copy()
		while len(c2) != 0 and co <= 5:
			item1=c2.pop()
			print item1
			co=co+1
			if co==6:
				exit(0)
    	if co < 5:	
    		c3 = c3 | c2
		c3 = c3 - s2
		s3 = c3.copy()
		while len(c3) != 0 and co <= 5:
			item2=c3.pop()
			print item2
			co=co+1
			if co == 6:
				exit(0)
    	if co < 5:
    		c4 = c4 | c3
		c4 = c4 - s3
	#s4 = c4.copy()
		while len(c4) != 0 and co <= 5:
			item3=c4.pop()
			print item3
			co=co+1
  
s1=sys.argv[1]
check(s1)
