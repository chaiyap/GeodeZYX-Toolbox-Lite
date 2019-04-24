# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:07:07 2016

@author: psakicki
"""

from megalib import *

# Sonardyne coords of the Beacons
A = np.array([[4593299.0931,632159.1592,4361699.9139],
[4592303.7621, 632242.0101,4362701.9719],
[4593868.8189, 630763.9603,4361311.4646],
[4593819.2648, 633423.1471,4360990.9815]])


GRASvel = (-0.0133 , 0.0188  , 0.0120)
NICAvel = (-0.0133 , 0.0190  , 0.0113)

FINAL_EPOCH = geok.dt2year_decimal(dt.datetime(2015,6,21))

B = []

for a in A:
    geok.helmert_trans(a,invert=1)
    argz = tuple(geok.helmert_trans(a,invert=1)) + (2009.0,) + NICAvel + (FINAL_EPOCH,)

    B.append(geok.itrf_speed_calc(*argz))

x0 ,y0 , z0 =   4595047.79934 , 632288.017869 , 4363273.52335
xyz0        = [ 4595047.79934 , 632288.017869 , 4363273.52335 ]

B0 = np.vstack(B)

np.column_stack(geok.XYZ2GEO(B0[:,0],B0[:,1],B0[:,2]))
C = np.stack(geok.XYZ2ENU_2( B0[:,0] , B0[:,1] , B0[:,2] , x0 ,y0 , z0)).T
C2 = np.dot(C,geok.C_enu2ned())


Bary_sonar_XYZ = geok.barycenter(B0[1:,])
Bary_sonar_FLH = geok.XYZ2GEO(*Bary_sonar_XYZ)

Bary_sonar_ENU = geok.XYZ2ENU_2( Bary_sonar_XYZ[0] , Bary_sonar_XYZ[1] ,
                                Bary_sonar_XYZ[2] , x0 ,y0 , z0)


Bary_sonar = geok.barycenter(C2[1:,])
Bary_nous  = np.array([   18.11865498  ,  91.1400511 ,  2388.86919509])
Bary_nous - Bary_sonar 
