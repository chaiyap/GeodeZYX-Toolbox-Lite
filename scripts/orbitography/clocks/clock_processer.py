#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:08:31 2017

@author: adminuser
"""

from megalib import *

DFdiff_stk = gf.pickle_loader('/home/adminuser/Documents/RMS_rapid_clock/crr_p3_diff_stk.pik')

rmsstk_all     = []
rmsstk_sat     = []
rmsstk_sta     = []
date_stk       = []

rmsstk_alt_all = []
rmsstk_alt_sat = []
rmsstk_alt_sta = []   

for DFdiff in DFdiff_stk:
    print(DFdiff['date'][0].to_pydatetime().date())
    date_stk.append(DFdiff['date'][0].to_pydatetime().date())
    
    All = DFdiff['diff']
    Sta = DFdiff[DFdiff['type'] == 'AR']['diff']
    Sat = DFdiff[DFdiff['type'] == 'AS']['diff']
    
    rmsstk_all.append(geok.rms_mean(All))
    rmsstk_sta.append(geok.rms_mean(Sta))
    rmsstk_sat.append(geok.rms_mean(Sat))
    
    rmsstk_alt_all.append(geok.rms_mean_alternativ(All))
    rmsstk_alt_sta.append(geok.rms_mean_alternativ(Sta))
    rmsstk_alt_sat.append(geok.rms_mean_alternativ(Sat))
    

DF = pd.DataFrame(list(zip(rmsstk_all,
                      rmsstk_sta,
                      rmsstk_sat,
                      rmsstk_alt_all,
                      rmsstk_alt_sta,
                      rmsstk_alt_sat)),
                  index = date_stk)


for i in range(6):
    plt.figure()
    geok.outiler_mad(DF[i],convert_to_np_array=False)[0].plot(marker='.')


#plt.plot(*geok.outlier_mad_binom(DF[3],DF[0]))
#plt.plot(date_stk, rmsstk_alt_all)
#plt.plot(date_stk, rmsstk_alt_all)
#    