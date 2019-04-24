# -*- coding: utf-8 -*-

import softs_runner
import glob

#modele
#out_dir = '/home/psakicki/THESE/DATA/1410_MARSITE/GPS_DATA/WORKING/CLEANs/24h'
#input_rinex='/home/psakicki/THESE/DATA/1410_MARSITE/GPS_DATA/WORKING/BIGs/ms2i_big_dec1'
#stat_out_name = 'ms2i'
#interval_size = 24

##mes parametres
#out_dir = '/home/vballu/DATA/GNSS/VANUATU/GPS_KINE/2010/ship/6h'
#input_rinex='/home/vballu/DATA/GNSS/VANUATU/GPS_KINE/2010/ship/ship???0.10o'
#stat_out_name = 'ship'
#interval_size = 6
#mes parametres
stat_out_name = ''
interval_size = 1 #h

out_dir = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/' + str(interval_size) + 'h'
out_dir = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_2h'
out_dir = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_1h'
out_dir = '/home/psakicki/THESE/DATA/1512_RINEX_SIO/DECIMED_but_not_SPLITED/'
out_dir = '/home/psakicki/Téléchargements/tlse'
out_dir = '/home/psakicki/THESE/DATA/1512_RINEX_SIO/SPLIT_n_SHIFT'
out_dir = '/home/psakicki/Téléchargements/tlse/'
out_dir = '/home/psakicki/THESE/DATA/1604_BOUEES/AIX/Fichiers_1sec_journaliers/BUOYS/1Hz'
out_dir = '/home/chup01/software/GINS/gin/TEMP_DATA/split_CNGH_12h'
out_dir = '/home/chup01/software/GINS/gin/TEMP_DATA/split_LROC_12h'
out_dir = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/RINEX_1h"

input_rinex='/home/vballu/DATA/GNSS/NC/NC_2014/RAW/ouva*o'
input_rinex='/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/ilel1610.15o'
input_rinex='/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/roof1610.15o'
input_rinex='/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/gspl*.Z'
input_rinex='/home/psakicki/THESE/DATA/1512_RINEX_SIO/DECIMED_but_not_SPLITED/sfg12252.14o'
input_rinex='/home/psakicki/THESE/DATA/1512_RINEX_SIO/DECIMED_but_not_SPLITED/sfg12252.14d.Z'
input_rinex='/home/psakicki/Téléchargements/tlse/tlse3010.15d.Z'
input_rinex='/home/psakicki/Téléchargements/tlse/tlse3010.15d.Z'
input_rinex='/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs_Daily1Hz/ensg2500.15d.Z'
input_rinex='/home/psakicki/THESE/DATA/1604_BOUEES/AIX/Fichiers_1sec_journaliers/BUOYS/*'
input_rinex='/home/chup01/software/GINS/gin/TEMP_DATA/cngh0170.16o'
input_rinex='/home/chup01/software/GINS/gin/TEMP_DATA/lroc0150.19o'








input_rinex = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/km_10580.10d.Z"
stat_out_name = 'km_1'
input_rinex = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/km_20580.10d.Z"
stat_out_name = 'km_2'

# ============= FIN DE PARAMETRES =============
inp_rnx_lis = glob.glob(input_rinex)

if inp_rnx_lis == []:
    print('inp_rnx_lis empty ...')
    print('check the path or the wildcard')

for rnx in inp_rnx_lis:
	print(rnx)
 
	softs_runner.rinex_spliter(rnx,out_dir,stat_out_name,
                            interval_size,compress=False,shift=0,
                            inclusive=True, teqc_cmd='/home/psakicki/SOFTWARE/GINS/gins_toolbox/bin/Linux/teqc')
                            
                            





