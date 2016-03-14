#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# -------------------------------------------------------------------------------------------
# NOVA Nuevo Observatorio Virtual Argentino  - Diciembre 2013 - Free For Use
# -------------------------------------------------------------------------------------------
#
# In: Directorio donde buscar fits (busca en forma recursiva - tambien subdirectorios)
# Out: Archivos.log - Arma archivos .log que clasifican los fits segun el CTYPE1 que tengan definido
#
# 
# Ejecucion: 
#  ./searchMulti.py <directorio_busca_fits>
#
# --------------------------------------------------------------------------------------------
# Ejemplo:
# ./searchMulti.py /var/gavo/inputs/icatespec/data/
#
# Deja en el directorio actual files LINEAR.log y MULTISPEC.LOG con los nombres de los archivos 
# que tienen en su header CTYPE1 LINEAR o MULTISPEC
# 
# --------------------------------------------------------------------------------------------
# Agregado: crear un archivo adicional error.log con los fits de los cuales no pudo leer la cabecera
#
#

import sys
from astropy.io import fits
import os
import sys
import re

dir = sys.argv[1]

# 
ctypes = dict()  
errorfiles = []


# Recorre los archivos del directorio
for dirEntry  in  os.walk(dir):
    dirpath = dirEntry[0];

    for filename in dirEntry[2]:
	
	try:	    
        	hdulist = fits.open(dirpath+'/'+filename, mode='readonly')

        	hdu =  hdulist[0]

        	# Obtiene el ctype1 de la cabacera del fit
        	ctype1 = hdu.header['ctype1']
        	print filename+" ................. "+ctype1

        	
        	# Guarda en el mapa el ctype y la lista de archivos que lo contiene
        	if (not ctypes.has_key(ctype1)):
            		ctypes[ctype1] = []

        	ctypes[ctype1].append(dirpath+"/"+filename)
	    
        	# ---

        	hdulist.close();
	except Exception, e:
		errorfiles.append(dirpath+"/"+filename)
		print "ERROR EN"+filename
		print e;
	 

# Graba archivos con la informacion de que archivo tiene cada ctype

for type in ctypes.keys():
        f = open(type+".log",'w')

        for filename in ctypes[type]:
                f.write(filename+'\n')

        f.close()	
	
# Graba los archivos que dieron error

f=open("error.log",'w')

for filename in errorfiles:

	f.write(filename+'\n')

f.close()

