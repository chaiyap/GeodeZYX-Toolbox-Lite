# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:39:27 2015

@author: psakicki
"""

import genefun
import matplotlib.pyplot as plt
import geoclass
import geodetik
import datetime as dt
import os
import glob
import itertools


data_gins_path = '/home/psakicki/gin/TP/GWADA/RESULTS/FLH_mk2/GINS/extracted/'
raw_plot_path = '/home/psakicki/gin/TP/GWADA/WORKING_MK2/RAW_PLOT/'
raw_plot_calais_path = '/home/psakicki/gin/TP/GWADA/WORKING_MK2/RAW_PLOT/calais'

statlis = ["ABMF","DHS0", 'BDOS' ,"ADE0", "ASF0", "CBE0", "DSD0", "FFE0", "FNA0", "FSDC", "HOUE", "LAM0", "MGL0", "PDB0", "PSA1", "SOUF"]
statlis = ['ABER','ABMF','ADE0','BDOS','BOUL','CBE0','DESI','DHS0','DSD0','FFE0','FNA0','FSDC','GOSI','HOUE','LAM0','LORI','MGL0','PSA1','SOUF','TRIL']
#statlis = ['MARI','SOUF']
#statlis = ['ABD0']

#geodetik.rinex_timeline('/home/psakicki/gin/TP/GWADA/RINX2')
geodetik.listing_gins_timeline('/home/psakicki/gin/TP/GWADA/RESULTS/FLH_mk2/GINS',15,19,24,29,'GWADA_MK2_FLH__')

tslist = []
for stat in statlis: 
    listfile = genefun.regex2filelist(data_gins_path,'.*' + stat)
    tsgwada = geoclass.read_gins_multi_extracted(listfile) 
    mp = tsgwada.mean_posi()
    disc = geoclass.read_station_info_time_solo('/home/psakicki/gin/TP/GWADA/station.info.ovsg.volobsis.discont',stat)[0]

    tsgwada.set_discont(disc)
    tsgwada.ENUcalc(mp)
    
# ===== SPECIFIC GESTION =====
    if tsgwada.stat == 'DHS0':
        win = [[dt.datetime(2011,8,9),dt.datetime(2099,1,1)]]
        tsgwada.timewin(win,mode='keep')
    if stat in ('MAGA','PDB0','ASF0'):
        continue
   
    tsgwada = geoclass.sigma_cleaner(tsgwada,2,cleantype='any') 
    tsgwada = geoclass.mad_cleaner(tsgwada,3,'dist')
#
## ===== PLOT =====
#    geoclass.export_ts_plot(tsgwada,raw_plot_path)
#    
# ====== EXPORT ======
#    geoclass.export_ts_as_neu(tsgwada,'/home/psakicki/gin/TP/GWADA/WORKING_MK2/RAW_NEU','gwada_2_')
    tslist.append(tsgwada)


calais_path = "/home/psakicki/gin/TP/GWADA/WORKING_MK2/DATA_CALAIS"
tscalaislist = []
for stat in statlis: 
    listoffiles = glob.glob(os.path.join(calais_path,stat + '*'))
    print(stat,listoffiles)
    if listoffiles == []:
        continue
    tscalais = geoclass.read_calais(listoffiles)
    
    tscalais = geoclass.sigma_cleaner(tscalais,2,cleantype='any') 
    tscalais = geoclass.mad_cleaner(tscalais,3,'dist')
    
#    tscalais.plot()
#    geoclass.export_ts_plot(tscalais,raw_plot_calais_path)
    tscalaislist.append(tscalais)
    
compar_path_ss_delta = "/home/psakicki/gin/TP/GWADA/WORKING_MK2/RAW_PLOT/COMPAR_ss_DELTA"
compar_path_ac_delta = "/home/psakicki/gin/TP/GWADA/WORKING_MK2/RAW_PLOT/COMPAR_ac_DELTA"

for ec,ps in itertools.product(tscalaislist,tslist):
    if ps.stat == ec.stat:
        # ss delta
        f = plt.figure()
        ps3 = geoclass.merge(ps,7)
        ps3.plot(fig=f,errbar = False)
        ec.plot(fig=f,errbar = False)
        geoclass.export_ts_figure_pdf(f,compar_path_ss_delta,ps.stat,close=True)
        # ac delta
        ff = plt.figure()
        coeff_ps = geoclass.linear_regress_find_coeff(ps3)
        coeff_ec = geoclass.linear_regress_find_coeff(ec)
        delta = [ (cec[1] - cps[1]) for cps,cec in zip(coeff_ps,coeff_ec) ]
        ps4 = geoclass.add_offset_ts(ps3,*delta)
        ps4.plot(fig=ff,errbar = False)
        ec.plot(fig=ff,errbar = False)
#        geoclass.export_ts_figure_pdf(ff,compar_path_ac_delta,ps.stat,close=True)


