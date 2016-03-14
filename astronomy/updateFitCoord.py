#!/usr/bin/env python
# coding: utf8
# NOVA Scritpt - October 2015
#
#

from astropy.io import fits
import traceback
import os, shutil
from astropy.coordinates import SkyCoord, Galactic
from astropy.coordinates.name_resolve import NameResolveError


def process(filenameDir):
    objectName = get_object_from_fit(filenameDir)

    if objectName != None:
        c = get_coords(objectName)

        if c != None:
            update_coords_in_fit(filenameDir, c)
        else:
            print filenameDir+": No se encontraron coordenadas para: "+objectName 

    else:
        print filenameDir+": FIT sin objectName"

def get_object_from_fit(filenameDir):
    objectName = None

    try:

        hdulist = fits.open(filenameDir, mode='readonly')
        prihdr = hdulist[0].header
        objectName = prihdr["OBJECT"]
        hdulist.close()

    except:
        if (traceback.format_exc()):
            error = traceback.format_exc()
            print error
            print "filenameDir ERROR reading FIT"

    return objectName 



def update_coords_in_fit(filenameDir, coords):
    try:

        hdulist = fits.open(filenameDir, mode='update')
        prihdr = hdulist[0].header
        prihdr["RA"] = coords.ra.deg
        prihdr["DEC"] = coords.dec.deg
        hdulist.flush()
                        
        hdulist.close()
    except:
        if (traceback.format_exc()):
            error = traceback.format_exc()
            print "filenameDir ERROR updating Coords"


def get_coords(targetObject):
    c = None

    retry = 5

    try:
        c = SkyCoord.from_name(targetObject)
    
    except NameResolveError:
        retry == 0
        pass
    except:
        if retry == 0:
            throws()
        else:
            retry = retry -1
            c = SkyCoord.from_name(targetObject)
    
    return c    

def main():
    dirName = "/home/nova/data/bibCba/final/data/"
    process(dirName+"514b.fit")

if  __name__ =='__main__':
    main()
