#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

dir = sys.argv[1]

for filename in os.listdir(dir):

	try:
		hdulist = fits.open(dir+'/'+filename, mode='update')

		hdulist.info();
	
		hdu =  hdulist[0]

		hdu.verify('fix')

		hdulist.close();
	except: 
		print 'Next' 
