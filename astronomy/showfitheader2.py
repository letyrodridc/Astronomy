#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
import sys
from astropy.io import fits
import os
import sys
import re

filename = sys.argv[1]


f = open(filename, mode='readonly')

line = f.read(80);

p = re.compile("END\s\s\s\s")

while (not p.match(line)):
	print line
	line = f.read(80);

f.close();
