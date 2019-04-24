# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:30:33 2015

@author: vballu
"""

from megalib import *
import matplotlib.pyplot as plt

listing_gins_folder = "/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/RESULTS_LPIL_GRG/"

station_info_path   = "/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/station.info.ulr6_withNC"
sinex_discont_path  = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/disc_IGS'
sinex_discont_path  = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/soln.snx'


#hector_neu_out_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/HECTOR_WORKING/NEUfiles'
hector_neu_out_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/HECTOR_WORKING/'

#raw_plots_out_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/HECTOR_WORKING/plots_bruts'
raw_plots_out_folder = '/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/HECTOR_WORKING/'


plt.ioff()

#for listing_gins_folder in glob.glob("/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/RESULTS_????_???"):
#for listing_gins_folder in glob.glob("/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/RESULTS_????_MIT"):
for listing_gins_folder in glob.glob("/home/vballu/gins_v2B/gin/PROJETS/NEWCAL/RESULTS_LPIL_GRG"):

    listing_gins_path = os.path.join(listing_gins_folder,'GINS_MAIN','*gins')
    
    listing_gins_list = glob.glob(listing_gins_path)
    
    timeseries = gcls.read_gins_multi_raw_listings(listing_gins_list)
    timeseries.anex['calc_center'] = os.path.basename(listing_gins_list[-1]).split('.yml')[0][-4:]
    
    if '_' in timeseries.anex['calc_center']:
        timeseries.anex['calc_center']  = 'grg2'
       
    
    timeseries.ENUcalc(timeseries.mean_posi())
    
    discont = gfc.read_station_info_time_solo(station_info_path,timeseries.stat)[0]
    discont = gfc.read_sinex_discontinuity_solo(sinex_discont_path,timeseries.stat)[0][1:]
    
    timeseries.set_discont(discont)
    
    timeseries = gcls.sigma_cleaner(timeseries,2,cleantype='any') 
    timeseries = gcls.mad_cleaner(timeseries,3,'dist')
    
    timeseries.plot('ENU')
    timeseries.plot_discont()
    f = plt.gcf()
    f.set_size_inches(16.53,11.69)
    
    prefix = timeseries.stat + '_' + timeseries.anex['calc_center'] 
    plt.savefig(os.path.join(raw_plots_out_folder,prefix + '.png'))
    
    plt.close()
    
    gcls.export_ts_as_neu(timeseries,hector_neu_out_folder,prefix)

