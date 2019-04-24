# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from megalib import *
import matplotlib.pyplot as plt
import geodetik as geok


sinex_data_parent_dir= '/home/psakicki/aaa_FOURBI/TMP_SNX/*snx'
rinex_data_parent_dir='/home/psakicki/aaa_FOURBI/data/'
rinex_data_parent_dir2='/home/psakicki/aaa_FOURBI/data2/'

plot_export_dir    = '/home/psakicki/aaa_FOURBI/'
plot_export_prefix = 'stat_monitoring'

snx_regex_pattern   = '[0-9]{4}_[0-9]{3}/OUT_PROD/[0-9]{4}_[0-9]{3}_prod.snx'
snx_paths_list      = glob.glob(sinex_data_parent_dir)
snx_paths_good_list = [e for e in snx_paths_list if re.search(snx_regex_pattern , e)]

### SINEX
snx_paths_list = glob.glob(sinex_data_parent_dir)
snxdico        = gcls.stations_in_sinex_multi(snx_paths_list)

### RINEX
datadico1  = geok.rinex_timeline_datadico(rinex_data_parent_dir,optional_info='DATA')
datadico2 = geok.rinex_timeline_datadico(rinex_data_parent_dir2,optional_info='DATA2')


#def rinex_timeline_datadico_merge(datadico_list):

datadico_list = [datadico2,datadico1]
priority_list = ['DATA','DATA2']
datadico_out  = dict()


def rinex_timeline_datadico_merge(datadico_list,priority_list):
    """
    Merge different RINEXs datadico, produced by rinex_timeline_datadico
    coming from different archives
    Args :
        rinex_timeline_datadico : list of RINEX datadico
        priority_list : priority list of 'optional_info' (archive ID)
                        it will erase optional_info of lower priority
    Returns :
        datadico_out : a merged datadico
    """

    datadico_merged = genefun.dicts_of_list_merge(*datadico_list)

    for k , dataval in datadico_merged.items():

        rnxname_list = [e[0]  for e in dataval]
        archive_list = [e[1]  for e in dataval]
        date_list    = [e[-1] for e in dataval]

        out_date_list , out_all_list = [] , [] 
        for r,a,d in zip(rnxname_list,archive_list,date_list):
            if d not in out_date_list:
                out_date_list.append(d)
                out_all_list.append((r,a,d))
            else:
                ind_existing   = out_date_list.index(d)
                archd_existing = out_all_list[ind_existing][1]
                if priority_list.index(a) < priority_list.index(archd_existing):
                    out_date_list.remove(d)
                    out_all_list.remove(out_all_list[ind_existing])
                    out_date_list.append(d)
                    out_all_list.append((r,a,d))                
    
        datadico_out[k] = out_all_list
        
    return datadico_out

datadico=rinex_timeline_datadico_merge(datadico_list,priority_list)


### DEFINE COLOR
colordico          = dict()
colordico['DATA']  = 'b' 
colordico['DATA2'] = 'r'

### PLOT
fig = geok.timeline_plotter(datadico,datadico_anex_list=[snxdico],
                            start=dt.datetime(2017,12,1), 
                            end  =dt.datetime(2099,1,1))

#                            colordico_for_main_datadico=colordico)
fig.savefig(plot_export_dir + plot_export_prefix + '_' + genefun.get_timestamp() + '.png',
            bbox_inches='tight')