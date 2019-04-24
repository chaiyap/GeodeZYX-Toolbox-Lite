#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:27:12 2017

@author: psakicki
"""


import matplotlib
matplotlib.use('agg')

import softs_runner
import genefun
import geodetik as geok
import datetime as dt
import re

main_dir           = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/OVSG_webobs'
main_dir           = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/OVSG_volobsis'
main_dir           = '/media/psakicki/a8536b8c-a646-4329-891f-a2deffb63e08/OLD2/GWADA/RINX2/ORPHEON'
main_dir           = '/media/psakicki/a8536b8c-a646-4329-891f-a2deffb63e08/OLD2/GWADA/RINX2/IGS'
main_dir           = '/media/psakicki/a8536b8c-a646-4329-891f-a2deffb63e08/OLD2/GWADA/RINX2/OVSG_OVSM'
main_dir           = '/home/psakicki/Téléchargements/MQ/'
main_dir           = '/home/psakicki/Téléchargements/GL/'
main_dir           = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/RINEX/1702_RINEX_GWA2A_REBOOT/tmp_IPGP/"
main_dir           = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/IPGP/MERGE" 

parent_archive_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/ORPHEON'
parent_archive_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/IGS'
parent_archive_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/OVSGM'
parent_archive_dir = '/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/RINEX/1702_RINEX_GWA2A_REBOOT/IPGP'
parent_archive_dir = "/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/GWA2A2018/RINEX/IPGP"

# Find the rinex
if 1:
    rinex_lis = softs_runner.multi_finder_rinex(main_dir,
                                                rinex_types=('o','d','d.Z','d.z'))
    # Move/Copy the rinex
    move = False
    softs_runner.multi_archiver_rinex(rinex_lis,parent_archive_dir,
                                      archtype='stat/year',move=move,
                                      force_mv_or_cp=True)

# plot the timeline

timeline_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/OVSGM'
timeline_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/'
timeline_dir = '/home/psakicki/THESE/DATA/1702_RINEX_GWA2A_REBOOT/ORPHEON'
timeline_dir = '/dsk/ggsp_pf/PLAYGROUND/psakicki/GWA2A2018/RINEX/1702_RINEX_GWA2A_REBOOT'

if 0:
    rinex_lis_for_timeline = softs_runner.multi_finder_rinex(timeline_dir,
                                                rinex_types=('o','d','d.Z','d.z'))
    geok.rinex_timeline(rinex_lis_for_timeline,use_rinex_lister = False)



