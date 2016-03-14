#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

dir = sys.argv[1]

data = dict()
qty = 0

for filename in os.listdir(dir):
	try:
		hdulist = fits.open(dir+'/'+filename, mode='readonly')

		hdu =  hdulist[0].header
	

		for k in hdu.keys():
			if (not data.has_key(k)):
				data[k] = set()
			data[k].add(filename)

		hdulist.close();
		qty+=1
	except:
		print filename	
		hdulist.close();
	
#Counting Sort
ordena = [None] * (qty+1)


print qty
print ordena

for k in data.keys():
	if (ordena[len(data[k])] == None):
		ordena[len(data[k])] = [[],set()]
	ordena[len(data[k])][0].append(k)
	
	for e in data[k]:
		ordena[len(data[k])][1].add(e)
i=0
while(i<len(ordena)):
	print i
	if (ordena[i] == None):
		print None
	else:
		print ordena[i][0]
		print ordena[i][1]
	print "\n"
	i+=1
	

