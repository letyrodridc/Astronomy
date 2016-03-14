#!/usr/bin/env python
# coding: utf8
# NOVA Scritpt - October 2015
#
#

from astropy.io import fits
import traceback
import os, shutil, sys
from astropy.coordinates import SkyCoord, Galactic
from astropy.coordinates.name_resolve import NameResolveError


def process(filenameDir):
    bibcode = get_bibcode_from_fit(filenameDir)

    if bibcode != None:
        print filenameDir+": "+bibcode
    else:
        print filenameDir+": FIT no tiene bibcode"

def get_bibcode_from_fit(filenameDir):
    bibcode = None
 
    try:

        hdulist = fits.open(filenameDir, mode='readonly')
        prihdr = hdulist[0].header
        bibcode = prihdr["REFERENC"]
        hdulist.close()

    except:
        if (traceback.format_exc()):
            error = traceback.format_exc()
            #print error
            #print "filenameDir ERROR reading FIT"

    return bibcode



def main():
    dirName = sys.argv[1]
 
 
    l = [filename for filename in os.listdir(dirName)]

    while (len(l) > 0):
        filename = l.pop()
        print 'Procesando archivo ...' + filename
        path = os.path.join(dirName, filename)
        if os.path.isdir(path):
            l.extend([filename+'/'+f for f in os.listdir(path)])
        else:
            process(dirName+filename)

if  __name__ =='__main__':
    main()
