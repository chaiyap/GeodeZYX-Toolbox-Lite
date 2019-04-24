#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 16:07:42 2018

@author: psakicki
"""

from megalib import *
import matplotlib.pyplot as plt
import matplotlib as mpl

path  = "/home/psakicki/aaa_FOURBI/TMP_SUM_files_GGSP_4_EGU_Poster/SNX_PF1_CS_TMP/"
path1 = "/home/psakicki/aaa_FOURBI/TMP_SUM_files_GGSP_4_EGU_Poster/SNX_PF1_CS_TMP/TAR/AC_CMB/CMB/SINEX/"
path2 = "/home/psakicki/aaa_FOURBI/TMP_SUM_files_GGSP_4_EGU_Poster/SNX_PF1_CS_TMP/TAR/PF1_PROD/SINEX/"

outdir = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/Plots/Coords_Stability"
    
bool_read_n_save              = 1
bool_extract_types_def_in_dic = 1
bool_plot_ENU3D = 0         # for just one simple selection
bool_plot_multi_enu2D3D = 1 # for a selection based on a more complex list / dict

### Generated using 
### /home/psakicki/CODES/geodezyx_toolbox_py3/scripts/GGRSP/misc/GGSP_extract_and_map_coords_from_CONTROL_files.py
stat_typ_path = "/home/psakicki/aaa_FOURBI/GGSP_stat_typ_dic.pik"

stat_typ      = gf.pickle_loader(stat_typ_path) 

if bool_read_n_save:

    if bool_extract_types_def_in_dic:
        stat_sel_list      = []
        stat_sel_name_list = []
        invert_select = 0

        for k , v in stat_typ.items():
            print("hard coded ratio (not reliable)", k,len(v) , float(len(v)) / 201.)
            stat_sel_name_list.append(k)
            stat_sel_list.append(gf.regex_OR_from_list([e[0] for e in v]))
        
        stat_sel_list.append(None)
        stat_sel_name_list.append("ALL")

    else:
        sta_sel = "S[0-9][0-9][A-Z]"
        sta_sel = None
        
        invert_select = 0

        stat_sel_list = [sta_sel] 
        stat_sel_name_list = ["NO_AUTO_SEL"]
    
    Adict = dict()
    for sta_sel , sta_sel_nam in zip(stat_sel_list,stat_sel_name_list):
        valstk = []
        
        for week in range(1660,2000):
            cslis = []
            p1lis = []
            cslis = sorted(glob.glob(path1 + "cs*" + str(week) + "*snx"))
            p1lis = sorted(glob.glob(path2 + "p1*" + str(week) + "*snx"))
            
            if not (cslis and p1lis):
                continue
                
            out = gcls.compar_sinex(cslis[0] , p1lis[0] , stat_select=sta_sel,
                                    invert_select=invert_select)
            valstk.append(out)
        
        A = pd.concat(valstk)
        Adict[sta_sel_nam] = A
        gf.pickle_saver(A,"/home/psakicki/aaa_FOURBI/","snx_diff_" + sta_sel_nam)
        
    gf.pickle_saver(Adict,"/home/psakicki/aaa_FOURBI/","snx_diff_dic")


if bool_plot_ENU3D:
    if not bool_read_n_save:
        A = gf.pickle_loader("/home/psakicki/aaa_FOURBI/snx_diff_NO_AUTO_SEL.pik")
    mpl.rcParams['legend.fontsize'] =  18
    mpl.rcParams['axes.titlesize']  =  26
    fig , ax = plt.subplots() 
    
    tup_enud=("e","n","u","d3D_enu")
    tup_enud_labl = ("East compo.","North compo.","Up compo.","3D Dist.")
    for enud , enud_labl in zip(tup_enud , tup_enud_labl) :
        Y = A[enud + "_rms"]*10**3
        YY = pd.rolling_mean(Y,10)
        ax.plot(A["week"],YY,label=enud_labl)
    
    
    ax.set_ylim(0,8)
    
    ax.legend(ncol=4)
    ax.set_xlabel("Time [GPS Weeks]")
    ax.set_ylabel("RMS differences [mm]")
    ax.set_title("Mean coordinates difference (PF1 w.r.t. CF-SNX Combined Solution)")
    
    koef = 1.9
    Len = (19.9/2.54) * koef * .9
    Hei = (9.6/2.54)  * koef * .8
    fig.set_size_inches((Len,Hei))
    fig.patch.set_alpha(0)
    plt.tight_layout()
    
    outplt = os.path.join(outdir, "Coords_Stability")
    for ext in (".svg" , ".png" , ".pdf"):
        plt.savefig(outplt + ext,bbox_inches='tight')    

if bool_plot_multi_enu2D3D:
    
    import matplotlib.lines as mlines
    
    if not bool_read_n_save:
        Adic = gf.pickle_loader("/home/psakicki/aaa_FOURBI/snx_diff_dic.pik")
        
    selec_group_list = ["MGEX","IGS","GSS","GESS"]
    selec_group_list = ["MGEX","IGS","ALL"]
    
    
    ##### for color and symb 
    coldic = dict()
    symdic = dict()
    labdic = dict()

    typtup     = ["IGS","MGEX","GESS","GSS","ALL"]
    coltup     = ["blue" , "green"  , "#984ea3" , "orange" , "xkcd:dark yellow"] 
    symtup     = ["^" , "v" , "<" , ">" , "*"] 
    labtup     = ["IGS GPS Only" , "IGS MGEX" , "GESS","GSS" , "All stations" ]
    
    for typ , col ,sym , lab in zip(typtup,coltup,symtup,labtup):
        coldic[typ] = col 
        symdic[typ] = sym 
        labdic[typ] = lab 

    ##### For col and symb
    
    
    
    
    mpl.rcParams['legend.fontsize'] =  17
    mpl.rcParams['axes.titlesize']  =  26
    fig , ax = plt.subplots() 
    
    tup_enud=("d2D_enu","d3D_enu")
    tup_enud_labl = ("3D Dist.","3D Dist.")
    handle_stk = []
    for sel_grp in selec_group_list:
        A = Adic[sel_grp]
        for enud , enud_labl in zip(tup_enud , tup_enud_labl) :
            
            if enud == "d2D_enu":
                linstyl        = "--"
                bool_stk_handl = False
            else:
                linstyl        = "-"
                bool_stk_handl = True
                
            Y = A[enud + "_rms"]*10**3
            YY = pd.rolling_mean(Y,10)
            hdl = ax.plot(A["week"],YY,label=labdic[sel_grp],color=coldic[sel_grp],
                    linestyle=linstyl)
            
            if bool_stk_handl:
                handle_stk.append(hdl[0])
        
        ax.set_ylim(0,8)
        
        #ax.legend(ncol=6)
        
        line2D = mlines.Line2D([], [], color='black', marker='',
                markersize=15, label='2D Plani. Dist.',linestyle="--")

        line3D = mlines.Line2D([], [], color='black', marker='',
                markersize=15, label='3D Dist.',linestyle="-")
        
        ax.legend(handles=handle_stk + [line2D , line3D], ncol=6)
        
        ax.set_xlabel("Time [GPS Weeks]")
        ax.set_ylabel("RMS differences [mm]")
        ax.set_title("Mean coordinates difference (PF1 w.r.t. CF-SNX Combined Solution)")
        
        koef = 1.9
        Len = (19.9/2.54) * koef * .9
        Hei = (9.6/2.54)  * koef * .8
        fig.set_size_inches((Len,Hei))
        fig.patch.set_alpha(0)
        plt.tight_layout()
        
    outplt = os.path.join(outdir, "Coords_Stability")
    for ext in (".svg" , ".png" , ".pdf"):
        plt.savefig(outplt + ext,bbox_inches='tight')    
