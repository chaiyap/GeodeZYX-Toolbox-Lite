# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:52:35 2016

@author: psakicki
"""

from tabulate import tabulate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from megalib import *

STAT = 'ensg'
STAT = 'umrb'

if STAT == 'ensg':
    ref    = np.array([4201575.85487 ,   189861.53838  , 4779065.51962])
    ref_pt = gcls.Point(ref[0],ref[1],ref[2],0,'XYZ')
    
    path_rtklib = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/RTKLIB/*out"
    path_gipsy  = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/GIPSYAPPS/*/*sum"
    path_nrcan  = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/NRCAN/ensg2500.pos"
    path_track  = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACKBADOFFSET2/*ENSG.LC'
    path_track  = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK/*250*ENSG.LC'
    path_track_short  = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK_shortmode/*250*ENSG.L1+L2'
    path_track_long   = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK_longmode/*250*ENSG.LC'
    
    path_gins_kf0 = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/GINS_KF0/*gins'
    path_gins_kf1 = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/GINS_KF1/*gins' 
    
    outpath = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/'
    
if STAT == 'umrb':
    path_rtklib = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/RTKLIB/OUTPUT/UMRB/87/*out"
    path_gipsy  = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/GIPSY/2012-03-27.UMRB/2012-03-27.UMRB*tdp"
    path_nrcan  = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/NRCAN/UMRB/87/UMRB0870.pos"
    path_track  = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/TRACK/OUTPUT/UMRB/87/*" +  STAT.upper()  + '.LC'
    path_track_short  = '/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/TRACK_REBOOT1sec_short/OUTPUT/*' +  STAT.upper()  + '.L1+L2'
    path_track_long   = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/TRACK_REBOOT1sec_long/OUTPUT/*" +  STAT.upper()  + '.LC'
    
    path_gins_kf0 = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/GINS/KF0/UMRB/*gins"
    outpath       = '/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/'
    path_gins_kf1 = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/GINS/KF1/*UMRB*gins"

#if STAT == 'umrb':
    path_rtklib = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/RTKLIB/OUTPUT/UMRB/87/*out"
    path_gipsy  = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/GIPSY/2012-03-27.UMRB/2012-03-27.UMRB*tdp"
    path_nrcan  = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/NRCAN/UMRB/87/UMRB0870.pos"
    path_track  = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/TRACK/OUTPUT/UMRB/87/*" +  STAT.upper()  + '.LC'
    path_track_short  = '/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/TRACK_REBOOT1sec_short/OUTPUT/*' +  STAT.upper()  + '.L1+L2'
    path_track_long   = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/TRACK_REBOOT1sec_long/OUTPUT/*" +  STAT.upper()  + '.LC'
    
    path_gins_kf0 = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/GINS/KF0/UMRB/*gins"
    outpath       = '/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/'
    path_gins_kf1 = "/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/GINS/KF1/*UMRB*gins"

gf.create_dir(outpath)

reload(gcls)
datadict = dict()
namend   = 15
loading  = 0
plot     = 1
if plot:
    revers = 1 # true for plot, false for tab
else:
    revers = 0
#revers=0
with_decimate_after_loading = 0
after_loading_decimator     = 300

decimate_during_loading = 1
if not plot:
    loading_decimator       = 1
else:
    loading_decimator       = 60
    

diconame = 'dico' + str(loading_decimator)

plt.ioff()

if loading:
    tslist_track = []
    TRACK = glob.glob(path_track)
    if 1:
        print(" ===== TRACK ===== ")
        for f in TRACK:
            ts = gcls.read_all_points(f)
            if decimate_during_loading:
                ts.decimate(loading_decimator)
            #ts.name = 'diff. TRACK, base : ' + ts.name.split('_')[3].upper()
            ts.name = 'TRACK ' + ts.anex['base']
            print(ts)
            tslist_track.append(ts)
        datadict['TRACK'] = tslist_track
     
    tslist_track_short = []
    TRACK_SHORT = glob.glob(path_track_short)
    if 1:
        print(" ===== TRACK SHORT===== ")
        for f in TRACK_SHORT:
            ts = gcls.read_all_points(f)
            if decimate_during_loading:
                ts.decimate(loading_decimator)
            #ts.name = 'diff. TRACK, base : ' + ts.name.split('_')[3].upper()
            ts.name = 'TRACKshort ' + ts.anex['base']
            print(ts)
            tslist_track_short.append(ts)
        datadict['TRACK_SHORT'] = tslist_track_short

    tslist_track_long = []
    TRACK_LONG = glob.glob(path_track_long)
    if 1:
        print(" ===== TRACK LONG ===== ")
        for f in TRACK_LONG:
            ts = gcls.read_all_points(f)
            if decimate_during_loading:
                ts.decimate(loading_decimator)
            #ts.name = 'diff. TRACK, base : ' + ts.name.split('_')[3].upper()
            ts.name = 'TRACKlong ' + ts.anex['base']
            print(ts)
            tslist_track_long.append(ts)
        datadict['TRACK_LONG'] = tslist_track_long
        

        
    # Generate dico
    tslist_rtklib = []
    RTKLIB = glob.glob(path_rtklib)
    if 1:
        print(" ===== RTKLIB ===== ")
        for f in RTKLIB:
            print('rtklib file : ' , f)
            ts = gcls.read_all_points(f)
            if decimate_during_loading:
                ts.decimate(loading_decimator)
            ts.name = 'RTKLIB ' + ts.anex['base']
            tslist_rtklib.append(ts)
            print(ts)
        datadict['RTKLIB'] = tslist_rtklib
            

    tslist_gipsy = []
    GIPSY = glob.glob(path_gipsy)
    if 1:
        print(" ===== GIPSY ===== ")
        for f in GIPSY:
            ts = gcls.read_all_points(f)
            if decimate_during_loading:
                ts.decimate(loading_decimator)
            tslist_gipsy.append(ts)
            print(ts)
    
        ts_gipsy_raw = gcls.merge_ts(tslist_gipsy)
        if decimate_during_loading:
            ts_gipsy_raw.decimate(loading_decimator)
        ts_gipsy_raw.name = 'PPP GIPSY'
        ts_gipsy = ts_gipsy_raw
        datadict['GIPSY_RAW'] = ts_gipsy_raw
        datadict['GIPSY']     = ts_gipsy
    
    if 1:
        print(" ===== NRCAN ===== ")
        ts_nrcan = gcls.read_nrcan_pos(path_nrcan)
        if decimate_during_loading:
            ts_nrcan.decimate(loading_decimator)
        ts_nrcan.name = 'PPP NRCAN'
        print(ts)
        datadict['NRCAN'] = ts_nrcan
    
    reload(gcls)       
    tslist_gins_kf0 = []
    GINS_KF0 = sorted(glob.glob(path_gins_kf0))
    if 1:
        print(" ===== GINS_KF0 ===== ")
        ts = gcls.read_gins_multi_raw_listings(GINS_KF0,'kine')
        if decimate_during_loading:
            ts.decimate(loading_decimator)
        ts.name = 'PPP GINS KF0'
        ts_gins_kf0 = ts
        print(ts)
        datadict['GINS_KF0'] = ts_gins_kf0
    
    tslist_gins_kf1 = []
    GINS_KF1 = sorted(glob.glob(path_gins_kf1))
    if 1 and STAT == 'ensg':
        print(" ===== GINS_KF1 ===== ")
        ts = gcls.read_gins_multi_raw_listings(GINS_KF1,'kine')
        if decimate_during_loading:
            ts.decimate(loading_decimator)
        ts.name = 'PPP GINS KF1'
        ts_gins_kf1 = ts
        print(ts)
        datadict['GINS_KF1'] = ts_gins_kf1
    if 1:
        print("saving dic start")
        gf.pickle_saver(datadict, outpath , diconame)
        print("saving dic end")

else:
    if 1:
        print("loading dic start")
        datadict = gf.pickle_loader(outpath + diconame + '.pik')
        print("loading dic end  ")
    
tslist_proto = []
if 1:
    ts_gins_kf0   = datadict['GINS_KF0']
if STAT == 'ensg' and 0:
    ts_gins_kf1   = datadict['GINS_KF1']
ts_nrcan      = datadict['NRCAN']
tslist_rtklib = datadict['RTKLIB']
if STAT == 'umrb':
    tslist_rtklib_near = [ts for ts in datadict['RTKLIB'] if ts.anex['base'] in ('ANGL','ROYA','AUNI','ILDX')]
elif STAT == 'ensg':
    tslist_rtklib_near = [ts for ts in datadict['RTKLIB'] if ts.anex['base'] in ('MLVL','SMNE','SIRT')]
    
tslist_track  = datadict['TRACK']
ts_gipsy      = datadict['GIPSY']
ts_gipsy_raw  = datadict['GIPSY_RAW']
tslist_track_short  = datadict['TRACK_SHORT']
for ts in tslist_track_short:
    ts.name = 'TRACKshort ' + ts.name[-4:]
tslist_track_long = datadict['TRACK_LONG']

tslist_proto.append(ts_gins_kf0)
tslist_proto.append(ts_nrcan)
tslist_proto = tslist_proto + tslist_rtklib + tslist_rtklib_near
tslist_proto = tslist_proto + tslist_track
tslist_proto = tslist_proto + tslist_track_short
tslist_proto = tslist_proto + tslist_track_long
tslist_proto.append( ts_gipsy    )
tslist_proto.append( ts_gipsy_raw)

if with_decimate_after_loading:
    [tsss.decimate(after_loading_decimator) for tsss in tslist_proto]

if STAT == 'ensg':
    # sorting the bases
    dicobaseorder  = dict()
    dicobaseorder['MLVL'] = 0
    dicobaseorder['SMNE'] = 1
    dicobaseorder['SIRT'] = 2
    dicobaseorder['CHPH'] = 3
    dicobaseorder['MAN2'] = 4
    
    for tss in tslist_rtklib:            
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_rtklib.sort(key=lambda x: x.anex['order'], reverse=revers)

    for tss in tslist_track:
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_track.sort(key=lambda x: x.anex['order'] , reverse=revers)
   
    for tss in tslist_track_short:
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_track_short.sort(key=lambda x: x.anex['order'] , reverse=revers)
    
    for tss in tslist_track_long:
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_track_long.sort(key=lambda x: x.anex['order'] , reverse=revers)   
    
    if 0:
        tslist_mono = [ts_gipsy , ts_nrcan , ts_gins_kf0 ]
    else:
        tslist_mono = []
    
    ts_gipsy.ENUcalc(ref_pt)
    ts_gipsy_corr = gcls.add_offset_ts(ts_gipsy,0,0,-0.1223,'ENU')
    
    
    tslist_mono , tslistname_mono = [ ts_gins_kf0 , ts_nrcan , ts_gipsy_corr] , 'tslist_mono'
    tslistlist  , tslistnamelist = [] , []
    
    tslist , tslistname     = tslist_rtklib + tslist_track + tslist_mono , 'tsall'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_mono   , 'tslist_mono'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_track  , 'tslist_track'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_track_short  , 'tslist_track_short'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_track_long   , 'tslist_track_long'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_rtklib , 'tslist_rtklib'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_rtklib_near , 'tslist_rtklib_near'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)


    
    for tslist , tslistname  in zip(tslistlist , tslistnamelist):
        end   = np.max([ t.enddate()   for t in tslist ])
        strt  = np.min([ t.startdate() for t in tslist ])
        
        ts_ref = gcls.TimeSeriePoint()
        A = gcls.Point(ref[0],ref[1],ref[2],strt,'XYZ')
        B = gcls.Point(ref[0],ref[1],ref[2],end ,'XYZ')
        ts_ref.add_point(A)
        ts_ref.add_point(B)
        
        ts_ref.from_uniq_point(A,
                              tslist[0].startdate(),
                              tslist[0].enddate())
        ts_ref.ENUcalc(ref_pt)
        ts_ref.meta_set(name='true coords.' , stat=STAT.upper())
        
        #ts_ref = tslist_rtklib[0]
        
        tslist = [ts_ref] + tslist
        
        ref_pt = ts_ref.mean_posi()
        
        [t.ENUcalc(ref_pt) for t in tslist if t.name != 'PPP GIPSY']
        
        #plt.savefig('/home/psakicki/aaa_FOURBI/kompar.pdf')
        #plt.savefig('/home/psakicki/aaa_FOURBI/kompar.png')
        
        
        diccompar = gcls.compar(tslist,'ENU',plot=0, Dtype='2D3D')
        tab1,tab2 = gcls.print4compar_tabular(diccompar,10)
        tabprint1     = tabulate(tab1,headers="firstrow", tablefmt="fancy_grid" , floatfmt=".4f")
        tabprint_tex1 = tabulate(tab1,headers="firstrow", tablefmt="latex" , floatfmt=".4f")

        tabprint2     = tabulate(tab2,headers="firstrow", tablefmt="fancy_grid" , floatfmt=".4f")
        tabprint_tex2 = tabulate(tab2,headers="firstrow", tablefmt="latex" , floatfmt=".4f")

        
        
        outpath_plot = os.path.join(outpath,diconame)
        gf.create_dir(outpath_plot)
        print(outpath_plot)
        print(tabprint1)
        print(tabprint2)

        if plot:
            diccompar    = gcls.compar(tslist,'ENU',plot=0, Dtype='2D3D')
            gcls.compar_plot(diccompar,namend=namend)
            outpath_plot = os.path.join(outpath,diconame)
            gf.create_dir(outpath_plot)
            plt.savefig(os.path.join(outpath_plot,tslistname + '_' + diconame +'.png'))
            #plt.savefig(os.path.join(outpath_plot,tslistname + '_' + diconame +'.svg'))
            plt.savefig(os.path.join(outpath_plot,tslistname + '_' + diconame +'.pdf'))

            plt.clf()
        else:
            gf.write_in_file(tabprint1,outpath_plot,tslistname+ '_1')
            gf.write_in_file(tabprint2,outpath_plot,tslistname+ '_2')
            gf.write_in_file(tabprint_tex1,outpath_plot,tslistname + '_1_tex')
            gf.write_in_file(tabprint_tex2,outpath_plot,tslistname + '_2_tex')
            gf.write_in_file(tabprint_tex1 + '\n' + tabprint_tex2,
                             outpath_plot,tslistname + '_3_tex')

#%%
reload(gcls)
if STAT == 'umrb':
    ILDX2009 = [4436671.0119  ,  -91138.0528 ,  4566018.1505]
    ILDX     = np.array(geok.itrf_speed_calc(ILDX2009[0],ILDX2009[1],ILDX2009[2],
                                             2009.0,-0.0135 , 0.0196, 0.0094,
                                             geok.dt2year_decimal(geok.doy2dt(2012,87))))
                                             
    # sorting the bases
    dicobaseorder  = dict()
    dicobaseorder['ILDX'] = 0
    dicobaseorder['AUNI'] = 1
    dicobaseorder['ROYA'] = 2
    dicobaseorder['ANGL'] = 3
    dicobaseorder['MAN2'] = 5
    dicobaseorder['BRES'] = 4    
    dicobaseorder['CHPH'] = 6
    dicobaseorder['SMNE'] = 7
    
    for tss in tslist_rtklib:            
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_rtklib.sort(key=lambda x: x.anex['order'], reverse=revers)

    for tss in tslist_track:
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_track.sort(key=lambda x: x.anex['order'], reverse=revers)
    
    for tss in tslist_track_short:
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_track_short.sort(key=lambda x: x.anex['order'], reverse=revers)

    for tss in tslist_track_long:
        tss.anex['order']  = dicobaseorder[tss.anex['base']]
    tslist_track_long.sort(key=lambda x: x.anex['order'], reverse=revers)

    if 0:
        tslist_mono = [ts_gipsy , ts_nrcan , ts_gins_kf0 , ts_gins_kf1]
    else:
        tslist_mono = []
    
    #ts_gipsy.ENUcalc(ref_pt)
    #ts_gipsy_corr = gcls.add_offset_ts(ts_gipsy,0,0,-0.1223,'ENU')
 
    tslistlist  , tslistnamelist = [] , []

    tslist_mono = [ ts_gins_kf0 , ts_nrcan , ts_gipsy ]
    
    ts_gipsy2   = gcls.add_offset_ts(ts_gipsy,0,0,-10000,'UXYZ')
    
    tslist , tslistname     = tslist_rtklib_near , 'tslist_rtklib_near'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname = tslist_rtklib + tslist_track + tslist_mono , 'tsall'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_track_short  , 'tslist_track_short'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname     = tslist_track_long   , 'tslist_track_long'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname = [ts_gipsy , ts_gipsy2] , 'ts_gipsy'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname = tslist_track  + tslist_mono , 'tslist_trackmono'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname = tslist_mono   , 'tslist_mono'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname = tslist_rtklib , 'tslist_rtklib'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    tslist , tslistname = tslist_track  , 'tslist_track'
    tslistlist.append(tslist) , tslistnamelist.append(tslistname)
    
    if 'redux' in outpath:
        tslistlist  , tslistnamelist = [] , []

        track_short_mans2 = [ts for ts in tslist_track_short if 'MAN2' in ts.name][0]
        track_long_mans2  = [ts for ts in tslist_track_long  if 'MAN2' in ts.name][0]
        track_mans2       = [ts for ts in tslist_track       if 'MAN2' in ts.name][0]
        rtklib_mans2      = [ts for ts in tslist_rtklib      if 'MAN2' in ts.name][0]
        track_short_ildx  = [ts for ts in tslist_track_short if 'ILDX' in ts.name][0]

        tslist_redux = [track_mans2] + tslist_mono               
        tslist , tslistname = tslist_redux  , 'tslist_redux'
        tslistlist.append(tslist) , tslistnamelist.append(tslistname)

        matplotlib.rcParams.update({'font.size': 14})
    
    for tslist , tslistname  in zip(tslistlist , tslistnamelist):
        end   = np.max([ t.enddate()   for t in tslist ])
        strt  = np.min([ t.startdate() for t in tslist ])
        
        for tss in tslist:
            print(tss.nbpts)
        
        #ts_ref = gcls.TimeSeriePoint()
        #A = gcls.Point(ref[0],ref[1],ref[2],strt,'XYZ')
        #B = gcls.Point(ref[0],ref[1],ref[2],end ,'XYZ')
        #ts_ref.add_point(A)
        #ts_ref.add_point(B)
        ts_ref = [ts for ts in tslist_track if 'ILDX' in  ts.name][0]
        ts_ref = [ts for ts in tslist_track_short if 'ILDX' in  ts.name][0]

        
        tslist = [ts_ref] + tslist
        if tslistname == 'tslist_track':
            tslist = tslist[:-1]
        
        ref_pt = ts_ref.mean_posi()
        
        #for ts in tslist:
        #    ts.plot('XYZ')
        
         
        #[t.ENUcalc(ref_pt) for t in tslist if t.name != 'PPP GIPSY']
        
        refmob = 0
        if refmob:
            [t.ENUcalc(ts_ref) for t in tslist]
        else:
            [t.ENUcalc(ref_pt) for t in tslist]
            
        tslist[0][0].E
        
        #plt.savefig('/home/psakicki/aaa_FOURBI/kompar.pdf')
        #plt.savefig('/home/psakicki/aaa_FOURBI/kompar.png')
           
        diccompar = gcls.compar(tslist,'ENU',plot=0, Dtype='2D3D')
        outpath_plot = os.path.join(outpath,diconame)
        gf.create_dir(outpath_plot)

        if plot:
            matplotlib.rcParams.update({'font.size':17})
            diccompar    = gcls.compar(tslist,'ENU',plot=0, Dtype='2D3D')
            gcls.compar_plot(diccompar,namend=namend)
            outpath_plot = os.path.join(outpath,diconame)
            gf.create_dir(outpath_plot)
            f = plt.gcf()  # f = figure(n) if you know the figure number
            f.set_size_inches(11.69,16.53)
            plt.savefig(os.path.join(outpath_plot,tslistname + '_' + diconame +'.png'))
            plt.savefig(os.path.join(outpath_plot,tslistname + '_' + diconame +'.pdf'))
            plt.savefig(os.path.join(outpath_plot,tslistname + '_' + diconame +'.svg'))

            #plt.savefig(os.path.join(outpath_plot,tslistname + '_' + diconame +'.svg'))
            plt.clf()

