#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:12:30 2019

@author: psakicki

Let's compute the Euler Pole of Eurasia plate
based on the velocities of some stations in
the ITRF2014 SINEX
"""

from megalib import *
import geok_euler_pole_calc as eulpol
import geo_files_converter_lib as gfc
import geodetik as geok
import numpy as np

### Local Path of the ITRF2014 SINEX file
### can be downloaded here :
### ftp://itrf.ign.fr/pub/itrf/itrf2014/ITRF2014-IGS-TRF.SNX.gz

p = "<path>/ITRF2014-IGS-TRF.SNX"

DF_ITRF = gfc.read_sinex(p,True)

### Select some station in Europe
Stations = ["BRST","BRUX","ZIMM","POTS","MATE"]

DF_ITRF_EURA = DF_ITRF[DF_ITRF["STAT"].isin(Stations)]


#### Convert XYZ => Lat Lon Height
lat_ref,long_ref , h_ref = geok.XYZ2GEO(DF_ITRF_EURA["x"],
                                        DF_ITRF_EURA["y"],
                                        DF_ITRF_EURA["z"])

#### Convert XYZ velocity => topocentric ENU velocity
vn_ref ,ve_ref , vh_ref = geok.XYZ2ENU(DF_ITRF_EURA["vx"],
                                       DF_ITRF_EURA["vy"],
                                       DF_ITRF_EURA["vz"],
                                       lat_ref,
                                       long_ref)

### Uncertainties set to 0
incvn_ref = None
incve_ref = None

### Compute the Euler Pole of the plate based on the set of station we selected
w,wratedeg,wlat,wlong,wwmat,desmat,nrmatinv=eulpol.euler_pole_calc(lat_ref,long_ref,
                                                                   vn_ref,ve_ref,
                                                                   incvn_ref,incve_ref)
#Returns
#w : numpy.array
#   Euler vector (rad/yr)
#wratedeg : float
#   Rate of rotation (deg/Myr)
#wlat,wlong : float
#   latitude and longitude of the Euler pole (deg)
#wwmat : numpy.array
#   weight matrix (for debug)
#desmat : numpy.array
#   design matrix (for debug)
#nrmatinv : 2-tuple
#   output of scipy's lstsq fct (for debug)


### Compute the Euler Pole of the plate based on the set of station we selected
vne_relat=eulpol.euler_vels_relative_to_ref(w,lat_ref,long_ref,vn_ref,
                                          ve_ref,incvn_ref,incve_ref)

### Convert the Euler vector w to a more intuitive latitude/longitude/rate
#Returns
#wlat,wlong : float
#   latitude and longitude of the Euler pole (deg)
#wrate : float
#   Rate of rotation (rad/Myr)
#wratedeg : float
#   Rate of rotation (deg/Myr)

### Convert the Euler vector from the pole latitude, longitude and rate
### Exemple for the Sinai plate, in Sadeh et al. 2012
w = eulpol.euler_pole_vector_from_latlongrate(56.642,330.836,np.deg2rad(0.35))