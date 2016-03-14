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


def process(filenameDir, updateCoords):
    objectName,ra,dec = get_object_from_fit(filenameDir)

    if objectName != None:
        print filenameDir+": "+objectName+","+str(ra)+","+str(dec)
    else:
        print filenameDir+": FIT sin objectName"

def get_object_from_fit(filenameDir):
    objectName = None
    ra = None
    dec = None
    try:

        hdulist = fits.open(filenameDir, mode='readonly')
        prihdr = hdulist[0].header
        objectName = prihdr["OBJECT"]
        ra = prihdr["RA"]
        dec = prihdr["DEC"]
        hdulist.close()

    except:
        if (traceback.format_exc()):
            error = traceback.format_exc()
            #print error
            #print "filenameDir ERROR reading FIT"

    return objectName, ra, dec



def main():
    dirName = sys.argv[1]
    updateCoords = False

    if len(sys.argv) > 2:
        updateCoords = sys.argv[2]

    l = [filename for filename in os.listdir(dirName)]

    while (len(l) > 0):
        filename = l.pop()
        print 'Procesando archivo ...' + filename
        path = os.path.join(dirName, filename)
        if os.path.isdir(path):
            l.extend([filename+'/'+f for f in os.listdir(path)])
        else:
            process(dirName+filename, updateCoords)

if  __name__ =='__main__':
    main()
