#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 11:05:39 2018

@author: psakicki
"""

from megalib import *
p="/home/psakicki/aaa_FOURBI/TMP_SUM_files_GGSP_4_EGU_Poster/sumfiles_CMB_OVF_TMP/*sum"
p="/home/psakicki/aaa_FOURBI/TMP_SUM_files_GGSP_4_EGU_Poster/SNX_PF1_CS_TMP/TAR/AC_CMB/CMB/SUM/*sum"


exportp = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/DataPython/"

filist = sorted(glob.glob(p))

pXlist = ("p1_","p2_","p3_","cor","igr")

GPSGAL = "_GPS"
GPSGAL = "_GAL"

BigStk = list()

for f in filist:
    
    print(f)
    
    week = gf.split_improved(os.path.basename(f),"_",".")[:-1]
    
    for d in range(7):
        if d != 6:
            mark_strt = "Table 3." + week + "." + str(d)
            mark_end  = "Table 3." + week + "." + str(d+1) 
        else:
            mark_strt = "Table 3." + week + "." + str(d)
            mark_end  = "Table 4:"            
            
        Extracted = gf.extract_text_between_elements(f, mark_strt , mark_end )
        
        if GPSGAL == "_GAL":    
            Greped = gf.egrep_big_string("XE",Extracted)
        elif GPSGAL == "_GPS":    
            Greped = gf.egrep_big_string(" G[0-9][0-9]",Extracted)
            
        if not Greped:
            print("WARN : No Gal Sats for ",week,d)
            continue
        
        GrepedPRN      = gf.egrep_big_string("PRN",Extracted)
        GrepedPRNsplit = GrepedPRN.split()
        
        dic_i_pX = dict()
        
        for pX in pXlist:
            i_pX = None
            try:
                i_pX = GrepedPRNsplit.index(pX)
            except:
                i_pX = None

            dic_i_pX[pX] = i_pX
        
        check_val = lambda x: np.nan if ((">>" in x) or ("--" in x)) else int(x)

        pX_val_dic = dict()
        for pX in pXlist:
            pX_val_dic[pX] = []         

        if type(Greped) is str:
            Greped = [Greped]

        for g in Greped:
            gsplit = g.split()
                            
            for pX in pXlist:
                pX_val_stk = []
                
                if not dic_i_pX[pX]:
                    continue
                else:
                    pX_val_dic[pX].append(check_val(gsplit[dic_i_pX[pX]]))
     
        pX_rms_dic = dict()
        
        nbsat = len(Greped)
        
        for pX , pxVal in pX_val_dic.items():
            pX_rms_dic[pX] = geok.rms_mean(pxVal)
        
            BigStk.append([week, d , pX , pX_rms_dic[pX] , nbsat])

Data = pd.DataFrame(BigStk)

gf.pickle_saver(Data , exportp , "DataOrb" + GPSGAL)

Clocks = True 

if Clocks:
    pclk = "/home/psakicki/aaa_FOURBI/TMP_SUM_files_GGSP_4_EGU_Poster/SNX_PF1_CS_TMP/TAR/AC_CMB/CMB/CLS/*cls"
    
    filist = sorted(glob.glob(pclk))
    
    BigStk = list()
    for f in filist:
        
        print(f)
        
        wwwwd = gf.split_improved(os.path.basename(f),"_",".")
        week = wwwwd[:4]
        d    = int(wwwwd[-1])
        
        mark_strt = "RMS (ps) OF AC CLOCK COMPARED TO COMBINATION"
        mark_end  = "CLOCK JUMP CORRECTIONS APPLIED"            
                
        Extracted = gf.extract_text_between_elements(f, mark_strt , mark_end )
        
        
        if GPSGAL == "_GAL":    
            Greped = gf.egrep_big_string("^  E",Extracted)
        elif GPSGAL == "_GPS":    
            Greped = gf.egrep_big_string("^  G",Extracted)
            
        if not Greped:
            print("WARN : No Gal Sats for ",week,d)
            continue
        
        GrepedPRN      = gf.egrep_big_string("NEPO    RMS",Extracted)
        GrepedPRNsplit = GrepedPRN.split()
        
        dic_i_pX = dict()
        
        for pX in pXlist:
            i_pX = None
            try:
                i_pX = GrepedPRNsplit.index(pX)
            except:
                i_pX = None
    
            dic_i_pX[pX] = i_pX
        
        check_val = lambda x: np.nan if ((">>" in x) or ("--" in x)) else int(x)
    
        pX_val_dic = dict()
        for pX in pXlist:
            pX_val_dic[pX] = []         
    
        if type(Greped) is str:
            Greped = [Greped]
    
        for g in Greped:
            gsplit = g.split()
            gsplit.remove("|")
            gsplit.remove("|")
    
            gsplit = [">>" if ee in ("-","X") else ee for ee in gsplit]
    
            sat    = gsplit[0][2:4] 
                            
            for pX in pXlist:
                pX_val_stk = []
                
                if not dic_i_pX[pX]:
                    continue
                else:
                    pX_val_dic[pX].append(check_val(gsplit[dic_i_pX[pX]]))
        
    
        pX_rms_dic = dict()
        pX_std_dic = dict()
        
        for pX , pxVal in pX_val_dic.items():
            pX_rms_dic[pX] = geok.rms_mean(pxVal)
            pX_std_dic[pX] = np.std(pxVal)
        
            BigStk.append([week, d , pX , pX_rms_dic[pX],pX_std_dic[pX]])
    
    DataCLS = pd.DataFrame(BigStk)

    gf.pickle_saver(DataCLS , exportp , "DataClk" + GPSGAL)

writing_file = 0

if writing_file:
    header="""+sum_orb_clk
*
*  MJD     WEEK D H  CENT STA      DX       DY       DZ       RX       RY       RZ      SCL     RMS     WRMS       TOFT       TDRFT      STDDEV        RMS       MEDI
*--------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

    footer="""*--------------------------------------------------------------------------------------------------------------------------------------------------------------------
*  MJD     WEEK D H  CENT STA      DX       DY       DZ       RX       RY       RZ      SCL     RMS     WRMS       TOFT       TDRFT      STDDEV        RMS       MEDI
*
-sum_orb_clk
"""

    for pXiter in pXlist:
        
        MJDstk = []
        RMSstk = []
        
        
        outpath = "/home/psakicki/aaa_FOURBI/" + "GALILEO_sum_final_" + pXiter + ".plt"
        
        outFile = open(outpath , "w+")
        
        Data_pX     = Data[np.logical_and(Data[2] == pXiter , np.logical_not(np.isnan(Data[3])))] 
        
        if Clocks:
            DataCLS_pX  = DataCLS[(DataCLS[2] == pXiter)]
        
        start = geok.dt2MJD(geok.gpstime2dt(int(Data_pX[0].iloc[0]) ,Data_pX[1].iloc[0]))
        end   = geok.dt2MJD(geok.gpstime2dt(int(Data_pX[0].iloc[-1]),Data_pX[1].iloc[-1]))
        
        outFile.write(gf.join_improved(" ","EPOCH INTERVAL:",start,end,"\n"))
    
        outFile.write(header)
    
        for index , l in Data_pX.iterrows():    
    
            week = l[0]
            d    = l[1]
            pX   = l[2]
            
            
            if Clocks:
                clk_val = DataCLS_pX[(DataCLS_pX[0] == week) & (DataCLS_pX[1] == d)]
            
                if len(clk_val) == 0:
                    clk_rms = 0
                    clk_std = 0
        
                elif len(clk_val) == 1:
                    clk_rms = np.float(clk_val[3])
                    clk_std = np.float(clk_val[4])
                else:
                    print("WARN : CA PLANTE !!!")
                    clk_rms = 0
                    clk_std = 0            
                if np.isnan(clk_rms):
                    clk_rms = 0
                if np.isnan(clk_std):
                    clk_std = 0   
            else:
                    clk_rms = 0
                    clk_std = 0                
                    
    
            if np.isnan(l[3]):
                continue
            
            if pXiter != pX:
                continue
        
            mjd = geok.dt2MJD(geok.gpstime2dt(int(l[0]),l[1])) + .5
            rms = l[3]*10**-3
            
            MJDstk.append(mjd)
            RMSstk.append(rms)
            
            outline = " {:9.3f} {:} {:} {:} {:}  XXX {:+8.4f} {:+8.4f} {:+8.4f} {:+8.4f} {:+8.4f} {:+8.4f} {:+8.4f} {:+7.3f} {:+7.3f}    {:+8.4f}    {:+8.4f}    {:+8.4f}    {:+8.4f} {:+8.4f}\n".format(mjd,week,d,12,pX,-0,0,0,0,0,0,0,rms,rms,0,0,clk_std*10**-2,clk_rms*10**-2,0)       
            outFile.write(outline)
        outFile.write(footer)
        outFile.close()    
    
    
