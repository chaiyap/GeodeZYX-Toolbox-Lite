#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:28:46 2018

@author: psakicki
"""

from megalib import *

snx1 = "/home/psakicki/aaa_FOURBI/COMPAR_BUG_UPDATE_TMP/2018_107/OUT_PROD/2018_107_prod.snx"
snx2 = "/home/psakicki/aaa_FOURBI/COMPAR_BUG_UPDATE_TMP/2018_107_run1/OUT_PROD/2018_107_prod.snx"

A = gcls.compar_sinex( snx1 , snx2 , out_meta=1,manu_wwwwd="19972",
                      out_means_summary=1)