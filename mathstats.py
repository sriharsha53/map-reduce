#!/usr/bin/env python
import mincemeat
from sys import argv

script, filename = argv
file = open(filename, 'r')
data = list(file)
file.close()
length = len(data)
chunkLength = length / 4
Lists = [data[i:i+chunkLength] for i in range(0,len(data), chunkLength)]
datasource = dict(enumerate(Lists))

def mapfn(k, v):
	for num in v:
		yield 'num', int(num)

def reducefn(k, vs):
	import math
	sums = sum(vs)
	count=len(vs)
	result = 0
	mean=sums/count
	sd=0
	for x in vs:
		sd= math.pow(int(x)-mean,2)+sd
	var=sd/count
	result=math.sqrt(var)
	return "  Count:   {0}\n    Sum:   {1}\nStd.dev:   {2}".format(count, sums, result)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results['num']
