# -*- coding: utf-8 -*-
"""
NOTA : New version of spyder (>=  3.2.8) doesn't manage the $PATH environnement
variable anymore if spyder is launched "graphically" by clicking on the Desktop
interface button 
=> spyder must be launched in a terminal
"""

import gins_runner
import softs_runner
import re

rinex_path = '/home/pierre/Téléchargements/blvr0030.15o'
rinex_path = '/home/psakicki/gin/TP/GWADA/RINX2/KARIB/A/guat/guat0010.02d.Z'
rinex_path = '/home/psakicki/gin/TP/GWADA/RINX2/HOUE/houe0010.02o'
rinex_path = '/media/vballu/echange/DATA_GR25_BOREL/RINEX_30s/moma3650.14o'
#rinex_path = '/media/vballu/echange/DATA_GR25_BOREL/RINEX_1s_6h/mo6h215a.14o' #jour de beau temps
#rinex_path = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/PINS/pins2440.14o'
rinex_path = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/roof161a.15o'
rinex_path = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/1h/roof161a.15o'
rinex_path = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/3h/roof161a.15o'

rinex_path = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/30sec/ilel1610.15o'
rinex_path = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/30sec/roof1610.15o'

rinex_path = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/4h/roof161a.15o'
rinex_path = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/30sec/ilel1610.15o'


rnx_lis =  [ '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/6h/ilel161a.15o',
'/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/4h/ilel161a.15o',
'/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/4h/roof161a.15o',
'/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/3h/ilel161a.15o',
'/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/3h/roof161a.15o']

rnx_lis =  [
'/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/4h/ilel161a.15o',
'/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/4h/roof161a.15o']

rnx_lis = ['/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/30sec/roof1610.15o',
           '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/30sec/ilel1610.15o']

rnx_lis    = ['/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/ezev/ezev1700.15d.Z',
             '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/nica1700.15d.Z']


director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v5_generik.yml' 
director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/STATIC/STATIC_v3_interpvit_generik.yml'
director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/STATIC/STATIC_v1_generik.yml'

director_name_prefix  =  'TESTOI3_MK8'
director_name_prefix  =  'TESTOI3_STATIC'
director_name_prefix  =  'TESTCALCCNTR'
director_name_prefix  =  'GSEA_ONSHOR'


# si temp_data_folder non renseigné => rinex copié dans /gin/TEMP_DATA
temp_data_folder   = '/home/psakicki/gin/TP/GWADA/RINEX'
temp_data_folder   = ''

# si out_director_folder  non renseigné => directeur copié dans /gin/data/directeur
out_director_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/CHAL'
out_director_folder = ''

auto_staocl = True # se rapporte à la creation auto d'un station et oceload pour le rinex traité
station_file = '/home/psakicki/gin/data/stations/KARIB_mk3.stat'
oceanload_file = '/home/psakicki/gin/data/charge/ocean/KARIB_mk3.oclo'
station_file   = ''
oceanload_file = ''

full_files_lis = []
specific_stats = [] #['cn19',]

# utile pour le cas avec plein de rinex
rinex_archive = '/home/psakicki/gin/TP/GWADA/RINX2/KARIB/B'
rinex_archive = '/media/vballu/echange/DATA_GR25_BOREL/RINEX_30s'
rinex_archive = "/home/psakicki/aaa_FOURBI/TLSE2002/"

opts_gins_pc= ''
opts_gins_90=''
#opts_gins_90=' -IPPP'

perso_orbclk=1
calc_center='jpl'
repro=2

out_coords = 'nochange'
out_coords = 'FLH'
out_coords = 'XYZ'

auto_interval = True 

# EXEMPLE A
#produce a director from a rinex, and write it in the specific location
#
#Return :  
#        the path of the produced director as a string 
#
#If the rinex is not in a gins style folder, it will be copied in the
#``temp_data_folder``
#
#If ``temp_data_folder`` is not specified ( == '') rinex will be copied in 
#a ad hoc folder ``../gin/TEMP_DATA``
#
#If ``out_director_folder`` is not specified ( == ''), output director will be 
#created in the ``../gin/data/directeur folder``
#
#automatic mode : (auto_staocl)
#    create automaticaly a station file and a ocean loading file
#    auto mode is prioritary upon the manu mode
#    
#    so, if a path for stat file or ocload file is specified and 
#    auto_staocl is on, it will be the automatic stat/ocload 
#    which will be used
#perso_orbclk : 
#    download and use specifics orbits 
#    according to calc_center & repro args
#    
#    (they are useless if perso_orbclk aren't activated)                               
#

if 0:
# generate dir and launch it
    directorA = gins_runner.gen_dirs_from_rnxs(rinex_path, \
                director_generik_path,director_name_prefix,temp_data_folder, \
                auto_staocl=auto_staocl,oceanload_file=oceanload_file , \
                stations_file=station_file,perso_orbclk=perso_orbclk,
                calc_center=calc_center,repro=repro,out_coords=out_coords,
                auto_interval=auto_interval)
    gins_runner.run_directors(directorA,opts_gins_90=opts_gins_90,opts_gins_pc=opts_gins_pc)

# EXEMPLE B
if 1:
# launching multi rinex experience
    # B1 : find plenty of rinex in a folder and his subfolders
#    s,e = softs_runner.start_end_date_easy(1980,1,2099,1)
    rnx_lis = gins_runner.get_rinex_list(rinex_archive,
                                        specific_stats=['GRAS'],invert=False,start=s,end=e)
    ## B2 : Making the corresponding directors
    dir_lis = gins_runner.gen_dirs_from_rnxs(rnx_lis , \
                director_generik_path,director_name_prefix,temp_data_folder, \
                auto_staocl=auto_staocl,oceanload_file=oceanload_file , \
                stations_file=station_file,perso_orbclk=perso_orbclk,
                calc_center=calc_center,repro=repro,out_coords=out_coords,
                auto_interval=auto_interval)    
    # B3 : launch thoses directors
    # B3a : on a single slot (most common)
#    gins_runner.run_directors(dir_lis,opts_gins_90=opts_gins_90,opts_gins_pc=opts_gins_pc)
    # B3b : on several slots
    gins_runner.run_dirs_multislots(dir_lis,['','U','L','R'])

# EXEMPLE C
if 0:
    # rerun a stopped experience using  smart_directors_to_run function
    # C1
    di_run_lis = gins_runner.smart_directors_to_run(director_name_prefix + '*')
    # C2a : on a single slot (most common)
    gins_runner.run_directors(di_run_lis,opts_gins_90=opts_gins_90)
    # C2b : on several slots
    #gins_runner.run_dirs_multislots(di_run_lis,['','U','L','R'])

# EXEMPLE D
if 0:
#smart archiving
    genepath = '/home/psakicki/aaa_FOURBI/archivebidon/'
    wildcard_dir='TESTOI3_MK3**'
    gins_main_archive= genepath + 'GINS_MAIN'
    gins_anex_archive= genepath + 'GINS_ANEX'
    prepars_archive= genepath + 'PREPARS'
    director_archive= genepath + 'DIR'
    gins_runner.smart_listing_archive(wildcard_dir,gins_main_archive,
                                      gins_anex_archive,prepars_archive,
                                      director_archive)

#    gins_runner.sort_by_stations(gins_main_archive,wildcard_dir,18)
# EXEMPLE E
if 0:
    station_file = '/home/vballu/gins_v2B/gin/data/stations/station_VB.stat'
    oceanload_out_file = '/home/vballu/gins_v2B/gin/data/charge/ocean/loading_VB'
    gins_runner.write_oceanload_file(station_file,oceanload_out_file)