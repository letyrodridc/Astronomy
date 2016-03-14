#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re




def headerSet(filename):
	result = set()

	p = re.compile("END\s\s\s\s")

	f = open(filename, mode='readonly')

	line = f.read(80);
	result.add(line)
	
	while (not p.match(line)):
        	line = f.read(80)
		result.add(line)

	f.close();

	return result

filename = sys.argv[1]
dir1 = sys.argv[2]
dir2 = sys.argv[3]


f = open(filename,'r')

for file in f:
	file = file[:-1]
	file1 = headerSet(dir1+"/"+file)
	file2 = headerSet(dir2+"/"+file)

	print "-------- "+file+" -----------"
	file1 ^= file2
	it = iter(sorted(file1))
	
	while (True):
		try:
			print it.next()
	
		except StopIteration:
			break;



