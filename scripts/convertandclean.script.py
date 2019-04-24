# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:55:45 2015

@author: psakicki

Script réadapté pour le preprocess de l'eq file 
de JuraMk4 le 15 juillet 2015
"""

import os
import glob
import geoclass as gcls
import geo_files_converter_lib as gfc
import matplotlib.pyplot as plt
from megalib import  *
reload(gcls)


# PATHS ENTREE/SORTIE
#input_dir  = '/home/mrabin/Documents/timeseries_jura_pos/*pos'
#output_dir = '/home/mrabin/Documents/timeseries_jura_neu/'
#output_prefix = 'jura3b'

input_dir  = '/home/pierre/Documents/1507_JURAmk4/POSfiles/*pos'
output_dir = '/home/pierre/Documents/1507_JURAmk4/PREPROCESSING'
output_prefix = 'jura4_allstats'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

station_info_path='/home/mrabin/Documents/station.info.light'
station_info_path='/home/pierre/Documents/1507_JURAmk4/POSfiles/stationinfo/station.info'
eqfile_path='/home/pierre/Documents/1507_JURAmk4/POSfiles/stationinfo/station.jura4.work.eq'
eqfile_path="/home/pierre/Documents/1507_JURAmk4/POSfiles/stationinfo/noigs.jura.work.eq"
eqfile_path="/home/pierre/Documents/1507_JURAmk4/POSfiles/stationinfo/igsnoigs.jura.work.eq"


#On converti le stat info en eqfile (optionnel)
if 0:
    gfc.convert_statinfo2eqfile(station_info_path,eqfile_path)
  
# On restructure un eq file qui a seriv de base a une detection des offsets manuels  (optionnel)
if 0: 
    inpeq = '/home/pierre/Documents/1507_JURAmk4/POSfiles/stationinfo/noigs.jura.workmodif.eq'    
    direq = os.path.dirname(inpeq)
    outeq = 'noigs.jura.workmodif.restructured.eq'
    
    eqdico = gfc.read_eqfile_as_dico(inpeq)
    gfc.write_eqfile_from_dico(eqdico,direq,outeq)

if 1:
    for fil in glob.glob(input_dir):
        disc = []
        
        # import des données    
        ts = gcls.read_pbo_pos(fil) 
    
        # cas special ou on elimine la station si elle st pas dans le fichier de discont
        if 1:
            if not genefun.grep_boolean(eqfile_path,ts.stat):
                print(ts.stat , ' not in the discont file')

            else:
                print(ts.stat , 'in the discont')
    
                # nettoyage des offsets
                if 1:
                    ts = gcls.mad_cleaner(ts,seuil=3.5,coortype='ENU')
                if 1:
                    ts = gcls.sigma_cleaner(ts,seuil=3,coortype='ENU') 
            
                # supression du trend
                if 1:
                    ts = gcls.detrend_ts(ts,coortype='ENU')
            
                #gestion des disconts/offsets
                # ICI 2 CHOIX : LIRE STATION INFO OU BIEN EQFILE
                # le cas idéal : on a un eqfile
                # mais le cas le plus courant, on utilise le station info pour avoir les discontinuités 
                if 1:
                    disc = gfc.read_eqfile_time_solo(eqfile_path,ts.stat)[0]
                if 0:
                    disc = gfc.read_station_info_time_solo(station_info_path,ts.stat)[0]
                ts.set_discont(disc)  
    
        # plot et export des plots
        if 1:
            plt.ioff()
            ts.plot_discont(1)
            ts.plot(fig=1)
            
          
    
        for i in range(1):
            f = plt.figure(i+1)
            f.set_size_inches(16.53,11.69) 
            for a in f.axes[1:]:
                labels = a.get_xticklabels()
                for l in labels:
                    l.set_rotation(40)
                    l.set_horizontalalignment('right')
            figpath = os.path.join(output_dir , output_prefix + '_' + ts.stat +'_' + str(i) + '.png')   
            f.savefig(figpath,papertype='a4',format='png')
    
            plt.clf()    
            plt.close('all')  
    
        gcls.export_ts_as_neu(ts,output_dir,output_prefix)
