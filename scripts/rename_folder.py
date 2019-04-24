#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:06:36 2019

@author: psakicki
"""

from megalib import *

p = "/dsk/mansur/MGEX/ARCHIVE_PROD_REPRO2/products"

L = glob.glob(p + "/wk*")

for l in L:
    b = os.path.basename(l)
    d = os.path.dirname(l)
    os.chdir(d)
    if len(b) < 6:
        bnew = b[0:2] + "0" + b[2:]
        print(b,bnew)
        os.rename(b,bnew)
        
        
