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
	c = get_coords("HD 128620")
	print c
if  __name__ =='__main__':
    main()
