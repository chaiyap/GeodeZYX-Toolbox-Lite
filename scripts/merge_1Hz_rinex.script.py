# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:28:46 2015

@author: psakicki
"""

import softs_runner
import glob , itertools , os ,re
import geodetik as geok
import datetime as dt
import subprocess
import genefun as gf

#path = '/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/1sec/nica/*'
#outdir = os.path.dirname(path)

path   = '/home/psakicki/THESE/DATA/1604_BOUEES/AIX/IPGB/*Z'
path   = '/home/psakicki/THESE/DATA/1604_BOUEES/AIX/UMRB/*Z'
path   = '/home/psakicki/Téléchargements/lroc/*Z'

path   = '/home/psakicki/Téléchargements/lroc/*Z'

path = "/home/psakicki/Téléchargements/transfer_397074_files_6ca51ea5/IGNTEST_1sec/smne/2017/*Z"


outdir = gf.create_dir(os.path.join(os.path.dirname(path),'MERGED'))

filis = glob.glob(path)

rinexlis = [ f for f in filis if re.match(softs_runner.rinex_regex(1),os.path.basename(f)) ]

datelis = []
statlis = []

operarnxlis       = []
umcomp_rnx_to_del_lis = []

for rnx in rinexlis:
    datelis.append(geok.rinexname2dt(os.path.basename(rnx)).date())
    statlis.append(os.path.basename(rnx)[0:4])
    
    if softs_runner.check_if_compressed_rinex(rnx):
        rnx_uncompress = softs_runner.crz2rnx(rnx)
        operarnxlis.append(rnx_uncompress)
        umcomp_rnx_to_del_lis = []
        
    else:
        operarnxlis.append(rnx)

operarnxlis = list(set(operarnxlis))
    
datelis = list(set(datelis))
statlis = list(set(statlis))

for stat , dat in itertools.product(statlis , datelis):
    rinexs_of_the_date_lis = []
    for rnx in operarnxlis:
        rnxnam = os.path.basename(rnx)
        if rnxnam[0:4] == stat and dat == geok.rinexname2dt(rnxnam).date():
            rinexs_of_the_date_lis.append(rnx)
        

    rinex_out_name = geok.statname_dt2rinexname(stat,dt.datetime.combine(dat, dt.time()),'o')

    p = subprocess.Popen('',executable='/bin/bash', stdin=subprocess.PIPE , stdout=subprocess.PIPE , stderr=subprocess.PIPE)
    
    command = 'teqc ' +  ' '.join(sorted(rinexs_of_the_date_lis)) + ' > ' + os.path.join(outdir,rinex_out_name)
    
    print(command)

    err_log_name = os.path.join(outdir , rinex_out_name + ".err.log")
    print(rinex_out_name)
    
    stdout,stderr = p.communicate( command )
    std_file = open(rinex_out_name, "w")
    std_file.write(stdout) 
    std_file.close()
    if stderr != '':
        print(err_log_name + " is not empty, must be checked !")     
        print(stderr)
        err_file = open(err_log_name, "w")
        err_file.write(stderr)
        err_file.close()        
        

[ os.remove(e) for e in umcomp_rnx_to_del_lis ]
