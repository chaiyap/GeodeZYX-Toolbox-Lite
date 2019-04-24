# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 15:05:32 2015

@author: psakicki


NOTA : New version of spyder (>=  3.2.8) doesn't manage the $PATH environnement
variable anymore if spyder is launched "graphically" by clicking on the Desktop
interface button 
=> spyder must be launched in a terminal

"""

import matplotlib
matplotlib.use('Agg')
import genefun as gf
if gf.spyder_run_check():
    plt.ioff()
import softs_runner
from os.path import join

    
# CHEMINS A PRECISER

general_workdir = '/home/psakicki/THESE/GWADA/WORKING_MK2/'
general_workdir = '/home/psakicki/WORKING_MK2/'
general_workdir = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1805_RENAG_TimeSeries_Synthetic/HECTOR_WORK/v2"
general_workdir = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/HECTOR_WORK"
general_workdir = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/GNSS_RESULTS/GINS/01_GFZorbs/04a_HECTOR_WORK"
general_workdir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/01_Syncro_Server_TPX1/GNSS_RESULTS/EPOS/OK_mk2_good/04a_HECTOR_WORK"
general_workdir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/01_Syncro_Server_TPX1/GNSS_RESULTS/GINS/01_GFZorbs/04a_HECTOR_WORK"

esttrend_generik = join(general_workdir,'generik_config/estimatetrend_onlyyearly_generik.ctl')
esttrend_generik = join(general_workdir,'generik_config/estimatetrend_halfyear_generik.ctl')


remout_generik   = join(general_workdir ,'generik_config/removeoutliers_generik.ctl')

path_suffix = "_with_manu_discont"
path_suffix = "_MERGED"
path_suffix = ""

raw_neu_path         = join(general_workdir , 'RAW_NEU'                      + path_suffix)
outlier_removed_path = join(general_workdir , 'outliers_removed'             + path_suffix)
trend_output_path    = join(general_workdir , 'trend_output_onlyyearly'      + path_suffix)
trend_output_path    = join(general_workdir , 'trend_output_halfyear'        + path_suffix)

#
velo_output_path     = join(general_workdir , 'vel_output')
velo_output_name = 'trend_output_onlyyearly'
velo_output_name = 'trend_output_halfyear'

specific_stats = ('SOUF','MARI') 
specific_stats = ('SOUF','MARI') 
specific_stats = ('MAGA','PDB0','ASF0')
specific_stats = ('ABD0',)

specific_stats = ("SC02","MR01","MR03","RU02")
specific_stats = ("RU07","SC06","SC07","SU06","SU07")
specific_stats = ("YRCM","KI01","DES3")

specific_stats = ("GHAJ","DES1")


specific_stats = ("JOR2","DES1","JOR1")
specific_stats = ("JOR3",)


specific_stats = tuple()

#specific_stats = ("YRCM",)
#specific_stats = ("BALJ",)

invert_specific = False 

# invert specific :
# False = keeping the specific stats 
# True  = removing the specific stats
# or for all stations, leave a empty 
# tuple in specific_stats
# 
# If only one elt in specific_stats
# use a syntax as : ('ABD0',) with a , 
# at the end

# LANCEMENT DE LA PARTIE OUTLIER REMOVING
if 1:
    softs_runner.multi_neufile_outlier_removing(raw_neu_path,
                                                remout_generik,
                                                outlier_removed_path,
                                                extention='neu',
                                                specific_stats=specific_stats,
                                                invert_specific=invert_specific)
# LANCEMENT DE LA PARTIE ESTIMATION TREND
if 1:
    softs_runner.multi_momfile_trend_processing(outlier_removed_path,
                                                esttrend_generik,
                                                trend_output_path,
                                                specific_stats=specific_stats,
                                                invert_specific=invert_specific)
# LANCEMENT DE LA PARTIE EXTRACTION DES VITESSES

if 1:
    for style in ("globk","epc","csv_renag","dataframe"):
        softs_runner.multi_sumfiles_trend_extract(trend_output_path,
                                                  velo_output_path,
                                                  velo_output_name,
                                                  raw_neu_path,
                                                  specific_stats=specific_stats,
                                                  invert_specific=invert_specific,
                                                  style=style)

