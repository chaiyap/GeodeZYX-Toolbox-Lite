# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:29:35 2016

@author: psakicki
"""

from megalib import *

sp3 = "/home/psakicki/aaa_FOURBI/igr18940.sp3"
clk = "/home/psakicki/aaa_FOURBI/igr18940.clk"
sp3 = "/home/psakicki/aaa_FOURBI/160428_SeismeLR/recherche_1/orbits/2016-04-28.sp3"


for l in open(sp3):
    if l[0] == '*':
        T = geok.datetime_improved(*[float(e) for e in l[1:].split()])
    if not 'PG' == l[0:2]:
        continue
    else:
        idsat  = int(l[2:4])
        deltat = float(l.split()[4]) * 10**-6
        
        print('{} G{:2}  {:4} {:2} {:2} {:2} {:2} {:9.6f}  2   {:19.12e} {:19.12e}'.format('AS',str(idsat).zfill(2),T.year,T.month,T.day,T.hour,T.minute,T.second,deltat,10**-11))
    
print("AR QAQ1 2016 04 24 15 15  0.000000  2    1.662582237550e-04  7.766620618350e-12")
print('AR RBAY 2016 04 24 15 15  0.000000  2   -3.399361719774e-08  1.467716900960e-11')
