#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

linenbr = 0

filename1 = sys.argv[1]
filename2 = sys.argv[2]

f1 = open(filename1, mode='readonly')
f2 = open(filename2, mode='readonly')

line1 = f1.read(80);
line2 = f2.read(80)

linenbr +=1 

if (not (line1 == line2)):
	print linenbr
	print line1
	print line2
	print "\n"

while True:
       	line1 = f1.read(80)
	line2 = f2.read(80)
	
	linenbr+=1
        
	if not line1:
                 break
 
	if (not (line1 == line2)):
        	print linenbr
		print line1
        	print line2
        	print "\n"


f1.close();
f2.close();


