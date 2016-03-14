#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# -------------------------------------------------------------------------------------------
# NOVA Nuevo Observatorio Virtual Argentino  - Diciembre 2013 - Free For Use
# -------------------------------------------------------------------------------------------
#
# In: Archivo con lista de nombre archivos a copiar
# In: Directorio Destino
#
# Copia los archivos de la lista al directorio destino 
#
# Ejecucion: 
#  ./copyFilesFromFile.py <archivo_con_list> <target_dir> 
#
# --------------------------------------------------------------------------------------------
# Ejemplo:
# ./copyFilesFromFile.py LINEAR.LOG /var/gavo/inputs/icatespec/data/ 
#
# Copia los archivos indicados en el archivo LINEAR.LOG, al directorio /var/gavo/inputs/icatespec/data/
# 
# --------------------------------------------------------------------------------------------
#
#

import sys
from astropy.io import fits
import os
import sys
import re
import shutil

filename = sys.argv[1]
dirname = sys.argv[2]


f = open(filename,'r')
pattern = re.compile("[^/]*\.fit");

for line in f:
	s = pattern.search(line.lower())
	newfilename = s.group()
	shutil.copy(line[:-1], dirname+"/"+newfilename)

f.close()	


