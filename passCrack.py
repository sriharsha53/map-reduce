#!/usr/bin/env python
import mincemeat
import string
import random
import itertools as t
from sys import argv
script, hashcode = argv

def pass_gen():
	str = string.ascii_lowercase + string.digits
	pList = list()
	for i in range(1,5):
		pList.append(t.product(str,repeat=i))

	wordsList = list()
	for iterate in pList:
		for singlewordlist in iterate:
			word = ''.join(singlewordlist)
			wordsList.append(word)
	return wordsList


data = pass_gen()
length = len(data)
chunkLength = length / 800
Lists = [{'sublists': data[i:i+chunkLength],'hashcode': hashcode} for i in range(0,len(data), chunkLength)]
datasource = dict(enumerate(Lists))

def mapfn(k, v):
	import hashlib
	for w in v['sublists']:
		hashw = hashlib.md5(w).hexdigest()[0:5]
		hashc = v['hashcode']
		if hashw == hashc:
			yield hashc, w

def reducefn(k, v):
	return v
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results



