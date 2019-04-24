# -*- coding: utf-8 -*-
import softs_runner
import datetime as dt

# STATDICO 
# a statdico is a dictionary associating Archives Centers to list of stations 
# EX :
# statdico['archive center 1'] = ['STA1','STA2','STA3', ...]
# statdico['archive center 2'] = ['STA2','STA1','STA4', ...]

# EXEMPLEs
#statdico['igs'] = ['scub' , 'guat' , 'ssia' , 'slor' , 'mana' , 'cro1']
#statdico['rgp'] = []
#statdico['ovsg'] = ['abd0']
#statdico['unavco'] = ['CN40' , 'CN19' , 'CN38' , 'SAN0' , 'CN35' , 'ROA0' , 'CN29' , 'CN18' , 'CBMD' , 'LCSB' , 'GCFS' , 'GCEA' , 'CN10' , 'CN12' , 'PRCG' , 'SMRT' , 'BARA']
#statdico['igs'] = ['scub' , 'guat' , 'ssia' , 'slor' , 'mana' , 'cro1']
#statdico['igs'] = ['SFER','WARN','GANP','UZHL','PTBB','TITZ','FFMJ','WSRT','KOSG','DLFT']

# if you want you can download the same stat. in several servers (assuming is the same data)
#statdico['igs'] = ['TLSE']
#statdico['rgp'] = ['TLSE']
#statdico['renag'] = ['TLSE']

#statdico['igs'] = ['LROC']
#statdico['rgp'] = ['LROC']
#statdico['renag'] = ['LROC']

# ========= END OF EXEMPLES =========

statdico = dict()
#statdico['rgp'] = ['EZEV','NICA']
#statdico['rgp'] = ['BSCN']
#statdico['rgp_1Hz'] = ['MLVL']
#statdico['rgp_1Hz'] = ['ANGL','AUNI','CHIZ','ILDX','LROC','ROYA']
#statdico['rgp_1Hz'] = ['SMNE']


#statdico['renag'] = ['MARI']
#statdico['renag'] = ['ABER','DESI','LORI','MARI','BOUL','GOSI','MAGA','TRIL']
#statdico['ovsg']    = ['ABD0','ADE0','ASF0','BDOS','CBE0','DDU0','DED0','DHS0','DSD0','FFE0','FNA0','FSDC','GDB0','HOUE','LAM0','MGL0','MPCH','PDB0','PSA1','SEG0','SOUF','TDB0']



#statdico['igs'] = ['KOUC','PTVL']
#statdico['igs'] = ['NRMD']

#statdico['nav'] = ['BRDC']


#POUR LA GWADA
statdico['orpheon'] = ['ABER','DESI','LORI','MARI','BOUL','GOSI','MAGA','TRIL']
#statdico['ovsg']    = ['ABD0','ADE0','ASF0','BDOS','CBE0','DDU0','DED0','DHS0','DSD0','FFE0','FNA0','FSDC','GDB0','HOUE','LAM0','MGL0','MPCH','PDB0','PSA1','SEG0','SOUF','TDB0']
#statdico['rgp']      = ['ABMF',"LMMF","FFT2","PPTG"]


#Pour le test
#statdico['rgp_1Hz'] = ['TLSE','SMNE']
#statdico['igs']     = ['ZIMM']

# START & END DATES OF DATA TO DOWNLOAD
s,e = softs_runner.start_end_date_easy(2000,1,2015,150)
s,e = softs_runner.start_end_date_easy(2006,1,2006,5)
s,e = softs_runner.start_end_date_easy(2015,167,2015,174)
s,e = softs_runner.start_end_date_easy(2009,1,2009,50)
s,e = softs_runner.start_end_date_easy(2015,249,2015,251)
s,e = softs_runner.start_end_date_easy(2015,167,2015,174)
s,e = softs_runner.start_end_date_easy(2015,300,2015,301)
s,e = softs_runner.start_end_date_easy(2015,249,2015,251)
s,e = dt.datetime(2015,4,28) , dt.datetime(2015,4,28)
s,e = dt.datetime(2016,2,1) , dt.datetime(2017,3,14)
s,e = dt.datetime(2015,1,1) , dt.datetime(2017,3,14)
s,e = dt.datetime(2014,10,1) , dt.datetime(2017,3,14)
s,e = dt.datetime(2014,1,1) , dt.datetime(2014,1,5)
s,e = dt.datetime(2016,4,1) , dt.datetime(2016,4,5)
s,e = dt.datetime(2016,8,1) , dt.datetime(2016,8,5)
s,e = dt.datetime(2016,12,1) , dt.datetime(2016,12,5)
s,e = dt.datetime(2016,1,1) , dt.datetime(2016,12,31)
s,e = softs_runner.start_end_date_easy(2014,1,2014,365)
s,e = softs_runner.start_end_date_easy(2007,1,2018,329)
s,e = softs_runner.start_end_date_easy(2015,1,2018,329)
s,e = softs_runner.start_end_date_easy(2018,310,2018,329)
s,e = softs_runner.start_end_date_easy(2014,360,2016,50)

s,e = softs_runner.start_end_date_easy(2014,100,2014,250)
s,e = softs_runner.start_end_date_easy(2013,1,2018,328)
s,e = softs_runner.start_end_date_easy(2016,300,2017,50)
s,e = softs_runner.start_end_date_easy(2014,340,2017,352)
s,e = softs_runner.start_end_date_easy(2014,340,2017,352)
s,e = softs_runner.start_end_date_easy(2013,167,2013,176)
s,e = softs_runner.start_end_date_easy(2016,193,2016,200)
s,e = softs_runner.start_end_date_easy(2018,19,2018,50)



# PLACE OF THE ARCHIVE WHERE THE RINEX WILL BE SAVED
archive_dir = '/home/pierre/Documents/geodezyx_toolbox/scripts/archiverinex'
archive_dir ='/home/psakicki/ARCHIVEAnnexe/IGSJURAmk4'
archive_dir ='/home/psakicki/ARCHIVEAnnexe/IGSJURAmk4'
archive_dir ='/home/vballu/archiv_POUR8TEST/'
archive_dir ='/home/vballu/DATA/GNSS/VANUATU/GPS_STATIC/'
archive_dir ='/home/psakicki/aaa_FOURBI/TLSE2002'
archive_dir ='/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE'
archive_dir ='/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE'
archive_dir ='/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL'
archive_dir ="/home/psakicki/THESE/DATA/1506_GEODESEA/GNSS_ONSHORE/nica/1sec"

archive_dir = "/home/psakicki/THESE/DATA/1509_TOIT_DPTS/MLVL/mlvl/1Hz"
archive_dir = "/home/psakicki/Téléchargements"

archive_dir = "/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/OVSG/"
archive_dir = "/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/IGNTEST/"
archive_dir = "/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/ORPHEON/"

archive_dir = "/home/psakicki/THESE/DATA/1706_RNX_VANU/ORBITS"

archive_dir = "/home/adminuser/Téléchargements"

archive_dir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/RINEX/1702_RINEX_GWA2A_REBOOT/ORPHEON"
archive_dir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/RINEX/1702_RINEX_GWA2A_REBOOT/RGP"

archive_dir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/RGP"
archive_dir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/RENAG_ORPHEON"
archive_dir = "/wrk/sakic_xchg/GWA2A2018/RINEX/RINEX/GOOD/RENAG_ORPHEON/"

#archive_dir = "/home/psakicki/Téléchargements/transfer_397074_files_6ca51ea5/IGNTEST_1sec"


# ARCHTYPE : structure of the archive like
#archtype ='stat/year/doy'
#archtype ='stat'
#archtype ='week/dow/stat'
archtype ='stat/year'

parallel_download=1

user   = 'pierres'
passwd = 'ps7563'

user   = 'orph30ssakic'
passwd = 'orpheon&sakic!'

if 1:
    url_list = softs_runner.multi_downloader_rinex(statdico,archive_dir,s,e,archtype,
                                                   parallel_download,sorted_mode=0,
                                                   user=user,passwd=passwd)
    
    









# ================= ORBITS ==============================
if 0:
    orblis = softs_runner.multi_downloader_orbs_clks( archive_dir , s , e ,
                                                     archtype='/',
                                                     calc_center = 'igs')
                                               

