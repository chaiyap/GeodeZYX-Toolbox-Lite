# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:35:45 2015

@author: vballu
"""

from megalib import *
import matplotlib.pyplot as plt

working_dir = "/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/NASA_JPL_timeseries/"
station_info_path = "/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/station.info.ulr6_withNC"
sinex_discont_path  = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/disc_IGS'

raw_plots_out_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/HECTOR_WORKING/plots_bruts'

hector_neu_out_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/HECTOR_WORKING/NEUfiles'

filis = glob.glob(working_dir + '/????.???')
statlis = list(set([os.path.basename(f)[0:4] for f in filis]))

tsjpl_lis = []

for stat in statlis:
    latlonrad_files_list = glob.glob(working_dir + '/' + stat + '.***' )
    tsjpl = gcls.read_jpl_timeseries_solo(latlonrad_files_list)
    tsjpl_lis.append(tsjpl_lis)
        
    discont = gfc.read_station_info_time_solo(station_info_path,tsjpl.stat)[0]
    discont = gfc.read_sinex_discontinuity_solo(sinex_discont_path,tsjpl.stat)[0][1:]
    
    tsjpl.set_discont(discont)
    
    tsjpl = gcls.sigma_cleaner(tsjpl,2,cleantype='any') 
    tsjpl = gcls.mad_cleaner(tsjpl,3,'dist')
    
    tsjpl.plot('ENU')
    tsjpl.plot_discont()
    f = plt.gcf()
    f.set_size_inches(16.53,11.69)
    
    prefix = 'tsJPL_' + tsjpl.stat + '_' 
    plt.savefig(os.path.join(raw_plots_out_folder,prefix + '.png'))

    gcls.export_ts_as_neu(tsjpl,hector_neu_out_folder,prefix)


