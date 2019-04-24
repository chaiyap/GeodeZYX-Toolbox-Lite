#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:25:00 2017

@author: adminuser

This script read the clocks logs to get the RMS 
"""
# Removing variables 
#from IPython import get_ipython
#get_ipython().magic('reset -sf') 
#closing all figs
#plt.close('all')

from megalib import *

import matplotlib.pyplot as plt


p1 = '/home/adminuser/Documents/RMS_rapid_clock/clock_sum/*'

L = sorted(glob.glob(p1))

pftup = ('x11','x12','x13','x21','x31')


def read_cf_orb_clock_sum(file_in):
    fil = open(file_in)
    datadic = dict()

    for pf in pftup:
        datadic[pf] = np.nan

    for l in fil:
        if 'MJD:' in l:
            datadic['mjd'] = int(l.split()[-1])
        
        for pf in pftup:
            if ' ' + pf + ' |' in l:
                rms = int(l.split()[-4])
                datadic[pf] = rms
    return  datadic
                
            
            
dicstk = []
for f in L:
    D = read_cf_orb_clock_sum(f)
    dicstk.append(D)


DATA = dict(list(zip(dicstk[0],list(zip(*[list(d.values()) for d in dicstk])))))

        
#arr = np.vstack(sorted([ (e['mjd'],e['p1r'],e['p2r'],e['p3r']) for e in dicstk ], key=lambda tup: tup[0]))
#arr = np.vstack(sorted([ (e['mjd'],e['p1r'],e['p2r'],e['p3r']) for e in dicstk ], key=lambda tup: tup[0]))

for pf in pftup:
    plt.plot(DATA['mjd'],DATA[pf])
