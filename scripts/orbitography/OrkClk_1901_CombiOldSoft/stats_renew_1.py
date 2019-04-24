#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:52:20 2019

@author: psakicki
"""
import matplotlib.pyplot as plt
plt.style.use("file:///home/psakicki/.config/matplotlib/matplotlibrc_GFZStyle_moded_HTrans")

from megalib import *

pd.option_context('display.max_rows', None, 'display.max_columns', None)

path_root = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/0000_Combination_MGEX/1901_PlotsReboot/00_SycroFromServer/"

folder_exp = "12_decimates_clk_at_5min"

path_work = os.path.join(path_root,folder_exp)

LFILES = gf.find_recursive(path_work,"*")

Files_cls = [e for e in LFILES      if re.search("cls$",e)]
Files_sum = [e for e in LFILES      if re.search("sum$",e)]
Files_sum_full = [e for e in LFILES if re.search("sum_full$",e)]

COLOR = {
        "com": "#e41a1c"    , "gbm": "#4daf4a"     , "grm" : "xkcd:light blue",
        "jam": "xkcd:orange", "wum": "xkcd:bright blue" , "igs" : "xkcd:navy blue",
        "cmg": "xkcd:orange", "brd":"xkcd:black", "igr" : "xkcd:sky blue"
}

#### LOADING
DFexclu_stk = []
for f_sum in Files_sum:
    DFexclu_stk.append(gcls.read_combi_sum_exclu(f_sum))
    
DFexclu = pd.concat(DFexclu_stk,sort=True)


DFsumfull_stk = []
for f_sum_full in Files_sum_full:
    DFsumfull = gcls.read_combi_sum_full(f_sum_full,RMS_lines_output=True,
                             convert_prn_int_2_str=True)
# Date are stored in :
#    DF.date_mjd
#    DF.date_dt  
#    DF.date_gps
    
    DFsumfull_stk.append(DFsumfull)


DFclk_stk = []
for f_cls in Files_cls:
    DFclk_mono = gcls.read_combi_clk_rms(f_cls)
    DFclk_stk.append(DFclk_mono)

DFclk = pd.concat(DFclk_stk,sort=True)
    
#### PROCESSING ORBITS
#%%
if 1:
    clean_mode = ("logs","outlier_simple")
    clean_mode = ("outlier_simple")
    
    
    DFrms_stk = []
    
    Constell_select = ("E",)
    Constell_select = ("G",)
    Constell_select = ("J",)
    
    trigger = 1.
    trigger = .2
    
    for DFsumfull in DFsumfull_stk:
        Bool_Const = DFsumfull["CONST"].isin(Constell_select)
        
        Selected_AC   = [e for e in DFsumfull.columns if re.search("^[a-z]{3}$",e)]
        
        DFsumfull_wrk = DFsumfull[Selected_AC]
        DFsumfull_wrk = DFsumfull_wrk[Bool_Const]
    
        DFsumfull_wrk[np.isclose(0,DFsumfull_wrk)] = 0.
    
        if "logs" in clean_mode:
            DFexclu_day = DFexclu.loc[DFsumfull.date_dt] == True
            DFsumfull_wrk[DFexclu_day[DFsumfull_wrk.index] == False] = np.nan
        if "outlier_simple" in clean_mode:
            DFsumfull_wrk[np.abs(DFsumfull_wrk) > trigger] = np.nan ## ON a des fois des trucs negatifs oO dt.datetime(2018,4,8)
            
        Serie_rms = DFsumfull_wrk.apply(geok.rms_mean)
        DFrms = pd.DataFrame(Serie_rms).transpose()
        DFrms.date_dt = DFsumfull.date_dt
        DFrms.index =  [DFsumfull.date_dt]
        
        print(DFsumfull.date_dt)
        
        DFrms_stk.append(DFrms)
                
        [e.date_dt for e in DFrms_stk]
        
    #%%
    #for ac in Selected_AC:
            
    DF_summary = pd.concat(DFrms_stk,sort=True)
    
    fig , ax = plt.subplots()
    
    for ac in DF_summary.columns:
        #Traw       = DF_summary.index
        ACdata_raw = DF_summary[ac]
        
        Splot = ACdata_raw[np.logical_not(np.isnan(ACdata_raw))]
        if len(Splot) > 0:     
            
            Splot = Splot[np.logical_not(np.isclose(Splot,0))]
            
            Traw_dt  = Splot.index
            Traw_mjd = geok.dt2MJD(Traw_dt)
            Traw_gps = geok.dt2gpsweek_decimal(Traw_dt)
            Yraw = Splot.values
            
            Ysmooth = geok.gaussian_filter_GFZ_style_smoother_improved(Traw_mjd,
                                                                       Yraw,7)
            Tplot = Traw_gps
    
            color = COLOR[ac]
            ax.plot(Tplot,Ysmooth,c=color,label=ac)        
            ax.plot(Tplot,Yraw,'.',c=color,markersize=0.5)
            plt.legend()
      
#%%
if 1: 
    
    fig , ax = plt.subplots()
    

    DFclk_wrk = DFclk[Selected_AC]
    
    for ac in DFclk_wrk.columns:
        ACdata_raw = DFclk_wrk[ac]
        
        Splot = ACdata_raw[np.logical_not(np.isnan(ACdata_raw))]
        
        if len(Splot) > 0:     
            
            Splot = Splot[np.logical_not(np.isclose(Splot,0))]
            
            Traw_dt  = Splot.index
            Traw_mjd = geok.dt2MJD(Traw_dt)
            Traw_gps = geok.dt2gpsweek_decimal(Traw_dt)
            Yraw = Splot.values
            
            Ysmooth = geok.gaussian_filter_GFZ_style_smoother_improved(Traw_mjd,
                                                                       Yraw,7)
            Tplot = Traw_dt
    
            color = COLOR[ac]
            ax.plot(Tplot,Ysmooth,c=color,label=ac)        
            ax.plot(Tplot,Yraw,'.',c=color,markersize=0.5)
            plt.legend(ncol=2)
            
    ax.set_ylim(0,1000)
    
    ax.set_title("Final Clocks RMS - All Satellites")
    ax.set_xlabel("Days")
    ax.set_ylabel("RMS (ps)")
    
    plt.savefig("/home/psakicki/GFZ_WORK/RENDU/1902_SeminaireLR/" + "RMSclk.png")
    
