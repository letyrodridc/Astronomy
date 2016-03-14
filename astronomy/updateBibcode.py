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


def process(filenameDir, bibcode):
    update_reference(filenameDir, bibcode)


def update_reference(filenameDir, bibcode):
    try:

        hdulist = fits.open(filenameDir, mode='update')
        prihdr = hdulist[0].header
        
        if "REFERENC" not in prihdr:
            prihdr["REFERENC"] = bibcode
        else:
            print filenameDir+" existe REFERENC : "+prihdr["REFERENC"]

        hdulist.flush()
                        
        hdulist.close()
    except:
        if (traceback.format_exc()):
            error = traceback.format_exc()
            print error

def main():
    if len(sys.argv) < 2:
        print "Debe ingresar dos parámetros: directorio y archivo donde esta el bibcode"

    dirName = sys.argv[1]
    bibCodeFilename = sys.argv[2]

    print "Ejecutando para: "
    print dirName
    print bibCodeFilename

    f = open(dirName+bibCodeFilename,'r')
    bibcode = f.read()

    print "Actualizando bibcode: "+bibcode
    continuar = raw_input("continuar?[y/n]")

    if continuar == 'y':
        l = [filename for filename in os.listdir(dirName)]

        while (len(l) > 0):
            filename = l.pop()
            print 'Procesando archivo ...' + filename
            path = os.path.join(dirName, filename)
            if os.path.isdir(path):
                l.extend([filename+'/'+f for f in os.listdir(path)])
            else:
                if filename != bibCodeFilename:
                    process(dirName+filename, bibcode)
    else:
        print "Ha elegido no continuar el proceso."
    f.close()


if  __name__ =='__main__':
    main()
