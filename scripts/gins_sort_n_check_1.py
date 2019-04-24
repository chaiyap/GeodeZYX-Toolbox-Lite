#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:21:05 2018

@author: psakicki
"""

from megalib import *
import glob
import os
import shutil
import softs_runner
import gins_runner

path_orig       = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/"
path_raw        = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK"
path_sorted     = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/SORTED"
path_duplicated = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/DUPLICATED"

#path_listing_raw    = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK"
#path_listing_sorted = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/SORTED"
#path_duplicated     = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/batch/solution/OK/DUPLICATED"


wildcard_raw = "*GWA2A_OPE_1a*"
wildcard_raw = "*GWA2A_OPE_2a*"

rinex_archive = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/"
rinex_archive = "/wrk/sakic_xchg/GWA2A2018/RINEX/"
rinex_archive = "/wrk/sakic_xchg/GWA2A2018/RINEX/RINEX/GOOD"
specific_stats = []
start,end = softs_runner.start_end_date_easy(1980,150,2050,200)


del_duplicated = True

def extract_stat_date(fil):
    fil_base = os.path.basename(fil)
    fil_base_splited = fil_base.split(".yml")[0].split("_")
    jjul = int(fil_base_splited[-2])
    STAT = fil_base_splited[-3]
    dt = geok.jjulCNES2dt(jjul)
    doy , yyyy = geok.dt2doy_year(dt)
    return STAT,jjul,dt,yyyy,doy


############ MOVE SOL FILE INTO DEDICATED FOLDER
if 1:
    print("INFO : move solutions in the OK folder")
    print("WARN : This operation is risky, you have 4sec to cancel")
    komand ="mv -v " + path_orig + "/" + wildcard_raw + " " + path_raw
    print(komand)
    time.sleep(4)
    gf.create_dir(path_raw)
    os.system(komand)
    
########### MOVE SOL FILE INTO DEDICATED FOLDER
Files_raw = sorted(glob.glob(os.path.join(path_raw,wildcard_raw)))
if 1:
    for fil in Files_raw:
        STAT,jjul,dt,yyyy,doy = extract_stat_date(fil)
        print("INFO : move ",  STAT,jjul)
        path_out = os.path.join(path_sorted,STAT)
        gf.create_dir(path_out)
        print("INP :", fil )
        print("OUT :", path_out )
        shutil.move(fil,path_out)


############ GIVE PRETTY NAMES to SOL FILES
### STAT_JJUL_YYYY_DOY_<the_rest_of_the_file>
if 1:  
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    for fil in Files_sorted:
        print(fil)
        STAT,jjul,dt,yyyy,doy = extract_stat_date(fil)
        fil_base = os.path.basename(fil)
        #print(STAT,jjul,dt,yyyy,doy)
        regex_pretty = "^\w{4}_\d{5}_\d{4}_\d{3}"
        if not re.search(regex_pretty,fil_base):
            stat_jjul_yyyy_doy = gf.join_improved("_",STAT,jjul,yyyy,doy)
            fil_new = os.path.join(os.path.dirname(fil),stat_jjul_yyyy_doy + '_' + os.path.basename(fil))
            print("OLD :", fil)
            print("NEW :", fil_new)
            os.rename(fil,fil_new)
            

############ CHECK CONSISTENCY

if 1:
    print("############ CHECK CONSISTENCY")
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    for fil in Files_sorted:
        bool_consistent = True
        STAT_filename,jjul,dt,yyyy,doy = extract_stat_date(fil)
        Pt_obj = gcls.read_gins_solution(fil,"static")
        if not Pt_obj:
            print("WARN : solution file is empty")
            bool_consistent = False
        elif Pt_obj.name != STAT_filename:
            print("WARN : STAT in solution file != filename")
            print(Pt_obj.name , STAT_filename)
            bool_consistent = False
        else:
            bool_consistent = True
        
        if not bool_consistent:
            print("      removing : ",fil)
            os.remove(fil)

############ CHECK for DOUBLES
if 1:
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    
    L_sol = [(os.path.basename(f).split("_")[0],
          int(os.path.basename(f).split("_")[1])) for f in Files_sorted]
    
    L_sol = pd.DataFrame(L_sol).sort_values([0,1])

    Bool = L_sol.duplicated([0,1],False)
    
    L_dup_simple = L_sol[Bool]
    
    L_dup_tmp1 = sorted(list(set([gf.join_improved("",*row) for row in L_dup_simple.values])))    
    L_dup_uniq  = pd.DataFrame([(e[0:4],int(e[4:])) for e in L_dup_tmp1])
    
    L_dup_opera = L_dup_simple
    L_dup_opera = L_dup_uniq

    print(len(L_sol),np.sum(Bool))
    
    print("DUPLICATED :")
    for l in L_dup_opera.values:
        print(l)
    ################## MOVE DUPLICATED
    if 1:
        gf.create_dir(path_duplicated)
        timstp_gins = lambda f: geok.datestr_gins_filename_2_dt("".join(f.split(".")[-3]))
        for i_l , l in enumerate(L_dup_opera.values):
            print("INFO : duplicated file",i_l,*l)
            ### Really dirty : we reload all the files at each iter in Files_sorted since L_dup is not uniquified
            ### Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
            dupl_regex    = gf.join_improved("_",*l)
            Dupl_files    = [e for e in Files_sorted if re.match(dupl_regex,os.path.basename(e))]
            print("INFO :",len(Dupl_files),"files founds")
            ### We move the most recent files to the DUPLICATE folder
            Dupl_files_time = [timstp_gins(e) for e in Dupl_files]
            ##Dupl_files_mv   = [e for (e,etime) in zip(Dupl_files,Dupl_files_time) if etime != np.min(Dupl_files_time)]
            for fil in Dupl_files:
                print("INFO : min timestamp",np.min(Dupl_files_time))
                print("INFO : cur timestamp",timstp_gins(fil))
                if timstp_gins(fil) != np.min(Dupl_files_time):  
                    del_duplicated = True
                    if not del_duplicated:
                        print("INFO : MOVE to duplicated : ",fil)
                        shutil.move(fil,path_duplicated)
                    else:
                        print("INFO : RM duplicated : ",fil)
                        os.remove(fil)
                        
                    
                    
############ DETERMINE THE RATIO OF THE PROCESSED FILES
if 1:
    Files_sorted = sorted(gf.find_recursive(path_sorted,wildcard_raw))
    
    L_sol = [(os.path.basename(f).split("_")[0],
          int(os.path.basename(f).split("_")[1])) for f in Files_sorted]
    
    L_sol = pd.DataFrame(L_sol)
    
    Rnx_inp = gins_runner.get_rinex_list(rinex_archive,
                                     specific_stats=[],
                                     invert=False,start=start,end=end)
    
    L_rnx = [(os.path.basename(rnx)[:4].upper(),
          geok.dt2jjulCNES(geok.rinexname2dt(os.path.basename(rnx)))) for rnx in Rnx_inp]
    
    L_rnx = pd.DataFrame(L_rnx)
    
    for stat in L_rnx[0].unique():
        L_rnx_stat = L_rnx[L_rnx[0] == stat]
        L_sol_stat = L_sol[L_sol[0] == stat]
        n_rnx_stat = len(L_rnx_stat)
        n_sol_stat = len(L_sol_stat)
        ratio = n_sol_stat / n_rnx_stat
        print(stat,n_sol_stat,n_rnx_stat,ratio)


############ SORT LISTING ACCORDING TO SOL FILES
#if 0:


##### State 181211 1338
# ABD0 1444 1454 0.9931224209078404
# ADE0 2944 2979 0.9882510909701242
# AJB0 1336 1703 0.7844979448032883
# AMC0 598 599 0.998330550918197
# BIM0 1378 1499 0.9192795196797865
# CBE0 1579 1579 1.0
# DHS0 2485 2627 0.9459459459459459
# DSD0 1908 1947 0.9799691833590138
# FFE0 1876 2049 0.915568570034163
# FNA0 1828 1969 0.9283900457084815
# FNG0 540 689 0.783744557329463



# ABD0 1444 2644 0.546142208774584
# ADE0 2929 2979 0.9832158442430345
# AJB0 1611 1703 0.9459776864357017
# AMC0 578 1701 0.33980011757789536
# BIM0 1344 1499 0.8965977318212142
# CBE0 1549 2769 0.559407728421813
# DHS0 2428 3825 0.6347712418300654
# DSD0 1855 2967 0.6252106504887092
# FFE0 1823 2111 0.8635717669351018
# FNA0 1798 1969 0.9131538852209243
# FNG0 666 1903 0.34997372569626906
# FSDC 2916 3314 0.8799034399517199
# HOUE 4029 6274 0.6421740516416959
# ILAM 1158 1396 0.829512893982808
# LAM0 2130 2430 0.8765432098765432
# MAD0 37 1254 0.029505582137161084
# MGL0 1208 1366 0.8843338213762811
# MLM0 1647 1858 0.8864370290635092
# MPOM 1069 1225 0.8726530612244898
# PAR1 0 771 0.0
# PDB0 0 112 0.0
# PSA1 1607 2984 0.5385388739946381
# SAM0 1024 1105 0.9266968325791856
# SBL0 56 531 0.10546139359698682
# SOUF 3791 5851 0.6479234318919843
# STG0 0 186 0.0
# TAR1 196 1286 0.15241057542768274
# TDB0 1421 2722 0.5220426157237326
# ASF0 0 37 0.0
# DDU0 0 40 0.0
# DHS1 0 107 0.0
# GDB0 0 11 0.0
# MPCH 0 26 0.0
# SEG0 0 22 0.0
# ABER 1491 1533 0.9726027397260274
# BOUL 1484 1525 0.9731147540983607
# DESI 1397 1409 0.9914833215046132
# GOSI 1492 1517 0.983520105471325
# LORI 1496 1536 0.9739583333333334
# MAGA 919 933 0.984994640943194
# MARI 1487 1538 0.9668400520156046
# TRIL 1461 1518 0.9624505928853755
# ABMF 2232 3258 0.6850828729281768
# FFT2 154 668 0.23053892215568864
# LMMF 2372 3668 0.6466739367502726
# PPTG 27 756 0.03571428571428571




# ABD0 1977 2644 0.7477307110438729
# ADE0 2944 2979 0.9882510909701242
# AJB0 1661 1703 0.9753376394597769
# AMC0 1150 1701 0.6760728982951205
# BIM0 1500 1499 1.0006671114076051
# CBE0 2102 2769 0.7591188154568437
# DHS0 3149 3825 0.8232679738562092
# DSD0 2411 2967 0.8126053252443546
# FFE0 2014 2111 0.9540502131691142
# FNA0 1925 1969 0.9776536312849162
# FNG0 1296 1903 0.6810299527062533
# FSDC 3280 3314 0.9897404948702474
# HOUE 5131 6274 0.8178195728402933
# ILAM 1397 1396 1.0007163323782235
# LAM0 2393 2430 0.9847736625514403
# MAD0 649 1254 0.5175438596491229
# MGL0 1298 1366 0.9502196193265008
# MLM0 1854 1858 0.9978471474703983
# MPOM 1226 1225 1.0008163265306123
# PAR1 771 771 1.0
# PDB0 111 112 0.9910714285714286
# PSA1 2296 2984 0.7694369973190348
# SAM0 1104 1105 0.9990950226244344
# SBL0 283 531 0.5329566854990584
# SOUF 4983 5851 0.8516492907195351
# STG0 93 186 0.5
# TAR1 700 1286 0.5443234836702955
# TDB0 2070 2722 0.7604702424687729
# ABER 1534 1534 1.0
# BOUL 1524 1526 0.9986893840104849
# DESI 1408 1410 0.9985815602836879
# GOSI 1515 1519 0.9973666886109283
# LORI 1535 1537 0.9986987638256344
# MAGA 932 934 0.9978586723768736
# MARI 1536 1539 0.9980506822612085
# TRIL 1514 1519 0.9967083607636603
# ABMF 3261 3258 1.0009208103130756
# FFT2 668 668 1.0
# LMMF 3662 3668 0.9983642311886587
# PPTG 756 757 0.9986789960369881
# ASF0 0 37 0.0
# DDU0 0 40 0.0
# DHS1 0 107 0.0
# GDB0 0 11 0.0
# MPCH 0 26 0.0
# SEG0 0 22 0.0


### ./THESE/CODES/stationinfo2gins/station.info.ovsg



