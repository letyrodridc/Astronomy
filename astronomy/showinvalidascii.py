#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

filename = sys.argv[1]


f = open(filename, mode='readonly')

line = f.read(80);

p = re.compile("END\s\s\s\s")

while (not p.match(line)):
	errorline = False
	errorchars = []

	line = f.read(80)
	for c in line:
                if ord(c) > 127:
			errorchars.append(c)
			errorline = True

	if errorline == True:
		print errorchars
		print line
		errorline = False	
f.close();
