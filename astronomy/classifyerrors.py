#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# -------------------------------------------------------------------------------------------
# NOVA Nuevo Observatorio Virtual Argentino  - Diciembre 2013 - Free For Use
# -------------------------------------------------------------------------------------------
#
# In: file with GAVO imp errors
# Out: Filename, error archive. Ordered by error.
#
# 
# Ejecucion: 
#  ./classifyerror.py <errorlog.log>
#
# --------------------------------------------------------------------------------------------
#

import sys
from astropy.io import fits
import os
import sys
import re

filename = sys.argv[1]

# 
errors = []
errorFile = "";

# Graba archivos con la informacion de que archivo tiene cada ctype

f = open(filename,'r')

for line in f:
	if (line.find("Failed") >=0):
		errorFile =  line.replace("Failed ", "");
	else: 
		if (line.find("Error while importing source; changes from this source will be rolled back, processing will continue.") >= 0):
			error = line
			error = error.replace("*X*X* Error while importing source; changes from this source will be rolled back, processing will continue. ","")
			errors.append(error[1:-2]+"\t"+errorFile);

f.close()	


errors.sort()	

	

# Graba los archivos que dieron error

f=open("error.log",'w')

for line in errors:
	f.write(line)

f.close()

