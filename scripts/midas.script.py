#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:21:58 2018

@author: psakicki
"""

from megalib import *
import pandas as pd
import softs_runner

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)

path_midas_soft="/home/psakicki/SOFTWARE/MIDAS/midas.e"

#### EXEMPLES
tenu_file_path="/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/RAMO.tenu"
tenu_file_path="/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/MASI.tenu"
tenu_file_path="/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/YRCM.tenu"
tenu_file_path="/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/JOR2.tenu"

raw_dir="/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/RAW_NEU/"
work_dir="/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/MIDAS_WORK/"

raw_dir  = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/01_Syncro_Server_TPX1/GNSS_RESULTS/GINS/01_GFZorbs/03b_export_coords_MIDAS"
work_dir = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/01_Syncro_Server_TPX1/GNSS_RESULTS/GINS/01_GFZorbs/04b_MIDAS_WORK"

L = glob.glob(raw_dir + "/*tenu")

#plt.ioff()

if 1:
    for tenu_file_path_iter in L:
        step_file_path_iter = tenu_file_path_iter.replace("tenu","step")
        softs_runner.midas_run(tenu_file_path=tenu_file_path_iter,
                               work_dir=work_dir,
                               path_midas_soft=path_midas_soft,
                               step_file_path=step_file_path_iter,
                               with_plot=True,
                               keep_plot_open=False)  

if 0:
    vel_generic_path = work_dir + "/*vel_*"
    DFvel = softs_runner.midas_vel_files_2_pandas_DF(vel_generic_path)
    genefun.pickle_saver(DFvel , work_dir,  "midas_velo_DataFrame")

if 0:
    path_out_excel =  os.path.join(work_dir,"midas_velo_sheet.xls")
    DFvel.to_excel(path_out_excel)
        


        
