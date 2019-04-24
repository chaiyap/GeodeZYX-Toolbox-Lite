# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:08:14 2015

@author: psakicki
"""

import softs_runner
import glob , itertools , os
import collections
import geoclass as gcls

# SINGLE MODE
if 0:
    rnx_rover    = "/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ROOF/4h/roof161a.15o"
    rnx_base     = "/home/psakicki/THESE/DATA/1506_TEST_TOIT_3/OPERA_RINEX/ILEL/4h/ilel161a.15o"
    
    working_dir       = '/home/psakicki/THESE/RUNNING_EXP/track/TESTOIT3'
    experience_prefix = "TESTOIT3_air"
    ILELrefpos        = [ 0.442604443913433E+07 , 
                         -0.894254996071955E+05 ,
                          0.457629676666969E+07 ]
    
    mode     = 'air'
    outtype  = 'XYZ'
    XYZbase  = ILELrefpos
    
    softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                              experience_prefix,XYZbase,mode=mode)
                          
#MULTI MODE
if 0:                     
    ENSGrefpos       = [4201575.85487 ,   189861.53838  ,   4779065.51962 ] 
    NICArefpos_RGF93 = [4581809.283   ,   581031.772    ,   4384492.682   ]
    NICArefpos       = [4581808.8798  ,   581032.2302   ,   4384493.0375  ]
    
    
    rnx_rover_dir = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz"
    rnx_rover_dir = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_1h/"

    rnx_base_dir  = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/1sec/nica"
    working_dir   = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/TRACK'
    working_dir   = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/SOLUTION_TRACK_NICA/ITRF_REF_COORDS"
    experience_prefix = "GEODESEA_NICA"
    
    mode     = 'air'
    outtype  = 'FLH'
    XYZbase  = NICArefpos
    
    rnx_base_lis  = glob.glob(rnx_base_dir  + '/*')
    rnx_rover_lis = glob.glob(rnx_rover_dir + '/gspl171a.15d.Z')
    
    for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):
        if os.path.basename(rnx_base)[4:7] == os.path.basename(rnx_rover)[4:7]:
    
            softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                                      experience_prefix,XYZbase,mode=mode)

#MULTI MODE HAWAII
if 1: 
    dictpos  = dict()                 
    dictpos["kokb"]  = [-5543837.3395 ,   -2054587.7350  ,  2387809.8667 ] 
    dictpos["mkea"]  = [-5464104.3916 ,   -2495167.3995  ,  2148291.1574 ] 
    dictpos["km_1"]  = [-5610851.210440 , -1963563.159138 ,  2303910.859183 ] 
    dictpos["km_2"]  = [-5610849.731425 , -1963563.188935 ,  2303914.502848 ] 
    
    rnx_rover_dir = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/RINEX_Orig"
    rnx_base_dir  = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/RINEX_BASE"
    
    working_dir   = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/TRK"
    experience_prefix = "ITEC_HAWA_01"
    
    orbit = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/TRK/TEMP/gat15726.sp3"
    
    mode     = 'long'
    outtype  = 'FLH'
    
    rnx_base_lis  = glob.glob(rnx_base_dir  + '/*Y*')
    rnx_rover_lis = glob.glob(rnx_rover_dir + '/*')
    
    for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):

        XYZbase   = dictpos[os.path.basename(rnx_base)[0:4]]
        XYZrover  = dictpos[os.path.basename(rnx_rover)[0:4]]
        
        softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                                  experience_prefix,XYZbase,XYZrover,mode=mode,
                                  forced_sp3_path=orbit)


if 0:
    rnx_base    = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/RINEX_test/zim20580.10o"
    rnx_rover   = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/RINEX_test/zimm0580.10o"
    
    working_dir       = '/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1902_ITEC_Prelim/Ships/RINEX_test'
    experience_prefix = "TEST"
    
    mode     = 'air'
    outtype  = 'XYZ'
    
    softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                              experience_prefix,XYZbase=[],mode=mode)



if 0:                     
    ENSGrefpos       = [4201575.85487 ,   189861.53838  ,   4779065.51962 ] 
    NICArefpos_RGF93 = [4581809.283   ,   581031.772    ,   4384492.682   ]
    NICArefpos       = [4581808.8798  ,   581032.2302   ,   4384493.0375  ]
    
    refposdic = collections.OrderedDict([('CHPH', (4236233.08156, 110998.26463599999, 4751117.477176)), 
                                         ('MAN2', (4274275.799144, 11584.521544, 4718386.149148)), 
                                         ('MLVL', (4201576.823332, 189860.284372, 4779064.903872)), 
                                         ('SIRT', (4213550.772464001, 162494.69744, 4769661.8907079995)),
                                         ('SMNE', (4201791.9088, 177945.66576799998, 4779287.023676001))])
    refposdic['ENSG'] = [4201575.85487 ,     189861.53838  ,   4779065.51962 ]
    
    rnx_rover_dir = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz"
    rnx_rover_dir = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/PRINCIPAL_GSP1/RINEX_GSPL/1Hz/splited_1h/"

    rnx_base_dir  = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/1sec/nica"
    
    rnx_rover_dir = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/CRINEXs_Daily1Hz/"
    rnx_base_dir  = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/STATIONSSS_RGP/telechargement_RGP_*/recherche_1"
    
#    rnx_rover_dir = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL/mlvl/daily/"
#    rnx_base_dir  = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/STATIONSSS_RGP/telechargement_RGP_*/recherche_1"

    working_dir       = '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/TRACK_longmode'
    experience_prefix = "TRACK_TOITDPTS1603_longmode"
    
    mode     = 'air'
    mode     = 'short'
    mode     = 'long'

    outtype  = 'FLH'
    #XYZbase  = NICArefpos
    
    rnx_base_lis  = glob.glob(rnx_base_dir  + '/*o')
    rnx_rover_lis = glob.glob(rnx_rover_dir + '/*249*') + glob.glob(rnx_rover_dir + '/*251*')
    rnx_rover_lis = glob.glob(rnx_rover_dir + '/*250*')

    print('aaaa' ,  rnx_base_lis ,  rnx_rover_lis) 
    for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):
        print((rnx_base,rnx_rover))

        if os.path.basename(rnx_base)[4:7] == os.path.basename(rnx_rover)[4:7]:
    
            XYZbase = refposdic[os.path.basename(rnx_base)[0:4].upper()]
            softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                                      experience_prefix,XYZbase,mode=mode)
                              

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
    
    working_dir       = '/home/psakicki/THESE/DATA/1604_BOUEES/PROCESSING/TRACK_REBOOT1sec_long'
    experience_prefix = "TRACK_BOUEES_AIX_REBOOT1sec_long"
    
    mode     = 'air'
    mode     = 'long'
    outtype  = 'XYZ'
    interval = 1 #if None, interval of the rover
    
    XYZrover = [4436825.8548,   -90955.8009,  4565863.4535]
    
    rnx_base_lis  = glob.glob(rnx_base_dir  + '/*roya*87*o') + \
                    glob.glob(rnx_base_dir  + '/*man2*87*o') + \
                    glob.glob(rnx_base_dir  + '/*bres*87*o') + \
                    glob.glob(rnx_base_dir  + '/*angl*87*o') + \
                    glob.glob(rnx_base_dir  + '/*auni*87*o') + \
                    glob.glob(rnx_base_dir  + '/*chph*87*o') + \
                    glob.glob(rnx_base_dir  + '/*smne*87*o') + \
                    glob.glob(rnx_base_dir  + '/*ildx*87*o')
                    
    rnx_base_lis  = glob.glob(rnx_base_dir  + '/*ildx*87*o')


    rnx_rover_lis = []
    for rnx_rover_dir in (rnx_rover_dir_1,):
        rnx_rover_lis = rnx_rover_lis + glob.glob(rnx_rover_dir + '/*87*o')
     
    argtuplis = []     
    for (rnx_base,rnx_rover) in itertools.product(rnx_base_lis,rnx_rover_lis):
        print((rnx_base,rnx_rover))

        if os.path.basename(rnx_base)[4:7] == os.path.basename(rnx_rover)[4:7]:
    
            XYZbase = refposdic[os.path.basename(rnx_base)[0:4].upper()]
            argtup = (rnx_rover,rnx_base,working_dir,
                                      experience_prefix,XYZbase,XYZrover,
                                      outtype,mode,interval)
            argtuplis.append(argtup)
            softs_runner.track_runner(*argtup)
            
#    import multiprocessing as mp    
#    nbproc = 1
#    pool = mp.Pool(processes=nbproc)
#    results  = [pool.apply(softs_runner.track_runner, args=x) for x in argtuplis]
#    results2 = [e.get() for e in results] 

if 0:
    rnx_rover    = '/home/psakicki/THESE/DATA/1610_MASCARET/TOPCON_RAW_GOOD/base292z.16d.Z'
    rnx_rover    = "/home/psakicki/THESE/DATA/1610_MASCARET/TOPCON_RAW_GOOD/BASE/1018_ponton/base292Z.16o"
    rnx_base     = "/home/psakicki/THESE/DATA/1610_MASCARET/base/lbrd2920.16o"

    working_dir       = '/home/psakicki/THESE/DATA/1610_MASCARET/TRACK'
    experience_prefix = "MASCARET"
    
    mode     = 'air'
    outtype  = 'XYZ'
    
    XYZbase  = [4542413.8600 , -41847.1800 , 4462296.0930]
    XYZrover = [4543906.59545,-28703.3707673,4460850.80662]

    softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                              experience_prefix,mode=mode,calc_center='igr',
                              XYZbase=XYZbase,XYZrover=XYZrover)
                              
if 0:                     
    ENSGrefpos       = [4201575.85487 ,   189861.53838  ,   4779065.51962 ] 
    NICArefpos_RGF93 = [4581809.283   ,   581031.772    ,   4384492.682   ]
    NICArefpos       = [4581808.8798  ,   581032.2302   ,   4384493.0375  ]
    
    working_dir   = "/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/PROCESSED/TRACK"
    experience_prefix = "GEODESEA_NICA_REBOOT"
    
    mode     = 'long'
    outtype  = 'FLH'
    XYZbase  = NICArefpos
    
    rnx_base = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/1sec/nica/nica1730.15o'
    rnx_rover = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_GEODESEA/REBOOT_4_CNFG2_16/RINEX/gspl173A.15d.Z'
    
    softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                              experience_prefix,XYZbase,mode=mode)                           

    
if 0:                     
    working_dir   = "/home/psakicki/THESE/DATA/1611_GLACIER_AW/PROCESSING/TRACK_ATM_std"
    experience_prefix = "ARGENTIERE_atm"
    
    mode     = 'air'
    outtype  = 'FLH'
    
    rnx_base  = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argr1330.15o'
    rnx_rover = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argg1330.15o'
    
    XYZbase = [4411392.0999 ,  542028.3343 ,  4563154.0130]
    
    softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                              experience_prefix,XYZbase,mode=mode)  

if 0:                     
    working_dir   = "/home/psakicki/THESE/DATA/1611_GLACIER_AW/PROCESSING/TRACK_ATM_std"
    experience_prefix = "ARGENTIERE_atm"
    
    mode     = 'air'
    outtype  = 'FLH'
    
    rnx_base  = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argr1330.15o'
    rnx_rover = '/home/psakicki/THESE/DATA/1611_GLACIER_AW/argg1330.15o'
    
    XYZbase = [4411392.0999 ,  542028.3343 ,  4563154.0130]
    
    softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                              experience_prefix,XYZbase,mode=mode)  
    
    
if 0:                     
    working_dir   = "/home/psakicki/THESE/DATA/1702_NAPPE_EP/PROCESSING/TRACK_AIR"
    experience_prefix = "NAPPE_BRST"
    
    mode     = 'air'
    outtype  = 'FLH'
    
    rnx_base  = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/brst3350.16o'
    rnx_rover = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/NAPP3350.16o'
    rnx_rover = '/home/psakicki/THESE/DATA/1702_NAPPE_EP/RINEX/MICR3350.16o'

    XYZbase = [4231162.433449181, -332746.4665562841, 4745131.043373224] # BRST @ 2016.9125683060108

    softs_runner.track_runner(rnx_rover,rnx_base,working_dir,
                              experience_prefix,XYZbase,mode=mode)  

if 0:
    # conversion de GINS LISTING 2 ATM GAMIT
    IN  = '/home/psakicki/SOFTWARE_INSTALLED_2/GINS_NEW/gin/batch/listing/GLACIER_AW_argg_23873_2015_133_01s_xyz_0.yml.170127_044038.170127_045106.gins'
    OUT = '/home/psakicki/aaa_FOURBI/'
    gcls.MZB_GINS_2_ATM_GAMIT(IN,OUT)    