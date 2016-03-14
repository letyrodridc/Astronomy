#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

filename = sys.argv[1]


f = open(filename, mode='readonly')
f2 = open(filename+"out", mode='write')

line = f.read(80);
f2.write(line);
p = re.compile("END\s\s\s\s")

while (not p.match(line)):
	errorline = False
	errorchars = []

	
	line = f.read(80)
	line2 = ""
	for c in line:
               	if ord(c) > 127:
			errorchars.append(c)
			errorline = True
                        line2+='o'
		else:
			line2+=c		

	f2.write(line2);
	if errorline == True:
		print errorchars
		print line
		errorline = False
	
while (True):
	line = f.read(80)
	if not line: break
	f2.write(line)
	
f2.close()
f.close();
print "FIN"

