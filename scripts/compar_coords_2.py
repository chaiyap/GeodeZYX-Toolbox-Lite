# -*- coding: utf-8 -*-
"""
herité de :
/home/psakicki/THESE/CODES/CodePython/posi_bato/posi_bato_class_gpsa.py
"""

from geoclass import *
import geodetik as geok
import copy
import itertools


# tout le AL le doy 94 avec RTKLIB
#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gav1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gtr1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gba1_94_mk3a.out',
#            '/home/psakicki/THESE/DATA/1404_Tests_GPSA_Brest/DATA/Acoustic_TB/SORT/D2_gyro_posi.csv']

# Toutes les softs avec GOR94
#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94_reprise/R2/ALL094_SHORTnew.XYZ.GOR1.L1+L2',
#            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GOR1_94_02s.140704_100628.gins',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step1/tdp_final',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step2/tdp_final',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step3/tdp_final',
#            '/home/psakicki/THESE/DATA/1404_Tests_GPSA_Brest/DATA/Acoustic_TB/SORT/D2_gyro_posi.csv']

# GOR 94 plus specifique , softs valides + comparasion des steps gipsy
#filelist = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94_reprise/R2/ALL094_SHORTnew.XYZ.GOR1.L1+L2',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
#            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GOR1_94_02s.140704_100628.gins',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step3/tdp_final']

#filelist = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94_reprise/R2/ALL094_SHORTnew.XYZ.GOR1.L1+L2',
#             '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step1/tdp_final',
#             '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step2/tdp_final',
#             '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step3/tdp_final']

#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GOR1.L1+L2',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step3/tdp_final',
#            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GOR1_94_02s.140704_100628.gins',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94_RENN/ALL094_RENN.XYZ.GOR1.L1+L2',
#            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gor1.tdp.llh',
#            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gor1.tdp.llh']

# GAV 94 plus specifique , softs valides + comparasion des steps gipsy

#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/XYZ/gpsa_diff_brst_gav1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GAV1.L1+L2',
#            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GAV1_94_02s.140704_173835.gins',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGAV1/step3/tdp_final']
#
#
#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/XYZ/gpsa_diff_brst_gav1_94_mk3a.out',
#             '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGAV1/step1/tdp_final',
#             '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGAV1/step2/tdp_final',
#             '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGAV1/step3/tdp_final']
#

#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gav1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GAV1.L1+L2',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGAV1/step3/tdp_final',
#            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GAV1_94_02s.140704_173835.gins',
#            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gav1.tdp.llh',
#            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gav1.tdp.llh',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94_RENN/ALL094_RENN.XYZ.GAV1.L1+L2',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-RENN/gpsa_diff_renn_gav1_94_mk4a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-SMNE/gpsa_diff_smne_gav1_94_mk4a.out']

# GTR 94 plus specifique , softs valides + comparasion des steps gipsy
#
#
#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/XYZ/gpsa_diff_brst_gtr1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GTR1.L1+L2',
#            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GTR1_94_02s.140704_174255.gins',
#            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGTR1/step3/tdp_final']
#
#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gtr1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GTR1.L1+L2',
#             '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGTR1/step3/tdp_final',
#             '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GTR1_94_02s.140704_174255.gins',
#             '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gtr1.tdp.llh',
#             '/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gtr1.tdp.llh']
##             '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-RENN/gpsa_diff_renn_gtr1_94_mk4a.out',
##             '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-SMNE/gpsa_diff_smne_gtr1_94_mk4a.out']


# MEME RUN avec les 4 stations
#filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gtr1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gav1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
#            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gba1_94_mk3a.out']

# Juste les GIPSY bosser pour validation
#filelist = ['/home/psakicki/THESE/DATA/1409_GIPSY_PB/gav1.tdp.llh',
#            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gor1.tdp.llh',
#            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gtr1.tdp.llh']


# ======== LES BOSSER MK2 ========
# GOR94
#filelist1 = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94_reprise/R2/ALL094_SHORTnew.XYZ.GOR1.L1+L2',
#'/home/psakicki/gin/batch/listing/good_results/ABfVB2_GOR1_94_02s.140704_100628.gins',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/gor1.tdp.llh',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gor1.tdp.llh',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data30secMK2/gor1.tdp.llh']
#
#
#filelist2 = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GAV1.L1+L2',
#'/home/psakicki/gin/batch/listing/good_results/ABfVB2_GAV1_94_02s.140704_173835.gins',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/gav1.tdp.llh',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gav1.tdp.llh',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data30secMK2/gav1.tdp.llh']
#
#filelist3 = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GTR1.L1+L2',
#'/home/psakicki/gin/batch/listing/good_results/ABfVB2_GTR1_94_02s.140704_174255.gins',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/gtr1.tdp.llh',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gtr1.tdp.llh',
#'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data30secMK2/gtr1.tdp.llh']

#filelistlist = [filelist1 , filelist2 , filelist3 ]

# ------ Graph avec RENN et SMNE ------ 
filelist = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GAV1.L1+L2',
            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGAV1/step3/tdp_final',
            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GAV1_94_02s.140704_173835.gins',
            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gav1.tdp.llh',
            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94_RENN/ALL094_RENN.XYZ.GAV1.L1+L2',
            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-RENN/gpsa_diff_renn_gav1_94_mk4a.out',
            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-SMNE/gpsa_diff_smne_gav1_94_mk4a.out']

manunamelist = ['diff TRK BRST','diff RLIB BRST','PPP GINS','PPP GIPSY','diff TRK RENN','diff RLIB RENN','diff RTKLIB SMNE']
filelistlist = [filelist]


#  ======= LES GRAPHES POUR PRESENTATIONS =========

if 0:
    # mise en evidence que le RTK est pourri
    #filelist = [ '/home/psakicki/THESE/RUNNING_EXP/track/doy_94_reprise/R2/ALL094_SHORTnew.XYZ.GOR1.L1+L2',
    #            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
    #            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GOR1_94_02s.140704_100628.gins',
    #            '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gor1.tdp.llh',
    #            '/home/psakicki/THESE/DATA/1404_Tests_GPSA_Brest/DATA/Acoustic_TB/SORT/D2_gyro_posi.csv']
    #            
    ## Compar pour GAV
    filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gav1_94_mk3a.out',
                '/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GAV1.L1+L2',
                '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GAV1_94_02s.140704_173835.gins',
                '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gav1.tdp.llh']
    
    ## Compar pour GTR
    filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gtr1_94_mk3a.out',
                '/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GTR1.L1+L2',
                '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GTR1_94_02s.140704_174255.gins',
                '/home/psakicki/THESE/DATA/1409_GIPSY_PB/gtr1.tdp.llh']
                
    FLH_REF = Point( 48.38049469 , -4.49659227 , 65.8255 , initype='FLH' ) # coords de la stat de brest
    XYZ_REF = Point( 4231162.4810, -332746.5126 , 4745131.0156 )
    
    # et d'une window en manuelle pour periode déconnante
    windel = [[dt.datetime(2014,0o4,0o4,0o6,26,30),dt.datetime(2014,0o4,0o4,0o6,27,30)]]

# ============   COMPARAISON TOIT 3   =================

if 0:
    filelist = ['/home/psakicki/THESE/RUNNING_EXP/track/TESTOIT3/OUTPUT/TESTOIT3_roof_ilel_2015_161.pos.XYZ.ROOF.L1+L2',
                "/home/psakicki/THESE/RENDU/RESULTATS/1506_TEST_TOIT_3/2015-06-10.ROOF.sum",
                "/home/psakicki/THESE/RENDU/RESULTATS/1506_TEST_TOIT_3/TESTOI3_MK8_roof_23901_2015_161_01s_a4.yml.150709_180737.150709_180921.gins",
                "/home/psakicki/THESE/RENDU/RESULTATS/1506_TEST_TOIT_3/TESTOI3_MK8_roof_23901_2015_161_01s_a4.yml.150708_155458.150708_155639.gins",
                "/home/psakicki/THESE/RENDU/RESULTATS/1506_TEST_TOIT_3/test_roof_ilel_2015_161.out"]
     
    XYZ_REF = Point( 4426043.8569996189, -89428.884283183841, 4576297.0765448613)
    windel  = []

# ============   COMPARAISON TOIT 3   =================

#                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK/TRACK_TOITDPTS1603_ensg_chph_2015_250.pos.XYZ.ENSG.LC',
#                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK/TRACK_TOITDPTS1603_ensg_man2_2015_250.pos.XYZ.ENSG.LC',
#                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK/TRACK_TOITDPTS1603_ensg_mlvl_2015_250.pos.XYZ.ENSG.LC',
#                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK/TRACK_TOITDPTS1603_ensg_sirt_2015_250.pos.XYZ.ENSG.LC',
#                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/TRACK/TRACK_TOITDPTS1603_ensg_smne_2015_250.pos.XYZ.ENSG.LC',


if 1:
    filelist = ['/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/NRCAN/ensg2500.pos',
                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/RTKLIB/TOITDPTS_multistats_ensg_smne_2015_250.out',
                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/RTKLIB/TOITDPTS_multistats_ensg_sirt_2015_250.out',
                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/RTKLIB/TOITDPTS_multistats_ensg_mlvl_2015_250.out',
                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/RTKLIB/TOITDPTS_multistats_ensg_man2_2015_250.out',
                '/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/RTKLIB/TOITDPTS_multistats_ensg_chph_2015_250.out']






    XYZ_REF = Point( *[4201575.85487 ,   189861.53838  ,   4779065.51962 ]) # COORD OF ENSG STAT
    windel  = []



# =========================================================
# ================  FIN DES CHARGEMENTS  ==================
# =========================================================

filelistlist = [filelist]
        
dicname = dict()
dicname['gpsa_diff'] = 'diff. RTKLIB'
dicname['L1\+L2'] = 'diff. TRACK'
dicname['gins'] = 'PPP GINS'
dicname['tdp\.llh'] = 'PPP GIPSY'
dicname['.csv'] = 'RTK (temps reel)'

# CHARGEMENT DES TS à traitement spécial
tslist_spec = []
L = glob.glob('/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/GINS_KF0/*gins')
tsgins = read_gins_multi_raw_listings(L,'kine')
L = glob.glob('/home/psakicki/THESE/DATA/1509_TOIT_DPTS/PROCESSING/OK_1/GIPSYAPPS/2/*tdp')
tsapps = read_gipsy_tdp_list(L)
tslist_spec = [tsgins , tsapps]

# CHARGEMENT DES TS
tslistlist = []
for filelist in filelistlist:
    tslist = tslist_spec 
    for i,ifile in enumerate(filelist):
        ts = TimeSeriePoint()
        ts.readfile(ifile)
        ts.ENUcalc(XYZ_REF)
        ts.decimate(30)
        
        #Renomage semi auto en fonction du type de fichier
        if 1:
            for k in list(dicname.keys()):
                print(k)
                if bool(re.search(k,ifile)):
                    ts.name = dicname[k]
                    print(dicname[k])
        
        # Renommage 100% manu
        if 0:
            ts.name = manunamelist[i]
        
        tslist.append(ts)
    
    # adding the ref point
    tsref = TimeSeriePoint()
    tsref.from_uniq_point(XYZ_REF,
                          tslist[0].startdate(),
                          tslist[0].enddate())
    tsref.ENUcalc(XYZ_REF)
    tsref.meta_set(name='ref. true coords.' , stat='ENSG')
    tslist = [tsref] + tslist
    
    tslistlist.append(tslist)
    
   
# DEFINITION DE LA WINDOW EN FONCTION DU START/END DE LA 1ER TS
tslist = tslistlist[0] 
window = [tslist[0].startdate(),tslist[0].enddate()]

# APPLICATION DES WINDOWS
figure(1)    
clf()
for ts in tslist:
    ts.timewin([window])
#    ts.timewin(windel,'del')
    ts.plot()

# start / end name
snam=0 # 15
enam=100

figure(2)    
clf()
aaa = compar(tuple(tslist),seuil=10,mode="keep",coortype='ENU',Dtype='2D',namend = enam)

figure(4)
clf()
aaa = compar(tuple(tslist),seuil=10,mode="keep",coortype='ENU',Dtype='3D',namend = enam)

for dic in aaa:
    print(dic['name'][snam:enam], np.nanmean(dic['dD']) , np.nanstd(dic['dD']))
