#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:06:07 2018

@author: psakicki

This script is for testing the smoothing fct

"""

from   megalib import *
import pandas as pd

p = "/home/psakicki/aaa_FOURBI/TMP_SUM_files_GGSP_4_EGU_Poster/sum_file_ORIG/sum_final_p1_.plt"

D = pd.read_table(p,delim_whitespace = True,skipfooter=5,skiprows=[0,1,2,3,4,6],header=0)

pclk = '/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/DataPython/DataClk_GPS.pik'
Data = gf.pickle_loader(pclk)
Data = Data[Data[2] == "p1_"]

win  = 7
win2 = 3

nam = "RMS.1"
np.array(D["RMS.1"])

nam = "STDDEV"
np.array(D["STDDEV"])

VALstk = np.array(D[nam])


col=4
nam = "col" + str(col)
VALstk = np.array(Data[col][len(Data[4]) - len(D):])
MJDstk = np.array(D["MJD"])      

if nam == "RMS.1":
    boolkeep = np.array(VALstk) <= 999999
else:
    boolkeep = np.array(VALstk) < 9999999  # <= 0.5
    
VALstk2 = VALstk[boolkeep]
MJDstk2 = MJDstk[boolkeep]

VALstk3 = geok.gaussian_filter_GFZ_style_smoother(MJDstk2,VALstk2,win)
VALstk3 = geok.gaussian_filter_GFZ_style_smoother(MJDstk2,VALstk3,win2)

T3 = geok.dt2gpsweek_decimal(geok.MJD2dt(MJDstk2))
T  = geok.dt2gpsweek_decimal(geok.MJD2dt(MJDstk))



plt.plot(T3,VALstk3)
plt.suptitle(nam)
#plt.plot(D["MJD"],D["STDDEV"])