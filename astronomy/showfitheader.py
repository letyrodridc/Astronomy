#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

filename = sys.argv[1]




hdulist = fits.open(filename, mode='readonly')
hdu =  hdulist[0]

if (len(sys.argv) > 2):
	val = sys.argv[2]
	print filename+"....."+val+": "+hdu.header[val]
else:
	print filename
	hdrInfo = hdu.header
	
	for k in hdrInfo.keys():
		print k," = ", hdrInfo[k]

hdulist.close();
