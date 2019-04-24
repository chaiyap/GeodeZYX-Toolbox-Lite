#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:24:18 2017

@author: adminuser
"""

from megalib import *

rmsstk     = []
rmsstk_sat = []
rmsstk_sta = []
date_stk   = []
DFdiff_stk = []

print('name of the pickle changed ?')

for wk in range(1900,1974):
    for dow in range(7):
        
        wwwwd = str(wk) + str(dow)
        
        print(wwwwd)

        f1 = '/home/adminuser/Documents/RMS_rapid_clock/orbs_raw/combi_rapid_clk/w' + str(wk) +'/crr' + wwwwd + '.clk'
        f2 = '/home/adminuser/Documents/RMS_rapid_clock/orbs_raw/p1p2p3_rapid_clk/w' + str(wk) +'/p3r' + wwwwd + '.clk'
        
        DFdiff = gcls.clk_diff(f1,f2)
        DFdiff_stk.append(DFdiff)

if 1:
    gf.pickle_saver(DFdiff_stk,'/home/adminuser/Documents/RMS_rapid_clock/','crr_p3_diff_stk')





