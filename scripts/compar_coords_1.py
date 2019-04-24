"""
herité de :
/home/psakicki/THESE/CODES/CodePython/posi_bato/posi_bato_class_gpsa.py
privilegier la v2
"""




from geoclass import *
import geodetik as geok
import copy
import itertools




# tout le AL le doy 94 avec RTKLIB
filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gav1_94_mk3a.out',
            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gtr1_94_mk3a.out',
            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
            '/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gba1_94_mk3a.out',
            '/home/psakicki/THESE/DATA/1404_Tests_GPSA_Brest/DATA/Acoustic_TB/SORT/D2_gyro_posi.csv']

# Toutes les softs avec GOR94
filelist = ['/home/psakicki/THESE/RUNNING_EXP/RTKLIB/EXP_BREST-BRST_DIVERS/XYZ/gpsa_diff_brst_gor1_94_mk3a.out',
            '/home/psakicki/THESE/RUNNING_EXP/track/doy_94_reprise/R2/ALL094_SHORTnew.XYZ.GOR1.L1+L2',
            '/home/psakicki/gin/batch/listing/good_results/ABfVB2_GOR1_94_02s.140704_100628.gins',
            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step1/tdp_final',
            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step2/tdp_final',
            '/home/psakicki/THESE/RUNNING_EXP/gipsy_exp/brest_mk2/autoGOR1/step3/tdp_final',
            '/home/psakicki/THESE/DATA/1404_Tests_GPSA_Brest/DATA/Acoustic_TB/SORT/D2_gyro_posi.csv']

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
filelist1 = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94_reprise/R2/ALL094_SHORTnew.XYZ.GOR1.L1+L2',
'/home/psakicki/gin/batch/listing/good_results/ABfVB2_GOR1_94_02s.140704_100628.gins',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/gor1.tdp.llh',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gor1.tdp.llh',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data30secMK2/gor1.tdp.llh']


filelist2 = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GAV1.L1+L2',
'/home/psakicki/gin/batch/listing/good_results/ABfVB2_GAV1_94_02s.140704_173835.gins',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/gav1.tdp.llh',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gav1.tdp.llh',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data30secMK2/gav1.tdp.llh']

filelist3 = ['/home/psakicki/THESE/RUNNING_EXP/track/doy_94/ALL094_SHORT.XYZ.GTR1.L1+L2',
'/home/psakicki/gin/batch/listing/good_results/ABfVB2_GTR1_94_02s.140704_174255.gins',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/gtr1.tdp.llh',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data1Hz/gtr1.tdp.llh',
'/home/psakicki/THESE/DATA/1409_GIPSY_PB/data30secMK2/gtr1.tdp.llh']

filelistlist = [filelist1 , filelist2 , filelist3 ]

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

filelistlist = [filelist]

# GINS 
        
dicname = dict()
dicname['gpsa_diff'] = 'diff. RTKLIB'
dicname['L1\+L2'] = 'diff. TRACK'
dicname['gins'] = 'PPP GINS'
dicname['tdp\.llh'] = 'PPP GIPSY'
dicname['.csv'] = 'RTK (temps reel)'

FLH_BRST = Point( 48.38049469 , -4.49659227 , 65.8255 )
XYZ_BRST = Point( 4231162.4810, -332746.5126 , 4745131.0156 )

tslistlist = []
for filelist in filelistlist:
    tslist = []
    for i,ifile in enumerate(filelist):
        a = TimeSeriePoint()
# Pour du travail a distance
#        a.readfile('/run/user/1000/gvfs/sftp:host=calipso.univ-lr.fr,user=psakicki' +ifile)
        a.readfile(ifile)

        a.ENUcalc(XYZ_BRST)
        a.decimate(30)
        
        # Renomage des TS
#        for k in dicname.keys():
#            print k
#            if bool(re.search(k,ifile)):
#                a.name = dicname[k]
#                print dicname[k]
        
        # Renommage manu
#        a.name = manunamelist[i]
        
        
        tslist.append(a)
    tslistlist.append(tslist)
    
    
tslist = tslistlist[0]
    
window = [tslist[0].startdate(),tslist[0].enddate()]

figure(1)    
clf()
for ts in tslist:
    ts.timewin([window])
    ts.timewin([[dt.datetime(2014,0o4,0o4,0o6,26,30),dt.datetime(2014,0o4,0o4,0o6,27,30)]],'del')
    ts.plot()
    
#TS0 = tslist[0]
#TS0.aleapt()
#TS1 = tslist[1]
#TS1.aleapt()
#
#wink = time_gap(TS0,mode="keep")
#wind = time_gap(TS0,mode="del")
#
#Tref = TS0.to_list()[3]
#
#TS1k = time_win(TS1,wink,mode='keep')
#TS1d = time_win(TS1,wind,mode='del')
#
#T = TS0.to_list()[3]

#tslist.append(copy.deepcopy(tslist[-1]))
#
#tslist[-1].add_offset(0.6,0.4,0)

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
