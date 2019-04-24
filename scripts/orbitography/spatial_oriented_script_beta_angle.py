#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:42:50 2017

@author: adminuser
"""

from pyorbital import tlefile
import orbital
from megalib import *
from sgp4.earth_gravity import wgs84
from sgp4.io import twoline2rv
import ephem
import geodetik as geok 
import numpy as np
import datetime as dt

tlefilpath = '/home/adminuser/aaa_CODES_BRIBES/resource.txt'
tlefilpath = '/home/adminuser/aaa_CODES_BRIBES/galileo.txt'

# readig the tle 
tle = tlefile.read('GSAT0203 (PRN E26)', tlefilpath)

# gives sat parameter (other lib)
satellite = twoline2rv(tle.line1, tle.line2, wgs84)
tle_epoch = satellite.epoch

beta_stk  = []
epoch_stk = []
dec_stk   = []
ra_stk    = []
dauxstk,daux2stk   = [],[]
dtim_stk = []

usat_stk = []

n_epoch = 10000
step = 3600
for h in range(n_epoch):
    cur_epoch          = tle_epoch + dt.timedelta(seconds=h*step)
    position, velocity = satellite.propagate(*geok.dt2list(cur_epoch)) #km,km/s

    epoch_stk.append(cur_epoch)
    
    sun_objt = ephem.Sun(cur_epoch)

    Psat = np.array(position) 
    Vsat = np.array(velocity) 

    Psat_norm = Psat / np.linalg.norm(Psat)
    Vsat_norm = Vsat / np.linalg.norm(Vsat)
    
    dec = sun_objt.dec
    ra  = sun_objt.ra
    
    dec_stk.append(dec)
    ra_stk.append(ra)
    
    # conversion via
    # https://en.wikipedia.org/wiki/Equatorial_coordinate_system
    # see also
    #https://en.wikipedia.org/wiki/Position_of_the_Sun
    #https://en.wikipedia.org/wiki/Celestial_coordinate_system
    #https://en.wikipedia.org/wiki/Ecliptic_coordinate_system
    xsun = np.cos(dec) * np.cos(ra)
    ysun = np.cos(dec) * np.sin(ra)
    zsun = np.sin(dec)
    
    Psun      = np.array([xsun,ysun,zsun])
    Psun_norm = Psun / np.linalg.norm(Psun)
    N_norm    = np.cross(Psat_norm,Vsat_norm)

    #print Psun_norm
    
    # sin_beta = dot_product(xsunn,xorbn)
    # beta = asin(sin_beta)
    sin_beta = np.dot(Psun_norm,N_norm)
    beta     = np.arcsin(sin_beta)
    
    beta_stk.append(beta)
    
    sin_beta_x = np.sin(np.deg2rad(15))  
    
    
    try:
        daux = abs( np.arcsin( sin_beta_x / np.cos(beta) ) )
    except:
        daux = np.nan
    dauxstk.append(daux)
    try:
        daux2 = abs( np.arcsin( np.sin(np.deg2rad(4.1)) / np.cos(beta) ) )
    except:
        daux2 = np.nan
    daux2stk.append(daux2)
  
    sunors = geok.ECI2RTN_or_RPY(Psat,Vsat,Psun_norm,out_rpy=1)
    sunors = sunors / np.linalg.norm(sunors)


    usat = 1.5 * np.pi - np.arctan2(sunors[2],sunors[0])
    if (usat > 2*np.pi):
        usat = usat - 2*np.pi
    if (usat >   np.pi):
        usat = usat - 2*np.pi
        
    usat_stk.append(usat)    
    
    uaux = usat
    if (abs(usat) > 0.5*pi):
        uaux = uaux - np.pi * np.sign(usat)   
    uaux = uaux + daux


    ang_vel = 24.0 / 0.1407796356286E+02 *  2*np.pi
    dtim = uaux / ang_vel
    
    dtim_stk.append(dtim)

plt.plot(epoch_stk,np.rad2deg(beta_stk))

plt.figure()

plt.plot(epoch_stk,dauxstk)
plt.plot(epoch_stk,daux2stk)

plt.figure()

plt.plot(epoch_stk,dtim_stk)
#plt.plot(epoch_stk,usat_stk)



#plt.plot(epoch_stk,ra_stk)
