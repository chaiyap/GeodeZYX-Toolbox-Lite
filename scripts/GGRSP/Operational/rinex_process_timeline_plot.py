# -*- coding: utf-8 -*-
"""
Spyder Editor

Final name of rinex_timeline_GGRSP_beta_server
"""

#from megalib import *

import matplotlib
matplotlib.use('svg')

import re
import glob
import genefun
import matplotlib.pyplot as plt
import geodetik as geok
import geoclass as gcls
import datetime as dt
import os
import configparser
import ast
import sys,getopt


def main(argv):
    #### READING arguments
    help_str = argv[0] + ' -c <configfile_path>'
    try:
        opts, args = getopt.getopt(argv[1:],"hc:")
    except getopt.GetoptError:
        print(help_str)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_str)
            sys.exit()
        elif opt == "-c":
            configfile_path = arg

    config = configparser.ConfigParser()
    config.read(configfile_path)


    ### GENERAL 1 : Get the General name, date, and replace Alias
    gene_name  = config['General']['gene_name']

    ### Start and End limits
    if bool(config['General']['right_limit_today']):
        today = dt.datetime.now()
        rightdate = today
    else:
        rightdate = dt.datetime(*[int(e) for e  in config['General']['right_limit_manual'].split(",")])

    ddd ,yyyy = geok.dt2doy_year(rightdate)
    leftdate = rightdate - dt.timedelta(days=int(config['General']['days_back']))

    ## Replace Alias
    for sec_key    , sec_config in config.items():
        for subsec_key , subsec_val in sec_config.items(): #avoid subsec_val, it is not affected in case of multiple alias
            if "-GENE_NAME-" in sec_config[subsec_key]:
                sec_config[subsec_key] = sec_config[subsec_key].replace("-GENE_NAME-" , gene_name)
            if "-DDD-" in sec_config[subsec_key]:
                sec_config[subsec_key] = sec_config[subsec_key].replace("-DDD-" , str(ddd))
            if "-YYYY-" in sec_config[subsec_key]:
                sec_config[subsec_key] = sec_config[subsec_key].replace("-YYYY-" , str(yyyy))

    ### GENERAL 2
    time_plt_filename  = bool(config['Plot']['timestamp_in_plt_filename'])
    plot_export_prefix =      config['Plot']['plot_export_prefix'].replace(" ","_")
    plot_export_dir    =      config['Plot']['plot_export_dir'].replace(" ","_")
    genefun.create_dir(plot_export_dir)

    ### SINEX
    sinex_data_parent_dir = config['Sinex']['path']
    #snx_regex_pattern   = '[0-9]{4}_[0-9]{3}/OUT_PROD/[0-9]{4}_[0-9]{3}_prod.snx'
    #snx_regex_pattern   = '[0-9]{4}_[0-9]{3}_prod.snx'
    snx_regex_pattern     = config['Sinex']['snx_regex_pattern']

    snx_paths_list      = genefun.find_recursive(sinex_data_parent_dir , "*snx")
    snx_paths_good_list = [e for e in snx_paths_list if re.search(snx_regex_pattern , e)]
    #snx_paths_good_list = snx_paths_list
    snxdico             = gcls.stations_in_sinex_multi(snx_paths_list)

    ### RINEX
    datadico_list = []
    colordico     = dict()
    priority_ID_list  = []
    archive_name_list = []

    for RinexArchiveKey in config:
        if not "RinexArchive" in RinexArchiveKey:
            continue
        archive_parent_dir = config[RinexArchiveKey]['path']
        archive_name       = config[RinexArchiveKey]['name']

        archive_name_list.append(archive_name)

        # FIND RINEXs
        datadico = geok.rinex_timeline_datadico(archive_parent_dir,optional_info=archive_name)
        datadico_list.append(datadico)

        priority_ID_list.append(config[RinexArchiveKey]['priority'])

        # DEFINE COLOR
        colordico[archive_name] = config[RinexArchiveKey]['color']


    _ , archive_name_prio_list = genefun.sort_binom_list(priority_ID_list ,
                                                     archive_name_list) #USELESS
    _ , datadico_prio_list = genefun.sort_binom_list(priority_ID_list ,
                                                         datadico_list)

    #datadico_merged = geok.rinex_timeline_datadico_merge(datadico_prio_list,
    #                                                     archive_name_prio_list)

    datadico_merged = geok.rinex_timeline_datadico_merge(datadico_prio_list)


    ### PLOT
    fig = geok.timeline_plotter(datadico_merged,datadico_anex_list=[snxdico],
                                start=leftdate,
                                end  =rightdate,
                                colordico_for_main_datadico=colordico)

    ### SAVE FIG
    plt_out_path_list = []
    if time_plt_filename:
        timstp = '_' + genefun.get_timestamp()
    else:
        timstp = ""

    for plt_ext in config['Plot']['plot_export_type'].split(","):
        plt_out_path      = os.path.join(plot_export_dir , plot_export_prefix + timstp + '.' + plt_ext)
        fig.savefig(plt_out_path,bbox_inches='tight')
        plt_out_path_list.append(plt_out_path)

    ### SEND FIG BY MAIL
    if bool(config['Mail']['send_email']):
        plt_out_path_list_str = " ".join([" -a " + e for e in plt_out_path_list])
        send_cmd = " ".join(('echo "`date` / `whoami`@`hostname`" | mailx -s "' + config['Mail']['subject'] + '"' ,plt_out_path_list_str, config['Mail']['to']))

    print(send_cmd)
    os.system(send_cmd)

if __name__ == "__main__":
   main(sys.argv)
