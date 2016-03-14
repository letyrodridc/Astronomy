#! /usr/bin/env python

import os
import sys
import re
import glob
import shutil



#---------------------------------------------------------------
RD_DIR = "."
BACKUP_DIR = "nova_rd_dev"

#--------------------------------------------------------------
pattern = re.compile(".*\.rd$");
matched = []
dirnames = set()

for valor  in  os.walk(RD_DIR):
   dirpath = valor[0];
   
   if (dirpath.find(BACKUP_DIR)<0):
   	for filename in valor[2]:
		if (pattern.match(filename)):
			t = dirpath,filename
			matched.append(t)
			dirnames.add(dirpath)

for dirname in dirnames:
	newdir = BACKUP_DIR+dirname[1:]
        try:
	
		open(newdir)
	except IOError as error:
		if (error.errno == 2):
			print "- Creando directorio: "+newdir
			os.mkdir(newdir)
			 

for dirname, filename in matched:
	src = dirname+"/"+filename
	dst = BACKUP_DIR+dirname[1:]
	#print src
	#print dst
	print "Backupeando.... "+src
	shutil.copy(src,dst)
