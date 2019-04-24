# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:32:10 2015

@author: pierre
"""

import softs_runner
import glob
import itertools
import os
import collections

# Bloc exp
rnx_rover    = "/home/pierre/aaa_FOURBI/roof1610.15o"
rnx_base     = "/home/pierre/aaa_FOURBI/ilel1610.15o"
working_dir  = '/home/pierre/aaa_FOURBI/rtklib'
generik_conf = "/home/pierre/aaa_FOURBI/kine_diff_1.conf"
# Bloc exp
rnx_rover    = "/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/roof1610.15o"
rnx_base     = "/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/ilel1610.15o"
working_dir  = '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_TESTOIT3/'
generik_conf = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"

ILELrefpos = [ 0.442604443913433E+07 , -0.894254996071955E+05 , 0.457629676666969E+07 ]


# GEODESEA / EZEV as BASE
EZEVref      = [0.457347065428447E+07 , 0.601888613006856E+06 , 0.439008194625940E+07]
rnx_rover    = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/gspl1700.15o"
rnx_base     = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/ezev/ezev1700.15o"
working_dir  = '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/GEODESEA/'
generik_conf = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
exp_prefix   = "GSEA_ezev_gspl"

#softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
#                                   generik_conf,
#                                   working_dir, 
#                                   experience_prefix=exp_prefix,
#                                   XYZbase=EZEVref,outtype='deg')



# TOIT DPTS
ENSGrefpos = [4201575.85487 ,     189861.53838  ,   4779065.51962 ]
rnx_rover_dir = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL/mlvl"
rnx_base_dir  = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs_Daily1Hz"
working_dir   = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING'
generik_conf  = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
exp_prefix    = "TOITDPTS_ensg_mlvl"

rnx_base_lis  = glob.glob(rnx_base_dir  + '/*')
rnx_rover_lis = glob.glob(rnx_rover_dir + '/*')

#for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):
#    if os.path.basename(rnx_base)[4:7] == os.path.basename(rnx_rover)[4:7] :
#        
#        softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
#                                           generik_conf,
#                                           working_dir, 
#                                           experience_prefix=exp_prefix,
#                                           XYZbase=ENSGrefpos,outtype='deg')
                                           
                                           
#NICArefpos_RGF93 = [4581809.283   ,   581031.772    ,   4384492.682   ]
#NICArefpos       = [4581808.8798  ,   581032.2302   ,   4384493.0375  ]
#    
#rnx_rover_dir = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz"
#rnx_base_dir  = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/1sec/nica"
#working_dir  = "/home/psakicki/THESE/DATA/1506_GEODESEA/RTKLIB_process"
#working_dir  = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/SOLUTION_RTKLIB_NICA/ITRF_REF_COORDS"
#generik_conf  = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
#exp_prefix    = "GEODESEA_nica"

#rnx_base_lis  = glob.glob(rnx_base_dir  + '/*')
#rnx_rover_lis = glob.glob(rnx_rover_dir + '/*171*')

#for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):
    #if os.path.basename(rnx_base)[4:7] == os.path.basename(rnx_rover)[4:7]:
        
        #softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
                                           #generik_conf,
                                           #working_dir, 
                                           #experience_prefix=exp_prefix,
                                           #XYZbase=ENSGrefpos,outtype='deg',
                                           #clean_temp_dir=False)


# TOIT DPTS MULTISTATS
if 0:
    refposdic = collections.OrderedDict()
    #refposdic['CHPH'] =  [   4236233.0816  ,  110998.2646  , 4751117.4772  ]   
    #refposdic['MAN2'] =  [   4274275.7991  ,   11584.5215  , 4718386.1491  ]  
    #refposdic['MLVL'] =  [   4201576.8233  ,  189860.2844  , 4779064.9039  ]  
    #refposdic['SIRT'] =  [   4213550.7725  ,  162494.6974  , 4769661.8907  ]  
    #refposdic['SMNE'] =  [   4201791.9088  ,  177945.6658  , 4779287.0237  ]  
    
    refposdic = collections.OrderedDict([('CHPH', (4236233.08156, 110998.26463599999, 4751117.477176)), ('MAN2', (4274275.799144, 11584.521544, 4718386.149148)), ('MLVL', (4201576.823332, 189860.284372, 4779064.903872)), ('SIRT', (4213550.772464001, 162494.69744, 4769661.8907079995)), ('SMNE', (4201791.9088, 177945.66576799998, 4779287.023676001))])
    refposdic['ENSG'] = [4201575.85487 ,     189861.53838  ,   4779065.51962 ]
    
    rnx_rover_dir = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs_Daily1Hz/"
    rnx_base_dir  = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/STATIONSSS_RGP/telechargement_RGP_*/recherche_1"
    
    #rnx_rover_dir = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL/mlvl/daily/"
    #rnx_base_dir  = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs_Daily1Hz"
    
    
    working_dir   = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING'
    generik_conf  = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
    exp_prefix    = "TOITDPTS_multistats"
    
    rnx_base_lis  = glob.glob(rnx_base_dir  + '/*o')
    rnx_rover_lis = glob.glob(rnx_rover_dir + '/*')
    
    
    for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):
        print((rnx_base,rnx_rover))
        if (os.path.basename(rnx_base)[4:7] == os.path.basename(rnx_rover)[4:7]) and os.path.basename(rnx_rover)[4:7] in ('249','251'):
    		
    		
            refpos = refposdic[os.path.basename(rnx_base)[0:4].upper()]
            
            softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
                                               generik_conf,working_dir, 
                                               experience_prefix=exp_prefix,
                                               XYZbase=refpos,outtype='xyz')
                                           
if 0:
    refposdic     = collections.OrderedDict([('ANGL', (4404491.463891803, -108110.74519999999, 4596491.369008197)), 
                                             ('AUNI', (4429451.702603825, -73344.22005901638, 4573322.050031694)),
                                             ('BRES', (4370725.68305082, -36125.112323497255, 4629768.617508197)),
                                             ('CHPH', (4236233.126345355, 110998.20365901639, 4751117.440314207)), 
                                             ('ILDX', (4436670.968227869, -91137.98939453551, 4566018.180908743)), 
                                             ('MAN2', (4274275.839450819, 11584.458500000006, 4718386.110908197)), 
                                             ('ROYA', (4466458.820191803, -79862.86325300546, 4537304.7706551915)),
                                             ('SMNE', (4201791.951862842, 177945.60513551912, 4779286.986814207))])
                                         
    rnx_rover_dir_1 = "/home/psakicki/THESE/DATA/1604_BOUEES/AIX/UMRB/MERGED/"
    rnx_rover_dir_2 = "/home/psakicki/THESE/DATA/1604_BOUEES/AIX/SHOB"
    rnx_rover_dir_3 = "/home/psakicki/THESE/DATA/1604_BOUEES/AIX/IPGB"

    rnx_base_dir  = "/home/psakicki/THESE/DATA/1604_BOUEES/AIX/STATIONSSS_RGP/"
    
    working_dir       = '/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/RTKLIB'
    experience_prefix = "RTKLIB_BOUEES_AIX"
    
    
    rnx_base_lis  = glob.glob(rnx_base_dir  + '/*o')
    rnx_rover_lis = []
    for rnx_rover_dir in (rnx_rover_dir_1,):
        rnx_rover_lis = rnx_rover_lis + glob.glob(rnx_rover_dir + '/*o')


    for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):
        print((rnx_base,rnx_rover))
        if (os.path.basename(rnx_base)[4:7] == os.path.basename(rnx_rover)[4:7]):
    		
    		
            refpos = refposdic[os.path.basename(rnx_base)[0:4].upper()]
            
            softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
                                               generik_conf,working_dir, 
                                               experience_prefix=exp_prefix,
                                               XYZbase=refpos,outtype='xyz')
if 0:
    rnx_base     = "/home/psakicki/THESE/DATA/1610_MASCARET/base/lbrd2920.16o"
    rnx_base     = "/home/psakicki/THESE/DATA/1610_MASCARET/base/lbrd2910.16o"

    rnx_rover    = '/home/psakicki/THESE/DATA/1610_MASCARET/TOPCON_RAW_GOOD/base292y.16d.Z'
    rnx_rover    = '/home/psakicki/THESE/DATA/1610_MASCARET/TOPCON_RAW_GOOD/bins292y.16d.Z'
    rnx_rover    = '/home/psakicki/THESE/DATA/1610_MASCARET/TOPCON_RAW_GOOD/base292z.16d.Z'
    rnx_rover    = '/home/psakicki/THESE/DATA/1610_MASCARET/TOPCON_RAW_GOOD/bins291z.16d.Z'

    generik_conf = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
    working_dir  = '/home/psakicki/THESE/DATA/1610_MASCARET/RTKLIB/'
    exp_prefix   = "MASCARET"
    
    softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
                                       generik_conf,working_dir, 
                                       experience_prefix=exp_prefix,
                                       outtype='geo',calc_center='igr')


if 0:
    generik_conf = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
    working_dir  = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/PROCESSED/RTKLIB'
    exp_prefix   = "GEODESEA_NICA_REBOOT"
    
    rnx_base = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/1sec/nica/nica1730.15o'
    rnx_rover = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/RINEX/gspl173A.15d.Z'
    
    softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
                                       generik_conf,working_dir, 
                                       experience_prefix=exp_prefix,
                                       outtype='geo',calc_center='igs')
    
if 0:
    generik_conf = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
    working_dir  = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/PROCESSING/RTKLIB'
    exp_prefix   = "ARGENTIERE"
    
    rnx_base  = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argr1330.15o'
    rnx_rover = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argg1330.15o'
    
    softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
                                       generik_conf,working_dir, 
                                       experience_prefix=exp_prefix,
                                       outtype='geo',calc_center='igs')
      
if 1:
    generik_conf = "/home/psakicki/THESE/SOFTWARES/RTKLIB_Linux/conf_files/kine_diff_1.conf"
    working_dir  = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/PROCESSING/RTKLIB'
    exp_prefix   = "NAPPE_BRST"
    
    rnx_base  = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/brst3350.16o'
    rnx_rover = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/NAPP3350.16o'
    rnx_rover = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/MICR3350.16o'

    
    XYZbase = [4231162.433449181, -332746.4665562841, 4745131.043373224] # BRST @ 2016.9125683060108

    softs_runner.rtklib_run_from_rinex(rnx_rover,rnx_base,
                                       generik_conf,working_dir, 
                                       experience_prefix=exp_prefix,
                                       outtype='geo',calc_center='igs',
                                       XYZbase=XYZbase)