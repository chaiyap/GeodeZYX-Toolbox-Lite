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
import os
import glob

# PART 1
# How many RINEXs will you process ?
# You can give compressed RINEXs if you want
# 1a : It's a RINEX alone => give the path of the RINEX
if 1:
    rnx_inp = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_1h/gspl172j.15d.Z'

    rnx_inp = "/media/psakicki/TOSHIBA EXT/NEWCAL/RINEX_NETWORK/walp340g.94o"
    rnx_inp = "/media/psakicki/TOSHIBA EXT/NEWCAL/RINEX_NETWORK/walp113a.97o"
    rnx_inp = "/media/psakicki/TOSHIBA EXT/NEWCAL/RINEX_NETWORK/walp340g.94o"
    rnx_inp = "/media/psakicki/TOSHIBA EXT/NEWCAL/RINEX_NETWORK/walp096a.00o"
    rnx_inp = "/media/psakicki/TOSHIBA EXT/NEWCAL/RINEX_NETWORK/walp1790.95o"
    rnx_inp = "/media/psakicki/TOSHIBA EXT/NEWCAL/RINEX_NETWORK/walp341g.94o"

    rnx_inp = "/home/psakicki/THESE/DATA/1512_RINEX_SIO/DECIMED_but_not_SPLITED/sfg12252.14d.Z"
    rnx_inp = "/home/psakicki/THESE/DATA/1512_RINEX_SIO/SPLIT_4h/sfg1225t.14d.Z"

    rnx_inp = '/home/psakicki/Téléchargements/tlse/tlse301q.15d.Z'

    rnx_inp = '/home/psakicki/Téléchargements/tlse/tlse300z.15o'

    rnx_inp = '/home/psakicki/gin/batch/listing/test_inclusif_exclusif/exclusif/tlse301q.15d.Z'

    rnx_inp = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_1h/gspl171a.15d.Z"
    rnx_inp = "/home/psakicki/THESE/DATA/1512_RINEX_SIO/SPLIT/sfg1225q.14d.Z"

    rnx_inp = "/home/psakicki/Téléchargements/tlse/tlse301m.15d.Z"
    rnx_inp = '/home/psakicki/Téléchargements/tlse/tlse281z.15o'

    rnx_inp = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs/249/ensg249a.15d.Z"
    rnx_inp = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs_Daily1Hz_splited_4_APPS/ensg250a.15d.Z"

    rnx_inp = '/home/psakicki/Téléchargements/tlse/tlse300a.15d.Z'

    rnx_inp = "/home/psakicki/aaa_FOURBI/160428_SeismeLR/recherche_1/RAW_court/lroc119z.16d.Z"
    rnx_inp = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argg1330.15o'
    rnx_inp = '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/TP/TP_KALMAN/usud070f.11o'

    rnx_inp = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argg133D.15o'

    rnx_inp = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argg1330.15o'

    rnx_inp = '/home/psakicki/Téléchargements/smne/smne118d.15d.Z'

    rnx_inp = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/NAPP3350.16o'


    rnx_inp = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/MICR3350.16o'
    rnx_inp = '/home/psakicki/Téléchargements/transfer_397074_files_6ca51ea5/IGNTEST_1sec/tlse/2017/MERGED/tlse0010.17o'
    rnx_inp = '/home/psakicki/Téléchargements/transfer_397074_files_6ca51ea5/IGNTEST_1sec/zimm/2017/zimm0010.17d.Z'
    rnx_inp = '/home/psakicki/Téléchargements/transfer_397074_files_6ca51ea5/IGNTEST_1sec/smne/2017/MERGED/smne0010.17o'

    rnx_inp = '/home/psakicki/Téléchargements/transfer_397074_files_6ca51ea5/napp3140.14o'

    rnx_inp = '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/30sec/ilel1610.15o'
    rnx_inp = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/IGNTEST/tlse/2017/tlse0410.17d.Z'

    rnx_inp = '/home/psakicki/Téléchargements/telechargement_RGP_75668/recherche_1/smne0640.17o'

    rnx_inp = '/home/psakicki/Téléchargements/telechargement_RGP_75708/tlse0640.17o'

    rnx_inp = '/home/psakicki/Téléchargements/telechargement_RGP_75708/riga0640.17o'

    rnx_inp = '/home/psakicki/Téléchargements/telechargement_RGP_75708/v2/riga0640.17o'

    rnx_inp = "/home/psakicki/THESE/DATA/1703_TESTS_RINEX3/v2/tlse0640.17o"
    rnx_inp = '/home/psakicki/THESE/DATA/1610_MASCARET/base292Z.16o'

    rnx_inp = '/home/psakicki/GINS/gin/TP/TP_RELAX/conz1060.10o'

    rnx_inp = '/media/adminuser/8fdd4c0d-db6e-4b3a-9ef6-eb5e27a4c7c5/CALIPSO/psakicki/Téléchargements/aaa_OLD_1504_1609/tlse/tlse3000.15o'

    rnx_inp = '/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/RINEX/1702_RINEX_GWA2A_REBOOT/IGS/abmf/2015/abmf0530.15d.Z'

# 1b : It's a list of RINEXs   => make a list
if 0:
    rnx_inp = ['/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/30sec/roof1610.15o',
               '/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/30sec/ilel1610.15o']

    rnx_inp = sorted(glob.glob('/home/psakicki/THESE/DATA/1512_RINEX_SIO/SPLIT/*d.Z'))
    rnx_inp = sorted(glob.glob('/home/psakicki/THESE/DATA/1512_RINEX_SIO/SPLIT_n_SHIFT/*d.Z'))


    rnx_inp = ['/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/RINEX/gspl173a.15d.Z',
               '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/RINEX/gspl173b.15d.Z',
               '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/RINEX/gspl173c.15d.Z',
               '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/RINEX/gspl173d.15d.Z']

    rnx_inp = ['/home/psakicki/aaa_FOURBI/telechargement_RGP_71775/recherche_1/brst3200.16o',
               '/home/psakicki/aaa_FOURBI/telechargement_RGP_71775/recherche_1/msmm3200.16o',
               '/home/psakicki/aaa_FOURBI/telechargement_RGP_71775/recherche_1/smne3200.16o']

    rnx_inp = ['/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/MICR3350.16o',
               '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/NAPP3350.16o']
# 1c : RINEXs are in a archive => find them, select specific stations and specific period if you want
if 0:
    rinex_archive = '/home/psakicki/gin/TP/GWADA/RINX2/KARIB/B'
    rinex_archive = '/media/vballu/echange/DATA_GR25_BOREL/RINEX_30s'
    rinex_archive = "/home/psakicki/aaa_FOURBI/TLSE2002/"
    rinex_archive = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_2h'
    rinex_archive = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_1h'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL/mlvl/daily/'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL/mlvl/1Hz/mlvl/'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL/mlvl/daily'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs/250'
    rinex_archive = '/home/psakicki/THESE/DATA/1604_BOUEES/AIX/Fichiers_1sec_journaliers/BUOYS/1Hz'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs_Daily1Hz/'
    rinex_archive = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs/'
    rinex_archive = '/media/HDD_anex/OLD2/GWADA/RINX2/FFE0'
    rinex_archive = '/home/psakicki/Téléchargements/telechargement_RGP_75030/recherche_1'

    rinex_archive = '/home/psakicki/GINS/gin/TP/TP_RELAX'

    specific_stats = ['GRAS']
    specific_stats = []
    invert_selection = False
    # For the period, convert easily a start doy / end doy to a Python datetime object
    start,end = softs_runner.start_end_date_easy(2015,171,2015,172)
    start,end = softs_runner.start_end_date_easy(2015,150,2015,200)
    start,end = softs_runner.start_end_date_easy(2015,249,2015,251)
    start,end = softs_runner.start_end_date_easy(2012,87,2012,87)
    start,end = softs_runner.start_end_date_easy(2015,250,2015,250)
    start,end = softs_runner.start_end_date_easy(2007,0o01,2007,8)
    start,end = softs_runner.start_end_date_easy(1980,150,2050,200)

    rnx_inp = gins_runner.get_rinex_list(rinex_archive,
                                         specific_stats=specific_stats,
                                         invert=invert_selection,start=start,end=end)

# PART 2
# Generate the director(s) associated to the input RINEX(s)
#%%
if 1:
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v5_generik_local_macromod.yml'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v5_generik.yml'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v52_NRO_generik.yml'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/STATIC/STATIC_v1_generik.yml'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v6_generik.yml'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v52_NRO_generik.yml'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/v162_alb3_h30s_ippp'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v7_KALMAN_generik.yml'
    director_generik_path =  '/home/psakicki/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v7b_KALMAN_generik.yml'


    director_generik_path =  '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/STATIC/STATIC_v5_generik.yml'
    director_generik_path =  '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/STATIC/STATIC_v4_generik.yml'
    director_generik_path =  '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/STATIC/STATIC_v6_generik.yml'

    director_generik_path =  '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v52_NRO_generik.yml'
    director_generik_path =  '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v7b_KALMAN_generik.yml'
    director_generik_path =  '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v8_KALMAN_generik.yml'


    director_generik_path =  '/home/psakicki/GINS/gin/TP/TP_RELAX/DIR_MC0.yml'
    director_generik_path =  '/home/psakicki/GINS/gin/TP/TP_RELAX/DIR_MC0_perso.yml'

    director_generik_path = '/media/adminuser/8fdd4c0d-db6e-4b3a-9ef6-eb5e27a4c7c5/CALIPSO/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/data/directeur/operationnel/NEW/KINEMATIC/KINE_v8_KALMAN_generik.yml'

    director_generik_path = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GINS_data/directeurs/STATIC_v6_generik.yml"

    director_generik_path = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GINS_SOFTWARE/gin/data/directeur/arc_test_IPPP_complet"

    director_name_prefix  =  'TESTOI3_MK8'
    director_name_prefix  =  'TESTOI3_STATIC'
    director_name_prefix  =  'GSEA_ONSHOR'
    director_name_prefix  =  'TESTCALCC444'
    director_name_prefix  =  'GSEA_5'
    director_name_prefix  =  'TOIT_DPTS'
    director_name_prefix  =  'NCALDEL'

    director_name_prefix  = "SIO1_KINEv5_OPERA"
    director_name_prefix  = "SIO1_KINEv52_NRO_OPERA"
    director_name_prefix  = "SIO1_KINEv6_152"

    director_name_prefix  = "FASTEST_SIO_withKF"
    director_name_prefix  = "FASTEST_SIO_withoutKF"

    director_name_prefix  = "TLSESHIFT_shift0"
    director_name_prefix  = "SIO7b_shift1"

    director_name_prefix  = "FASTEST_withKF"
    director_name_prefix  = "FASTEST_withoutKF"

    director_name_prefix  = "BIGSES_withKF"

    director_name_prefix  = "TOITDPTS1603_withKF_daily_1_v22"
    director_name_prefix  = "TOITDPTS1603_withKF_hourly_v22"
    director_name_prefix  = "TOITDPTS1603_withoutKF_hourly_v22"

    director_name_prefix  = "BUOYS1603_KF1_hourly_v22"

    director_name_prefix  = "TOITDPTS1603_KF1_hourly_4_GINSOPERA_v22"
    director_name_prefix  = "SEISME_LR"

    director_name_prefix  = "GEODESEA_NICA_REBOOT"

    director_name_prefix  = "ADELADEL"
    director_name_prefix  = "GLACIER_AW_2"

    director_name_prefix  = "NAPPE_EP"

    director_name_prefix  = "TEST_NAP_BANDAID"

    director_name_prefix  = "TEST_GLOGAL"

    director_name_prefix  = "TEST_AW_KINE"

    director_name_prefix  = "TEST_GWA2A_PRELIM"


    # si temp_data_folder non renseigné => rinex copié dans /gin/TEMP_DATA
    temp_data_folder   = '/home/psakicki/gin/TP/GWADA/RINEX'
    temp_data_folder   = '' # Best Option

    # si out_director_folder non renseigné => directeur copié dans /gin/data/directeur
    # Use a specific directory only if not running directly GINS
    out_director_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/CHAL'
    out_director_folder = '' # Best Option

    auto_staocl    = True # se rapporte à la creation auto d'un station et oceload pour le rinex traité

    # if auto_staocl == False, specifing the station and oceload files created manually before
    station_file   = '/home/psakicki/gin/data/stations/KARIB_mk3.stat'
    oceanload_file = '/home/psakicki/gin/data/charge/ocean/KARIB_mk3.oclo'
    station_file   = '/home/psakicki/gin/TEMP_DATA/gspl_2015_171_OPERA.stat'
    oceanload_file = '/home/psakicki/gin/TEMP_DATA/gspl_2015_171_OPERA.oclo'
    oceanload_file = ''
    station_file   = ''

    # Use a specific calc center (False in most of case, default is GRG/GR2 orbits)
    perso_orbclk = False
    calc_center  = 'igu'
    repro        =  0

    out_coords = 'nochange' # The defaut output as in the generic director
    out_coords = 'FLH'
    out_coords = 'XYZ'

    # manual Prairie before PREPARS (be carreful)
    with_prairie   = False
    prairie_kwargs = {'with_historik':True,'with_wsb':False}


    # find the interval in RINEX and apply it to the director and the processing step,
    # True is the best option
    # If another interval is required, change the generic director
    auto_interval = True

    directors_list = gins_runner.gen_dirs_from_rnxs(rnx_inp                , \
                director_generik_path,director_name_prefix,temp_data_folder,
                auto_staocl=auto_staocl,oceanload_file=oceanload_file      ,
                stations_file=station_file,perso_orbclk=perso_orbclk       ,
                calc_center=calc_center,repro=repro,out_coords=out_coords  ,
                auto_interval=auto_interval,prairie=with_prairie           ,
                prairie_kwargs=prairie_kwargs)
#%%
# PART 2.5
# directors are already generated
# just find it according to the directors prefix
if 0:
#    director_name_prefix  = "TOITDPTS1603_withoutKF_hourly_1"
#    director_name_prefix  = "TOITDPTS1603_withoutKF_hourly_1"
    director_name_prefix  = "TOITDPTS1603_withKF_hourly_v22"

    wildcard_path = os.path.join(gins_runner.get_gins_path(1),'data',
                    'directeur',director_name_prefix + '*')
    directors_list = sorted(glob.glob(wildcard_path))

# PART 3
# Run the directors
# 3a : on a single slot (most common)
opts_gins_pc='R'
opts_gins_90='-IPPP'
opts_gins_90=''

#opts_gins_90=' -IPPP -lM 9000 -lF 100000'

#opts_gins_90=' -IPPP -lM 9000 -lF 100000'

version = 'VALIDE_16_1'
version = 'VALIDE_15_2_2'

#Version pour le Kalman
version = 'VALIDE_16_2'

#Version pour 2018
version = 'VALIDE_18_1'

if 1:
    gins_runner.run_directors(directors_list,opts_gins_90=opts_gins_90,
                              opts_gins_pc=opts_gins_pc,version=version)
# 3b : on several slots
if 0:
    gins_runner.run_dirs_multislots(directors_list , ['U','L','R'] ,
                                    version=version)


# PART 4
# find days which failed and rerun them
# generate a list of failed directors
# (according to directors prefix as a wildcard)
# and run them with functions of part 3
if 0:
    directors_list = gins_runner.smart_directors_to_run(director_name_prefix + '*')

# PART 5
# Smart archiving
# Once the experiment is finished, archive them in a specific folder
# director        => go to the director_archive
# prepars listing => go to the prepars_archive
# gins listing without duplicate  => go to the gins_main_archive
# gins listing with duplcates     => one goes to gins_main_archive
#                                    the others in gins_anex_archive
if 0:
    archive_path = '/home/psakicki/aaa_FOURBI/archivebidon/'
    director_name_prefix='TESTOI3_MK3**'
    gins_main_archive= os.path.join(archive_path ,'GINS_MAIN')
    gins_anex_archive= os.path.join(archive_path ,'GINS_ANEX')
    prepars_archive  = os.path.join(archive_path ,'PREPARS')
    director_archive = os.path.join(archive_path , 'DIR')

    gins_runner.smart_listing_archive(director_name_prefix,gins_main_archive,
                                      gins_anex_archive,prepars_archive,
                                      director_archive)

#    gins_runner.sort_by_stations(gins_main_archive,wildcard_dir,18)

# PART 6
# In annex, create manually an ocean loading file
if 0:
    station_file = '/home/vballu/gins_v2B/gin/data/stations/station_VB.stat'
    oceanload_out_file = '/home/vballu/gins_v2B/gin/data/charge/ocean/loading_VB'
    gins_runner.write_oceanload_file(station_file,oceanload_out_file)

# ========================================================================================================
# ========================================================================================================
# ========================================================================================================

# BACKUP POUBELLE de tous les anciens paramètres
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

rnx_lis = ['/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/ezev/ezev1700.15d.Z',
             '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/nica1700.15d.Z']
