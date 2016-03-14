#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# -------------------------------------------------------------------------------------------
# NOVA Nuevo Observatorio Virtual Argentino  - Diciembre 2013 - Free For Use
# -------------------------------------------------------------------------------------------
#
# In: Archivo con lista de nombre archivos a copiar
# In: Directorio Destino
# In: Prefijo inicial
# Out: archivo out.log con como hizo los renombres.
#
# Copia los archivos de la lista al directorio destino agregando un prefijo numerico que se
# autoincremente a partir del prefijo inicial 
# Ejecucion: 
#  ./copyFilesFromFile.py <archivo_con_list> <target_dir> <prefijo>
#
# --------------------------------------------------------------------------------------------
# Ejemplo:
# ./copyFilesFromFile.py LINEAR.LOG /var/gavo/inputs/icatespec/data/ 1
#
# Copia los archivos indicados en el archivo LINEAR.LOG, renombrandolos agregandole un prefijo
# que arranca en 1 y se autoincrementa, al directorio /var/gavo/inputs/icatespec/data/
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
prefix = int(sys.argv[3])


f = open(filename,'r')
f2 = open("out.log",'w')
pattern = re.compile("[^/]*\.fit");

for line in f:
	s = pattern.search(line.lower())
	newfilename =  str(prefix)+s.group()
	f2.write(newfilename+"\t"+line)	
	prefix+=1
	shutil.copy(line[:-1], dirname+"/"+newfilename)

f2.close()
f.close()	


