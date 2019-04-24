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

tlefilpath = '/home/adminuser/aaa_CODES_BRIBES/galileo.txt'
# readig the tle 
tle = tlefile.read('GSAT0101 (PRN E11)', tlefilpath)

# gives sat parameter (other lib)
satellite = twoline2rv(tle.line1, tle.line2, wgs84)
tle_epoch = satellite.epoch

for h in range(10):
    cur_epoch          = tle_epoch + dt.timedelta(seconds=h*3600)
    position, velocity = satellite.propagate(*geok.dt2list(cur_epoch))

    sun_objt = ephem.Sun(cur_epoch)

    Psat = np.array(position) * 1000
    Vsat = np.array(velocity) * 1000

    Psat = np.array([   -15779.437215560150435 ,  -23508.964967410494864  ,   8644.453520237560952])
    Vsat = np.array([        1.296220384065493  ,     -1.917314252639830  ,     -2.847293074880089])
    Psun = np.array([  -1.342404641197934E+008 , -5.934080206107079E+007 , -2.572342068927875E+007])

#     AAAAAAAAAAAAA yawerr,aux,nomi
#   0.000000000000000E+000
#       -1.606542300481316
#       -1.606542300481316
# BBBBBBBBBBBBB yaw_1
#       -3.141593
# CCCCCCCCCCCC sunors
#   2.379858191647978E-002   6.654859888132475E-001  -7.460308480163662E-001
# DDDDDDDDDDDDD Inputs
#   -15779.437215560150435   -23508.964967410494864     8644.453520237560952
#        1.296220384065493       -1.917314252639830       -2.847293074880089
#  -1.342404641197934E+008  -5.934080206107079E+007  -2.572342068927875E+007
#   1.703578156137057E-001
#          41
# EEEEEEEEEEEE Rcrs2ors
#   3.532662370257567E-001  -7.688096793507927E-001   5.330195492501879E-001
#  -5.225364448455557E-001   3.104619621186746E-001   7.941181766553120E-001
#  -7.759888076421138E-001  -5.590572803191509E-001  -2.920042493231377E-001
#    Rcrs2ors = np.array([[ 0.35330134, -0.76880968,  0.53301955],
#                         [-0.52248415,  0.31046196,  0.79411818],
#                         [-0.77600804, -0.55905728, -0.29200425]])

    
    Psat_norm = Psat / np.linalg.norm(Psat)
    Vsat_norm = Vsat / np.linalg.norm(Vsat)
    
    dec = np.deg2rad(sun_objt.dec)
    ra  = np.deg2rad(sun_objt.ra)
    
    Xsun = np.cos(dec) * np.cos(ra)
    Ysun = np.cos(dec) * np.sin(ra)
    Zsun = np.sin(dec)
    
    #Psun      = np.array([Xsun,Ysun,Zsun])
    Psun_norm = Psun / np.linalg.norm(Psun)
    N_norm    = np.cross(Psat_norm,Vsat_norm)

    print(Psun_norm)
    
    Rcrs2ors = np.array([[ 0.35330134, -0.76880968,  0.53301955],
                         [-0.52248415,  0.31046196,  0.79411818],
                         [-0.77600804, -0.55905728, -0.29200425]])
       
    
#    C_eci2rtn         = geok.C_eci2rtn(Psat,Vsat)
#    C_eci2rpy_working = np.dot(C_eci2rtn,geok.C_rtn2rpy())
#    Sworking          = np.dot(Psun_norm,C_eci2rpy_working)
#
#    S2                = np.dot(C_eci2rpy_working.T,Psun_norm)
#    
#    C_eci2rpy_3       = np.dot(geok.C_rtn2rpy().T,C_eci2rtn.T)
#    C_eci2rpy_natural = np.dot(geok.C_rtn2rpy(),C_eci2rtn)
#
#    S3          = np.dot(C_eci2rpy_3,Psun_norm)
#    S3_natural  = np.dot(C_eci2rpy_natural,Psun_norm)
#
#    geok.ECI2RTN_or_RPY(Psat,Vsat,Psun_norm,0)

    
    # =============== IOV ===========================
    S = geok.ECI2RTN_or_RPY(Psat,Vsat,Psun_norm,out_rpy=1)
    AY1 = -S[1] / np.sqrt(1- S[2]**2)
    AY2 = -S[0] / np.sqrt(1- S[2]**2)
    PSI_IOV = np.arctan2(AY1,AY2)

    # S = geok.ECI2RTN(Psat_norm,Vsat_norm,Psun_norm)
    

# EEEEEEEEEEEE Rcrs2ors
#   3.532662370257567E-001  -7.688096793507927E-001   5.330195492501879E-001
#  -5.225364448455557E-001   3.104619621186746E-001   7.941181766553120E-001
#  -7.759888076421138E-001  -5.590572803191509E-001  -2.920042493231377E-001
    

#   3.532662370257567E-001  -7.688096793507927E-001   5.330195492501879E-001
#  -5.225364448455557E-001   3.104619621186746E-001   7.941181766553120E-001
#  -7.759888076421138E-001  -5.590572803191509E-001  -2.920042493231377E-001
    
    
    #############################  FOC
    AT1 = np.dot(Psun_norm,N_norm)
    AT2 = np.dot(Psun_norm,np.cross(Psat_norm,N_norm))
    PSI_FOC = np.arctan2(AT1,AT2)
    
    print(PSI_IOV , PSI_FOC)
    
    
def yaw_nominal_gal_iov(Psat,Vsat,Psun):
    # discont see read data for beta angle py
    Psat = np.array( Psat )
    Vsat = np.array( Vsat )
    Psun = np.array( Psun )   

    Psun_norm = Psun / np.linalg.norm(Psun)
    
    S = geok.ECI2RTN_or_RPY(Psat,Vsat,Psun_norm,out_rpy=1)
    AY1 = -S[1] / np.sqrt(1- S[2]**2)
    AY2 = -S[0] / np.sqrt(1- S[2]**2)
    PSI_IOV = np.arctan2(AY1,AY2)
    
    return PSI_IOV


def yaw_nominal_gal_foc(Psat,Vsat,Psun):
        
    # discont see read data for beta angle py
    Psat = np.array( Psat )
    Vsat = np.array( Vsat )
    Psun = np.array( Psun )   
    
    Psat_norm = Psat / np.linalg.norm(Psat)
    Vsat_norm = Vsat / np.linalg.norm(Vsat)
    Psun_norm = Psun / np.linalg.norm(Psun)
    N_norm    = np.cross(Psat_norm,Vsat_norm)
    
    AT1 = np.dot(Psun_norm,N_norm)
    AT2 = np.dot(Psun_norm,np.cross(Psat_norm,N_norm))
    PSI_FOC = np.arctan2(AT1,AT2)
    
    return PSI_FOC

    

from numpy import radians
from scipy.constants import kilo

from orbital import earth, KeplerianElements, Maneuver, plot, plot3d

# Create molniya orbit from period and eccentricity
from orbital import earth_sidereal_day
molniya = KeplerianElements.with_period(
    earth_sidereal_day / 2, e=0.741, i=radians(63.4), arg_pe=radians(270),
    body=earth)

molniya2 = KeplerianElements.with_period(
    earth_sidereal_day / 2, e=0.741, i=radians(63.4), arg_pe=radians(270),
    body=earth,raan=list(range(10)))


# Simple circular orbit
orbit = KeplerianElements.with_altitude(1000 * kilo, body=earth)

plot3d(molniya)
plot3d(molniya2)


import matplotlib.pyplot as plt

plt.gcf()

plt.axis('equal')