#!/usr/bin/env python
import mincemeat
numlist=list()
for i in range(2,10000001):
	numlist.append(i)

data= numlist
length = len(data)
chunkLength = length / 10000
Lists = [data[i:i+chunkLength] for i in range(0,len(data), chunkLength)]
datasource = dict(enumerate(Lists))

def mapfn(k,v):
	for i in v:
		numStrings = str(i)
		if numStrings == numStrings[::-1]:
			yield 'num', numStrings

def reducefn(k, v):
	def isPrime(num):
		import math
		if(num==2):
			return True
		if(num%2==0):
				return False
		for x in range(3,int(math.sqrt(num))+1,2):
			if(num%x==0):
					return False
		else:
			return True

	palliprime=list()
	for a in v: 
		nu = int(a)
		if(isPrime(nu)):
			palliprime.append(nu)
			

	outSum = sum(palliprime)
	return 'output: {0}\nlength: {1}\n   sum: {2}'.format(palliprime, len(palliprime), outSum)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results=s.run_server(password="changeme")
print results['num']
