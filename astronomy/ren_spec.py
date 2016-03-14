#!/usr/bin/env python

import os
import sys
import re

dir = sys.argv[1]
pre = sys.argv[2]

for filename in os.listdir(dir):
    print  pre+filename

if len(sys.argv) > 2:
	print "Renaming files..."
	for filename in os.listdir(dir):
   		os.rename(dir+'/'+filename, dir+'/'+pre+filename)




