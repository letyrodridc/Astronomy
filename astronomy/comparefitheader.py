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

filename1 = sys.argv[1]
filename2 = sys.argv[2]
file1 = headerSet(filename1)
file2 = headerSet(filename2)

file1 ^= file2
it = iter(file1)

while (True):
	try:
		print it.next()
	
	except StopIteration:
		break;



