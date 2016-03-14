#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# -------------------------------------------------------------------------------------------
# NOVA Nuevo Observatorio Virtual Argentino  - Diciembre 2013 - Free For Use
# -------------------------------------------------------------------------------------------
#
# Busca en un directorio todos los archivos FITS que tienen caracteres ascii invalidos > 127
# In: Directorio Destino - Donde esta los archivos
#
# Ejecucion: 
#  ./showinvalidasciilist.py <target_dir> 
#
# --------------------------------------------------------------------------------------------
# Ejemplo:
# ./copyFilesFromFile.py /var/gavo/inputs/icatespec/data/ 
#
# --------------------------------------------------------------------------------------------
#

import sys
from astropy.io import fits
import os
import sys
import re

dir = sys.argv[1]
invalidFiles = []

def showInvalidInFile(filename):

	f = open(filename, mode='readonly')

	line = f.read(80);

	p = re.compile("END\s\s\s\s")

	showFilename=True

	while (not p.match(line)):
		errorline = False
		errorchars = []

		line = f.read(80)
		for c in line:
                	if ord(c) > 127:
				errorchars.append(c)
				errorline = True

		if errorline == True:

			if showFilename==True:
				print filename
				invalidFiles.append(filename);
				showFilename=False

			print errorchars
			print line
			errorline = False	
	f.close();



for filename in os.listdir(dir):
	showInvalidInFile(dir+"/"+filename)

f2 = open("showinvalidascii.out", "w")

for fname in invalidFiles:
	f2.write(fname+"\n")
f2.close()

