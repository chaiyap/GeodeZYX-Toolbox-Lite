import os
import subprocess
import time
import datetime as dt
import shutil
import itertools
import numpy as np


def doy2dt(year,days,hours=0,minutes=0,seconds=0):
    # All this because Python cant handle int with a starting with 0 (like 08)
    # => SyntaxError: invalid token
    year    = int(str(year))
    days    = int(str(days))
    hours   = float(str(hours))
    minutes = float(str(minutes))
    seconds = float(str(seconds))

    tempsecs = seconds + 60 * minutes + 3600 * hours
    finalsecs     = np.floor(tempsecs)
    finalmicrosec = np.round(tempsecs * 10**6)
    
    return dt.datetime(year, 1, 1) + dt.timedelta(days - 1) + \
    dt.timedelta(microseconds=finalmicrosec)
    

cluster_use = 0
wait_until_process_end = 0 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False

wait_time = 100*60  #activated only if wait_until_process_end = False 
wait_time = 0       #activated only if wait_until_process_end = False 

wait_sleeping_before_launch = 20

bunch_on_off = False

bj_check_on_off = False
bj_check_user   = 'psakicki'
bj_check_wait_time = 2*60

cln_global_reset = False

# W1959
startday = 2017203
endday   = 2017212

startday = 2017208
endday   = 2017208

# W1960
startday = 2017210
endday   = 2017219

# W1961
startday = 2017218
endday   = 2017226
# W1961 extract
startday = 2017221
endday   = 2017222

# W1961
startday = 2017218
endday   = 2017226

# INITIALISATION OF THE OPTIONAL ARGS
rod_list=[]
start_step=''
stop_step=''
task_only_step=''
#

configfile_dir  = "/dsk/ggsp_pf/PLAYGROUND/psakicki/CONFIG_FILES"

configfile_name = "CONFIG_TEST_RAPID_other_macromod.xml"
configfile_name = "CONFIG_GGSP_FINAL.xml"
configfile_name = "CONFIG_FILE_FINAL.xml"
configfile_name = "CONFIG_GGSP_RAPID_PS.xml"

rod_list=['clock30s']
rod_list=['predi']
rod_list=['clock30s','predi']

if 0:
    startday = 2017239
    endday   = 2017239
    configfile_name = "CONFIG_GGSP_RAPID_PS.xml"
    configfile_name = "CONFIG_GGSP_RAPID_PS_light.xml"
    configfile_name = "CONFIG_GGSP_RAPID_PS_light_n_mod.xml"
    rod_list=['clock30s','predi']
    if 0:
      start_step = '/predictions'
      start_step = '/analysis'
if 0:
    configfile_name = "CONFIG_GGSP_FINAL_PS.xml"
    rod_list=[]

if 0:
    configfile_name =  "CONFIG_FILE_FINAL.xml"
    rod_list=[]

if 0:
    # W1961
    startday = 2017270
    endday   = 2017273
    configfile_name =  "CONFIG_FILE_FINAL.xml"
    configfile_name =  "CONFIG_FILE_FINAL_atx1967_mod_atx.xml"
    configfile_name =  "CONFIG_FILE_FINAL_atx1967_orig_atx.xml"
    configfile_name =  "CONFIG_GGSP_FINAL_mod_full2.xml"
    configfile_name =  "CONFIG_GGSP_FINAL_mod_full2_new_atx.xml"
    rod_list=[]

if 0:
    # W1969
    startday = 2017290
    endday   = 2017290
    configfile_name =  "CONFIG_GGSP_FINAL_mod_full2_new_atx.xml"
    configfile_name =  "CONFIG_GGSP_FINAL_mod_full2.xml"


    rod_list=[]

if 0:
    startday = 2017271
    endday   = 2017271

    startday = 2017001
    endday   = 2017300

    startday = 2017272
    endday   = 2017272

    startday = 2017339
    endday   = 2017339
    wait_sleeping_before_launch = 3
    
    cluster_use                 = 1
    wait_until_process_end      = 0 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    cluster_use                 = 0
    wait_until_process_end      = 1 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False

    configfile_name = "PS_RAPID_light_4_eclipse_RAec.xml"

    rod_list=['clock30s','predi']
    if 0:
      start_step = '/analysis'
 
if 0:
    startday = 2017267
    endday   = 2017281

    cluster_use                 = 0
    wait_until_process_end      = 1 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 3

    cluster_use                 = 1
    wait_until_process_end      = 0 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 3

    configfile_name = "PS_RAPID_full_4_albedo_RAa2_for_local.xml"

    EPOS_bin_folder = "/dsk/igs2/soft_wrk/psakicki/SOFT_EPOS8_BIN/INTL64/"


    configfile_name = "PS_FINAL_4_origina_FIo.xml"
    #os.remove( os.path.join(EPOS_bin_folder,"qpdm7.out") )
    #shutil.copy(os.path.join(EPOS_bin_folder,"qpdm7.out_orig"), os.path.join(EPOS_bin_folder,"qpdm7.out"))

    configfile_name = "PS_FINAL_4_albedo_FIa.xml"
    #os.remove( os.path.join(EPOS_bin_folder,"qpdm7.out") )
    #shutil.copy(os.path.join(EPOS_bin_folder,"qpdm7.out_albedo"), os.path.join(EPOS_bin_folder,"qpdm7.out"))

    configfile_name = "PS_FINAL_4_eclipse_FIn.xml"
    #os.remove( os.path.join(EPOS_bin_folder,"qpdm7.out") )
    #shutil.copy(os.path.join(EPOS_bin_folder,"qpdm7.out_eclipse"), os.path.join(EPOS_bin_folder,"qpdm7.out"))


    rod_list=['clock30s','predi']
    if 0:
      start_step = '/analysis'


if 0:
    startday = 2017267
    endday   = 2017281

    cluster_use                 = 1
    wait_until_process_end      = 0 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 3

    configfile_name = "PS_FINAL_4_origina_FIo.xml"
    configfile_name = "PS_FINAL_4_albedo_FIa.xml"
    configfile_name = "PS_FINAL_4_eclipse_FIn.xml"
    
    configfile_name = "PS_RAPID_full_4_origina_RAo.xml"
    configfile_name = "PS_RAPID_full_4_eclipse_RAn.xml"
    configfile_name = "PS_RAPID_full_4_albedo_RAa.xml"


    rod_list=['clock30s','predi']
    if 0:
      start_step = '/analysis'


if 0:
    # Wtest
    startday = 2017323
    endday   = 2017329
    endday   = 2017336


    cluster_use                 = 0
    wait_until_process_end      = 1 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 5
    bunch_on_off    = False
    bunch_job_nbr   = 5
    bunch_wait_time = 60 * 60

    cluster_use                 = 1
    wait_until_process_end      = 0 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 5
    bunch_on_off    = True
    bunch_job_nbr   = 10
    bunch_wait_time = 60 * 60
    bj_check_on_off = False
    bj_check_user   = 'psakicki'
    bj_check_wait_time = 2*60
    bj_check_R_or_Q = ''

    cln_global_reset = 0

    # ORIGINAL 
    configfile_name = "PS_RAPID_GEI_1Oa.xml"
    configfile_name = "PS_RAPID_GEI_1Ua.xml"

    configfile_name = ["PS_RAPID_GEI_1Ua.xml","PS_RAPID_GEI_1Oa.xml"]
    configfile_name = ["PS_RAPID_GEI_1Ea.xml","PS_RAPID_GEI_1Ua.xml","PS_RAPID_GEI_1Oa.xml"]
    configfile_name = ["PS_RAPID_GEI_1Ea.xml","PS_RAPID_GEI_1Ua.xml","PS_RAPID_GEI_1Oa.xml","PS_RAPID_GEI_1Fa.xml","PS_RAPID_GEI_1Va.xml","PS_RAPID_GEI_1Pa.xml"]
    configfile_name = ["PS_RAPID_GEI_1Fa.xml","PS_RAPID_GEI_1Va.xml","PS_RAPID_GEI_1Pa.xml"]

    configfile_name = ["PS_RAPID_GEI_1Ua.xml","PS_RAPID_GEI_1Oa.xml"]
    configfile_name = ["PS_RAPID_GEI_1Ea.xml","PS_RAPID_GEI_1Fa.xml"]
    configfile_name = ["PS_RAPID_GEI_1Oc.xml","PS_RAPID_GEI_1Pc.xml"]
    configfile_name = "PS_RAPID_GEI_1Va.xml"
    configfile_name = "PS_RAPID_GEI_1Fa.xml"
    configfile_name = "PS_RAPID_GEI_1Ea.xml"
    startday = 2017331
    endday   = 2017336

    configfile_name = "PS_RAPID_GEI_1Oc.xml"
    startday = 2017335
    endday   = 2017336


    configfile_name = "PS_RAPID_GEI_1Pc.xml"
    startday = 2017323
    endday   = 2017336

    configfile_name = "PS_RAPID_GEI_1Ea.xml"
    startday = 2017336
    endday   = 2017336

    configfile_name = "PS_RAPID_GEI_1Fa.xml"
    startday = 2017332
    endday   = 2017336

    configfile_name = "PS_RAPID_GEI_1Va.xml"
    startday = 2017328
    endday   = 2017336

    configfile_name = "PS_RAPID_GEI_1Db.xml"
    startday = 2017323
    startday = 2017334
    endday   = 2017336

    rod_list=['clock30s','predi']
    if 0:
      start_step = '/analysis'
    
    
if 0:
    # Wtest
    endday   = 2017329
    startday = 2017323
    endday   = 2017336


    cluster_use                 = 1
    wait_until_process_end      = 0 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 5
    bunch_on_off    = True
    bunch_job_nbr   = 16
    bunch_wait_time = 60 * 60
    bj_check_on_off = False
    bj_check_user   = 'psakicki'
    bj_check_wait_time = 2*60
    bj_check_R_or_Q = ''

    cluster_use                 = 0
    wait_until_process_end      = 1 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 5
    bunch_on_off    = False
    bunch_job_nbr   = 5
    bunch_wait_time = 60 * 60

    cln_global_reset = 0

    configfile_name = "PS_FINAL_GEI_2Dc.xml"
    startday = 2017323
    endday   = 2017336

    startday = 2017322
    endday   = 2017322
    startday = 2017337
    endday   = 2017337


    configfile_name = "PS_RAPID_GEI_1Oc.xml"
    configfile_name = "PS_RAPID_full.xml"
    startday = 2017353
    endday   = 2017353

    rod_list=['clock30s','predi']
    if 0:
      start_step = '/analysis'
    
      
#### GWADA
if 1:
    # Wtest
    
    

    

    
    ############# ORBITS GFZ
    # Fin Experience GWADA (fin consistency EPOS, ECOM2) : 2018329
    # Fin Repro3 ready :  2018249
    startday = 2000134
    endday   = 2018249
    configfile_name = "CONFIG_FILE_GWA2A_v0B.xml"

    startday = 2018249
    endday   = 2018329
    configfile_name = "CONFIG_FILE_GWA2A_v0B_routine_orb.xml"

    ############# ORBITS GRGS
    # Fin Repro2 GRGS : 2013362


    startday = 2013362
    endday   = 2018329
    configfile_name = "CONFIG_FILE_GWA2A_v0B_routine_orb.xml"

    startday = 2000134
    endday   = 2013362
    configfile_name = "CONFIG_FILE_GWA2A_v0C_GRG_repro2.xml"



    
    cluster_use                 = 1
    wait_until_process_end      = 0 # only usefull when run in local, thus if cluster_use = True => wait_until_process_end = False
    wait_sleeping_before_launch = 1
    bunch_job_nbr   = 30
    bj_check_on_off = True
    bj_check_user   = 'psakicki'
    bj_check_wait_time = 30
    bj_check_R_or_Q = ''
    nb_jobs_max = 20

    configfile_dir  = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/01_Syncro_Server_TPX1/METADATA/config_EPOS/"
    
        
    Rnx_ORPHEON_new_file = "/wrk/sakic_xchg/GWA2A2018/RINEX/RINEX/GOOD/RENAG_ORPHEON_new_RINEX_clean.list"
    Rnx_ORPHEON_new_date_list = [l.strip().split("/")[-2] + l.strip().split("/")[-1][4:7] for l in open(Rnx_ORPHEON_new_file,"r+")]
    

    ### /dsk/repro3/ARCHIVE/IGS
    
    rod_list=[]
    if 0:
      start_step = '/analysis'

history_file_path = '/dsk/ggsp_pf/PLAYGROUND/psakicki/logs/history_cluster_loop.log'
logs_dir = '/dsk/ggsp_pf/PLAYGROUND/psakicki/logs/'

# END OF USER PARAMETERS
# ======================================================================


cln_global_path='/dsk/ggsp_pf/PLAYGROUND/psakicki/CONTROL/CNT_COMMON/CLN_GLOBAL'

CLN_GLOBAL="""%=CLN_GLOBAL 3.0
##########################################################################################
# File        : $HeadURL: svn://kg6/GGSP_PF/CONTROL/CNT_COMMON/CLN_GLOBAL $
# Last author : $Author: ggsppf $
# Last change : $Date: 2017-12-07 10:26:01 +0100 (Thu, 07 Dec 2017) $
# Revision    : $Rev: 1284 $
# Copyright   : GeoForschungsZentrum Potsdam
#
# Purpose     : TABLE OF STATION/SATELLITE EXCLUSION INTERVALLS
#
############################# end_of_header ##############################################

+cln_global
*-----------------------------------------------------------------------------------------
*CODE- ---MJDA---- ---MJDE---- -STA- SAT/SYS YYYY_DDD-LEN- ----COMMENT--->
*-----------------------------------------------------------------------------------------
*-----------------------------------------------------------------------------------------
*CODE- ---MJDA---- ---MJDE---- -STA- SAT/SYS YYYY_DDD-LEN- ----COMMENT--->
*-----------------------------------------------------------------------------------------
-cln_global
"""

if cln_global_reset:
    with open(cln_global_path,'w+') as f:
      f.write(CLN_GLOBAL)

if type(configfile_name) is str:
    configfile_list = [configfile_name]
    suffix_logname = '_' + configfile_name
elif type(configfile_name) is list:
    configfile_list = configfile_name
    suffix_logname = ''
else:
    print 'ERR : check configfile_name type !!! (str or list)'
    
now_str = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
log_path = os.path.join(logs_dir,'log_loop_run_' + now_str + suffix_logname + '.log'  )
LOGobj = open(log_path , 'w+')
print 'INFO : log of the loop in ' + log_path 


startday_dt = doy2dt(int(str(startday)[0:4]),int(str(startday)[4:7]))
endday_dt   = doy2dt(int(str(endday)[0:4]),int(str(endday)[4:7]))

day_range_dt = [startday_dt + dt.timedelta(n) for n in range(int((endday_dt - startday_dt).days))]
day_range = [str(d.year) + str(d.strftime('%j')) for d in day_range_dt]

#day_range = range(startday,endday+1) 
ITERLIST  = list(itertools.product(configfile_list , day_range ))

i_bunch = 0

print "****** JOBS THAT WILL BE LAUNCHED ******" 
print '*** from/to' , startday , endday 
print ITERLIST
print ''
print 'Number of jobs : ' + str(len(ITERLIST))
print "****************************************"
LOGobj.write(str(ITERLIST) + '\n')


def check_running(bj_check_user="psakicki",excludeC = True):
    bj_command = "perl /dsk/igs2/soft_wrk/psakicki/SOFT_EPOS8_BIN_TOOLS/SCRIPTS/e8_bjobs_local.pl"
    bj_list = subprocess.check_output(bj_command,shell='/bin/csh')
    bj_list_split = bj_list.split("\n")
    bj_pattern_checked = "  " + bj_check_user +  " " + bj_check_user
    bj_pattern_checked_C = "C" + bj_pattern_checked
    if excludeC:
        nb_jobs_running = np.sum([1 for l in bj_list_split if ((bj_pattern_checked in l) and (not bj_pattern_checked_C in l))])
    else:
        nb_jobs_running = np.sum([1 for l in bj_list_split if bj_pattern_checked in l])
        
    return nb_jobs_running , bj_list, bj_list_split




for config_name_iter , day  in ITERLIST:


    configfile_path = os.path.join(configfile_dir,config_name_iter)
    
    cfg_arg     = ' '.join(('-cfg',configfile_path))  
    
    beg_day_arg = ' '.join(('-beg_day',str(day)))
    
    if len(rod_list) == 0 or (len(rod_list) == 1 and rod_list[0] == ''):
        rod_arg = ''
    else:
        rods_as_str=','.join(rod_list)
        rod_arg = ' '.join(('-rod',rods_as_str))  
     
    if start_step == '':
        start_arg = ''
    else:
        start_arg = ' '.join(('-start',start_step))


    if stop_step == '':
        stop_arg = ''
    else:
        stop_arg = ' '.join(('-stop',stop_step))

    if task_only_step == '':
        task_only_arg = ''
    else:
        task_only_arg = ' '.join(('-stop',task_only_step))

    args_lis  = [cfg_arg,
                 beg_day_arg,
                 rod_arg,
                 start_arg,
                 stop_arg,
                 task_only_arg]
      
    if cluster_use:
        args_lis.insert(0,"cjob -c 'epos_start")
        args_lis.append(" '")
    else:
        args_lis.insert(0,"epos_start")
    
  
    kommand = ' '.join(args_lis)
  
    print kommand
    LOGobj.write(kommand + '\n')
  
    info_sleep = "INFO : script is sleeping for " +str(wait_sleeping_before_launch) +"sec (so you can cancel it) "
    print info_sleep
    LOGobj.write(info_sleep + '\n')
    time.sleep(wait_sleeping_before_launch) 
    info_start = "INFO : script starts @ " + str(dt.datetime.now())
    print info_start
    LOGobj.write(info_start + '\n')
    p = subprocess.Popen('',executable='/bin/csh', stdin=subprocess.PIPE , stdout=subprocess.PIPE , stderr=subprocess.PIPE)
    stdout,stderr = p.communicate( kommand )
    
    with open(history_file_path , "a") as myfile:
        myfile.write(kommand + '\n')

    if bj_check_on_off:    
        nb_jobs_running , bj_list, bj_list_split = check_running()
        while nb_jobs_running >= nb_jobs_max:          
            print "INFO : sleeping @ " + str(dt.datetime.now()) + " for " + str(bj_check_wait_time) + "s b.c. " + str(nb_jobs_running) + "job(s) run "
            print "********************************************************************************************************"
            print "*****************************      BATCH JOBs CURRENTLY RUNNING      ***********************************"
            print ""
            print bj_list
            print ""
            print "********************************************************************************************************"

            time.sleep(bj_check_wait_time)
            nb_jobs_running , bj_list, bj_list_split = check_running()

        print "INFO : let's continue,  " + str(nb_jobs_running) + "job(s) run (pause at " + str(nb_jobs_max) + ")"

    if wait_until_process_end:
        p.wait()
    else:
        time.sleep(wait_time)

