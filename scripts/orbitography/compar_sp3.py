#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:18:10 2017

@author: adminuser
"""

from megalib import *
from natsort import natsorted, ns

import geoclass as gcls

from tabulate import tabulate
import softs_runner

### SIMPLE COMPARISON
if 1:
    p1 = "/home/adminuser/Documents/1709_compar_orbit/data/CRASH2017287/BAD/2017_287_prod.sp3"
    p2 = "/home/adminuser/Documents/1709_compar_orbit/data/CRASH2017287/OK/2017_287_prod.sp3"
    
    p1 = "/home/adminuser/Documents/1709_compar_orbit/data/CRASH2017287/BAD/2017_287_predi.sp3"
    p2 = "/home/adminuser/Documents/1709_compar_orbit/data/CRASH2017287/OK/2017_287_predi.sp3"
    
    p1 = '/home/adminuser/Documents/1709_compar_orbit/data/1711_new_vs_old_epos_vers/2017_309/p1r19740.sp3'
    p2 = '/home/adminuser/Documents/1709_compar_orbit/data/1711_new_vs_old_epos_vers/2017_309true/p1r19740.sp3'
     
    p1 = '/home/adminuser/aaa_FOURBI/p1r19780_5minR.sp3'
    p2 = '/home/adminuser/aaa_FOURBI/p1r19780_5minG.sp3'
    
    p1 = "/home/psakicki/aaa_FOURBI/TMP_19862_Crash/RERUN/1/p1r19862_5min.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/TMP_19862_Crash/RERUN/2/p1r19862_5min.sp3"
    
    
    p1 = "/home/psakicki/aaa_FOURBI/COMPAR_BUG_UPDATE_TMP/p3r19972.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/COMPAR_BUG_UPDATE_TMP/2018_107_run1/OUT_PROD/2018_107_prod.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/COMPAR_BUG_UPDATE_TMP/2018_107/OUT_PROD/2018_107_prod.sp3"

    p1 = "/home/psakicki/aaa_FOURBI/COMPAR_BUG_UPDATE_TMP/2018_107_run1/OUT_PROD/2018_107_prod.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/COMPAR_BUG_UPDATE_TMP/2018_107/OUT_PROD/2018_107_prod.sp3"
    
    p1 = "/home/psakicki/aaa_FOURBI/DL_TMP/R1/p1r19972.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/DL_TMP/R2/p1r19972.sp3"
  
    p1 = "/home/psakicki/aaa_FOURBI/SP3_TMP/com19900.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/SP3_TMP/gbm19900.sp3"

    p1 = "/home/psakicki/aaa_FOURBI/aaaaaaaa/igs19935.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/aaaaaaaa/gbm19935.sp3"
    
    p1 = "/home/psakicki/aaa_FOURBI/aaaaaaaa/igs19930.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/aaaaaaaa/gbm19930.sp3"
    
    p1 = "/home/psakicki/aaa_FOURBI/1904_G4_bias/p1_20463.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/1904_G4_bias/p2_20463.sp3"
    

    name1=''
    name2=''
    
    p2="/home/psakicki/aaa_FOURBI/wk1989/com19896.sp3"
    p1="/home/psakicki/aaa_FOURBI/wk1989/grm19896.sp3"
    name1='GFZ'
    name2='Bern Obs.'
    save_plot=True
    save_plot_dir="/home/psakicki/aaa_FOURBI/wk1989"
    
    
    p1="/home/psakicki/aaa_FOURBI/compar_predi_rapid/p1p20220.sp3"
    p2="/home/psakicki/aaa_FOURBI/compar_predi_rapid/p1r20220.sp3"
    name1=''
    name2=''
    
    
    p1 = "/home/psakicki/aaa_FOURBI/1904_G4_bias/p1_20463.sp3"
    p2 = "/home/psakicki/aaa_FOURBI/1904_G4_bias/p2_20463.sp3"
    
    p2 = "/home/psakicki/aaa_FOURBI/1904_G4_bias/p3_20463.sp3"
    

    name1=''
    name2=''
    
    save_plot=True
    save_plot_dir=os.path.dirname(p1)    
    
    RTNoutput         = True # False only for debug & personal interest !! 
    convert_ECEF_ECI  = True # False only for debug !!
    clean_null_values = "any" # Can be "all" , "any", False or True (True => "all")
    
    sats_used_list = ["G"] # G,E,R,C ...
    
    
    
    Diff_all    = gcls.compar_orbit(p1,p2,
                                    sats_used_list=sats_used_list,
                                    RTNoutput=RTNoutput,
                                    convert_ECEF_ECI=convert_ECEF_ECI,
                                    name1=name1,name2=name2,
                                    clean_null_values = clean_null_values,
                                    step_data = 900)
    
    _           = gcls.compar_orbit_plot(Diff_all,
                                        save_plot=save_plot,
                                        save_plot_dir=save_plot_dir)
    
    ComparTable = gcls.compar_orbit_table(Diff_all)


### MORE COMPLEX CASE : LOOP FOR SEARCHING SAME ORBIT NAME IN DIFFERENTS FOLDERS
if 0:
    p2_dir_list = ['/home/adminuser/Documents/1709_compar_orbit/data/FINALorbs/FINALmod1',
    '/home/adminuser/Documents/1709_compar_orbit/data/FINALorbs/FINALatx1967ORI',
    '/home/adminuser/Documents/1709_compar_orbit/data/FINALorbs/FINAL',
    '/home/adminuser/Documents/1709_compar_orbit/data/FINALorbs/FINALatx1967MOD',
    '/home/adminuser/Documents/1709_compar_orbit/data/FINALorbs/FINALorig_good']
    
    orbnam = '/ANA/2017/2017_222/ORB/2017_222_orb_1d.sp3'

    
    p_ref = '/home/adminuser/Documents/1709_compar_orbit/data/FINALorbs/OFFICIAL/2017_222_orb_1d.sp3'
        
    for p2_dir in p2_dir_list:
        p2 = p2_dir + orbnam
        
        D1 = gcls.read_sp3(p_ref)
        D2 = gcls.read_sp3(p2)
        
        name1 = p_ref.split('/')[7]
        name2 = p2.split('/')[7]
        
        RTNoutput        = True # False only for debug & personal interest !! 
        convert_ECEF_ECI = True # False only for debug !!
    
        sats_used_list = ['E'] # G,E,R,C ...
        
        Diff_all    = gcls.compar_orbit(p_ref,p2,
                                    sats_used_list=sats_used_list,
                                    RTNoutput=RTNoutput,
                                    convert_ECEF_ECI=convert_ECEF_ECI,
                                    name1=name1,name2=name2)

        
        _           = gcls.compar_orbit_plot(Diff_all)
        ComparTable = gcls.compar_orbit_table(Diff_all)



### DOWNLADING REFERENCE ORBITS
if 0:
    archivedir_base = "/home/adminuser/Documents/1709_compar_orbit/data/REF_ORBITS"
    
    startdate = geok.sp3name2dt('p1r19681_5min')
    enddate   = geok.sp3name2dt('p1r19696_5min')
    sp3listZ = []
    
    
    for ac in ('tum','grm','gbm'):
        archivedir = archivedir_base + '/' + ac
        gf.create_dir(archivedir)
        sp3list_tmp = softs_runner.multi_downloader_orbs_clks(archivedir,
                                                              startdate,enddate,
                                                              ac,archtype ='/',
                                                              archive_center='cddis_mgex')
        sp3listZ = sp3listZ + sp3list_tmp
    
    
    sp3list = [gf.uncompress(e) for e in sp3listZ]



### COMPARISON FOR ECLIPSE & ALBEDO
if 0:
    

# =============================================================================
    
    plt_name_prefix = 'albedo_rapid_wrt_gbm'
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/REF_ORBITS/gbm/'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAa_1//'
    
    plt_name_prefix = 'eclipse_rapid_wrt_gbm'    
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/REF_ORBITS/gbm/'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAn_2//'
    
    plt_name_prefix = 'albedo_rapid_wrt_grg'
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/REF_ORBITS/grm/'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAa_1//'

    plt_name_prefix = 'eclipse_rapid_wrt_grg'    
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/REF_ORBITS/grm/'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAn_2//'
    
    plt_name_prefix = 'eclipse_rapid_wrt_pf1_rapid_like'    
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAo_1//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAn_2//'

    plt_name_prefix = 'albedo_rapid_wrt_pf1_rapid_like'
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAo_1//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/RAa_1//'


    p1list = glob.glob(p1dir + '*sp3')
    p2list = glob.glob(p2dir + '*sp3')
    
    p1date = [geok.sp3name2dt(e) for e in p1list]
    p2date = [geok.sp3name2dt(e) for e in p2list]
    
    
# =============================================================================
    

    plt_name_prefix = 'eclipse_final2_wrt_pf1_final2_like'    
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/FI2/FIo_2//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/FI2/FIn_2//'

    plt_name_prefix = 'albedo_final2_wrt_pf1_final2_like'
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/FI2/FIo_2//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/FI2/FIa_2//'


    p1list = glob.glob(p1dir + '*sp3')
    p2list = glob.glob(p2dir + '*sp3')
    
    p1date = [geok.doy2dt(int(os.path.basename(e).split('_')[0]),int(os.path.basename(e).split('_')[1])) for e in p1list]
    p2date = [geok.doy2dt(int(os.path.basename(e).split('_')[0]),int(os.path.basename(e).split('_')[1])) for e in p2list]    
    

# =============================================================================   
    plt_name_prefix = 'aaaa'
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/FIo_1//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/FI2/FIo_2//'
    
    
    plt_name_prefix = 'aaaa'
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/FIa_1//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/FI2/FIa_2//'
    
    p1list = glob.glob(p1dir + '*sp3')
    p2list = glob.glob(p2dir + '*sp3')
    
    p1date = [geok.doy2dt(int(os.path.basename(e).split('_')[0]),int(os.path.basename(e).split('_')[1])) for e in p1list]
    p2date = [geok.doy2dt(int(os.path.basename(e).split('_')[0]),int(os.path.basename(e).split('_')[1])) for e in p2list]


# =============================================================================

    p_datelist = sorted(list(set(p1date).intersection((p2date))))
    
    p1bool = [True if e in p_datelist else False for e in p1date]
    p2bool = [True if e in p_datelist else False for e in p2date]
    
    plt_outdir_basis = "/home/adminuser/Documents/1709_compar_orbit/plots" 
    
    plt_outdir       = os.path.join(plt_outdir_basis , plt_name_prefix)
    
    gf.create_dir(plt_outdir)
    
# =============================================================================


    plt_name_prefix = 'eclipse_final_wrt_pf1_final_like'    
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/FIo_1//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/FIn_1//'

    
    plt_name_prefix = 'albedo_final_wrt_pf1_final_like'
    p1dir = '/home/adminuser/Documents/1709_compar_orbit/data/FIo_1//'
    p2dir = '/home/adminuser/Documents/1709_compar_orbit/data/FIa_1//'
    
    p1list = glob.glob(p1dir + '*sp3')
    p2list = glob.glob(p2dir + '*sp3')
    
    p1date = [geok.doy2dt(int(os.path.basename(e).split('_')[0]),int(os.path.basename(e).split('_')[1])) for e in p1list]
    p2date = [geok.doy2dt(int(os.path.basename(e).split('_')[0]),int(os.path.basename(e).split('_')[1])) for e in p2list]
    

    for pdat in p_datelist:
        
        #plt.close('all')
        
        p1 = p1list[p1date.index(pdat)]
        p2 = p2list[p2date.index(pdat)]
        
        name1=''
        name2=''
    
        RTNoutput        = True # False only for debug & personal interest !! 
        convert_ECEF_ECI = True # False only for debug !!
        
        sats_used_list = ['E'] # G,E,R,C ...
        
        Diff_all    = gcls.compar_orbit(p1,p2,
                                        sats_used_list=sats_used_list,
                                        RTNoutput=RTNoutput,
                                        convert_ECEF_ECI=convert_ECEF_ECI,
                                        name1=name1,name2=name2)
        _           = gcls.compar_orbit_plot(Diff_all)
        ComparTable = gcls.compar_orbit_table(Diff_all)
                
        TabPrint =  tabulate(ComparTable,headers="keys",floatfmt=".4f")
        
        plt_outname = plt_name_prefix + '_' + gf.join_improved('_',*geok.dt2gpstime(pdat))
        gf.write_in_file(TabPrint , plt_outdir , plt_outname)
        
        for extplt in ('svg','pdf','png'):
            outpath = os.path.join(plt_outdir, plt_outname + '.' + extplt)
            plt.savefig(outpath)
