#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

filename = sys.argv[1]
dir = sys.argv[2]
dir2 = sys.argv[3]

hdulist = fits.open(dir+'/'+filename)

hdulist.info();

hdu =  hdulist[0]

hdu.verify('fix')

hdulist.writeto(dir2+'/'+filename, output_verify='fix')
	
hdulist.close();

