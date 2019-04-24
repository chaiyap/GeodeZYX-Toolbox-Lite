#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:19:22 2018

@author: psakicki
"""

import matplotlib.pyplot as plt
plt.style.use("file:///home/psakicki/.config/matplotlib/matplotlibrc_GFZStyle_moded1")
plt.style.use("file:///home/psakicki/.config/matplotlib/matplotlibrc_GFZStyle_GOOD2_EGU18")

from megalib import *
import pandas as pd

from matplotlib.ticker import MultipleLocator, FormatStrFormatter


# ==== COLOR DEFINITION =====

pXlist  = ('p1_','p2_', 'p3_',"cor","igr")
pXcolor = ("#40E0D0",
"#FF00FF",
"#FF0000",
"#006400",
"#4169E1")  

alternat_name_dic = dict()

alternat_name_dic['p1_'] = "GFZ"
alternat_name_dic['p2_'] = "ESOC"
alternat_name_dic['p3_'] = "Bern Obs."
alternat_name_dic["cor"] = "Rapid Combi."

colordict = dict()

for pX , col in zip(pXlist,pXcolor):
    colordict[pX] = col 

# ==== COLOR DEFINITION =====

period_start = 1660
period_end   = 1983

outdir = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/Plots/OrbClk"
outdir = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/Plots/OrbClk_reboot_for_test_only_mod1"

gf.create_dir(outdir)

bool_batch  = 1
bool_cut_y  = 1

bool_x_label_datetime = True


if not bool_batch:
    boolGAL     = 0
    boolCLK     = 1
    boolCLK_STD = 1

    boolGAL_iter = [boolGAL]
    boolCLK_iter = [boolCLK]
    boolCLK_STD_iter  = [boolCLK_STD]

else:

    boolGAL_iter      = [True , False]
    boolCLK_iter      = [True , False]
    boolCLK_STD_iter  = [True , False]    

    
BatchIterator = itertools.product(boolGAL_iter , boolCLK_iter , boolCLK_STD_iter)
#BatchIterator = []

for boolGAL , boolCLK , boolCLK_STD in BatchIterator:
    
    plt.close("all")
    plt.clf()
    
    if boolGAL:
        GPSGAL = "_GAL"  
        title_GPSGAL = "- GALILEO Satellites"
        pXlist  = ('p1_', 'p2_', 'p3_',"cor")
        
    else:
        GPSGAL = "_GPS"
        title_GPSGAL = "- GPS Satellites"
        pXlist  = ( 'p2_', 'p3_',"cor","igr", 'p1_')
    
    if not boolCLK:
        title_main = "Orbits RMS"
        ylabel = "Orbits RMS [mm]"
        if boolGAL:
            ylim = 200  
        else:
            ylim  = 20
    
    else:
        if boolCLK_STD:
            title_main = "Clocks Std. Dev."
            ylabel     = "Clocks STD [ps]"
    
            if boolGAL:
                ylim  = 40       
            else:
                ylim  = 40        
            
            
        else:
            title_main = "Clocks RMS"
            ylabel     = "Clocks RMS [ps]"
    
            if boolGAL:
                ylim = 70 
            else:
                ylim = 70
    
    pclk = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/DataPython/DataClk" + GPSGAL + ".pik"
    porb = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/DataPython/DataOrb" + GPSGAL + ".pik"
    
    if boolCLK:
        p = pclk
    else:
        p = porb
    
    
    Data = gf.pickle_loader(p)
    
    plt.close("all")
    

    fig , ax = plt.subplots()
    
    for pXiter in pXlist:  
        
        MJDstk , VALstk = [] , []
                
        Data_pX  = Data[(Data[2] == pXiter) & (np.logical_not(np.isnan(Data[3]))) & (pd.to_numeric(Data[0]) >= period_start) & (pd.to_numeric(Data[0]) <= period_end)] 
        
        if len(Data_pX) == 0:
            continue
        
        start = geok.dt2MJD(geok.gpstime2dt(int(Data_pX[0].iloc[0]) ,Data_pX[1].iloc[0] ))
        end   = geok.dt2MJD(geok.gpstime2dt(int(Data_pX[0].iloc[-1]),Data_pX[1].iloc[-1]))
    
        for index , l in Data_pX.iterrows():    
    
            week = l[0]
            d    = l[1]
            pX   = l[2]
            
            if np.isnan(l[3]):
                continue
            
            if pXiter != pX:
                continue
    
            mjd = geok.dt2MJD(geok.gpstime2dt(int(l[0]),l[1])) + .5
            
            if not boolCLK:
                val = l[3]
            else:
                if boolCLK_STD:
                    val = l[4]
                else:
                    val = l[3]
                    
            MJDstk.append(mjd)
            VALstk.append(val)
    
        win  = 7
        win2 = 3
                    
            #VALstk = np.array(outData["RMS"])
            #MJDstk = np.array(outData["MJD"])  
            
        VALstk = np.array(VALstk)
        MJDstk = np.array(MJDstk)    
        
        
        if bool_cut_y:
            boolkeep = np.array(VALstk) <= ylim
        else:
            boolkeep = np.array([True]* len(VALstk)) 
            
        VALstk2 = VALstk[boolkeep]
        MJDstk2 = MJDstk[boolkeep]
        
        #VALstk2 , MJDstk2  = geok.outlier_mad_binom(VALstk2 , MJDstk2)
        
        VALstk3 = geok.gaussian_filter_GFZ_style_smoother_improved(MJDstk2,VALstk2,win)
        VALstk3 = geok.gaussian_filter_GFZ_style_smoother_improved(MJDstk2,VALstk3,win2)
        
        T3 = geok.dt2gpsweek_decimal(geok.MJD2dt(MJDstk2))
        T  = geok.dt2gpsweek_decimal(geok.MJD2dt(MJDstk))
    
        #plt.plot(T,VALstk2,".",c=colordict[pX],label=pX.upper())
      
        if 0:
            ax.plot(T,VALstk,".",c=colordict[pX])    
        if not bool_x_label_datetime:
            ax.plot(T3,VALstk3,c=colordict[pX],label=pX.upper())
            ax.set_xlim(period_start,period_end)
            
            majorLocator   = MultipleLocator(20)
            majorFormatter = FormatStrFormatter('%d')
            minorLocator   = MultipleLocator(2)
            
            ax.xaxis.set_major_locator(majorLocator)
            ax.xaxis.set_major_formatter(majorFormatter)
            # for the minor ticks, use no labels; default NullFormatter
            ax.xaxis.set_minor_locator(minorLocator)
            
            #majorLocatorY   = MultipleLocator(20)
            #majorFormatterY = FormatStrFormatter('%d')
            minorLocatorY   = MultipleLocator(5)
            
            #ax.yaxis.set_major_locator(majorLocatorY)
            #ax.yaxis.set_major_formatter(majorFormatterY)
            ax.yaxis.set_minor_locator(minorLocatorY)    

            ax.set_xlabel("Time [GPS weeks]")       

        else:
            period_start_dt,period_end_dt = geok.gpstime2dt(period_start,0),geok.gpstime2dt(period_end,0)
            ax.plot(geok.MJD2dt(MJDstk2),VALstk3,c=colordict[pX],label=alternat_name_dic[pX])
            ax.set_xlim(period_start_dt,period_end_dt) 
            
        ax.set_ylim(0,ylim)                
    
         
    ax.set_ylabel(ylabel)                
    ax.set_title("Final " + title_main + " (PFs w.r.t. Final Combi.) " + title_GPSGAL)   

    koef = 2
    Len = (19.9/2.54) * koef
    Hei = (9.6/2.54) * koef
    fig.set_size_inches((Len,Hei))
    fig.patch.set_alpha(0)

    leg = ax.legend()  
    for line,text in zip(leg.get_lines(), leg.get_texts()):
        text.set_color(line.get_color())


    outplt = os.path.join(outdir, title_main.replace(" ","_") + title_GPSGAL.replace(" ","_") )
    for ext in (".svg" , ".png" , ".pdf"):
        plt.savefig(outplt + ext,bbox_inches='tight')             
                        

#%%

if True: #Plot Sat
    fignbsat , axnbsat = plt.subplots()
    
    porb = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/DataPython/DataOrb" + "_GAL" + ".pik"
    
    
    Data = gf.pickle_loader(porb)
    
    
    mpl.rcParams['lines.linewidth'] = 3

    existdate = []
    lastnbsat = 0
    
    Xnbsat = []
    Ynbsat = []
    
    for _, l in Data.iterrows():
        D = geok.gpstime2dt(int(l[0]),l[1])
        if 1: #l[4] >= lastnbsat: #not D in existdate and
            existdate.append(D)
            #axnbsat.plot(geok.dt2gpsweek_decimal(D),l[4],"k")
            Xnbsat.append(geok.dt2gpsweek_decimal(D))
            Ynbsat.append(l[4])
            if l[4] > lastnbsat:
                lastnbsat = l[4]
                
    axnbsat.plot(Xnbsat,Ynbsat,"g")
    LaunchList_Soyouz=["2011-10-21",
    "2012-10-12",
    "2014-08-22",
    "2015-03-27",
    "2015-09-11",
    "2015-12-17",
    "2016-05-24"]
    
    LaunchList_Ariane=["2016-11-17",
    "2017-12-12"]
    
    for ll in LaunchList_Soyouz:
        axnbsat.axvline(geok.dt2gpsweek_decimal(geok.date_string_2_dt(ll)),c="r")
    
    for ll in LaunchList_Ariane:
        axnbsat.axvline(geok.dt2gpsweek_decimal(geok.date_string_2_dt(ll)),c="b")
        
    axnbsat.set_xlabel("Time [GPS weeks]")                
    axnbsat.set_ylabel("Nb. of Galileo \n Sat. Available")   
    
    axnbsat.set_xlim(period_start,period_end) 

    
    majorLocator   = MultipleLocator(20)
    majorFormatter = FormatStrFormatter('%d')
    minorLocator   = MultipleLocator(2)
    
    axnbsat.xaxis.set_major_locator(majorLocator)
    axnbsat.xaxis.set_major_formatter(majorFormatter)
    # for the minor ticks, use no labels; default NullFormatter
    axnbsat.xaxis.set_minor_locator(minorLocator)
    
    #majorLocatorY   = MultipleLocator(20)
    #majorFormatterY = FormatStrFormatter('%d')
    minorLocatorY   = MultipleLocator(1)
    
    #ax.yaxis.set_major_locator(majorLocatorY)
    #ax.yaxis.set_major_formatter(majorFormatterY)
    axnbsat.yaxis.set_minor_locator(minorLocatorY)    
        
    axnbsat.set_title("Galileo Satellites Availability")   

    koef = 2
    Len = (19.9/2.54) * koef
    Hei = (9.6/2.54) * koef  * .7
    fignbsat.set_size_inches((Len,Hei))
    plt.tight_layout()
    fignbsat.patch.set_alpha(0)
    
    outplt = os.path.join(outdir, "Sats_GAL_Avail")
    for ext in (".svg" , ".png" , ".pdf"):
        plt.savefig(outplt + ext,bbox_inches='tight')    
    
    
                
        
        