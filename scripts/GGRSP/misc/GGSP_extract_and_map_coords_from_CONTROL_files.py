#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:27:44 2018

@author: psakicki
"""

from megalib import *

path_sta_sel = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/Map_Stats/sta_selection_uncommented"
path_coords  = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/Map_Stats/sta_coordinates" 
path_coords  = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/Map_Stats/sta_coordinates_save" 
patterntup = ["MGEX","GESS","GSS","00000:00000  [A-Z0-9]{4}$"]
typtup     = ["MGEX","GESS","GSS","IGS"]

outdir = "/home/psakicki/GFZ_WORK/RENDU/1801_EGU_Vienne/Posters/GGSP_PF_CFORB/Plots/Map"
outplt = os.path.join(outdir, "Map_GGSP_Stations")


fail_cont = 0

outdic = dict()

for typ , pattern in zip(typtup ,patterntup):
    llist = gf.grep(path_sta_sel,pattern,regex=True)
    print(typ)
    
    outdic[typ] = []
    
    for l in llist:
        lsplit = l.split()
        
        stat_numID  = int(lsplit[0])
        stat_charID = (lsplit[5])
        
        coords_line =gf.grep(path_coords,
                             "POS_VEL:XYZ     m " +lsplit[0],
                             only_first_occur=True)
        
        if not coords_line:
            fail_cont += 1
            continue
        
        c_splt = coords_line.split()
        
        C = [float(e) for e in c_splt[4:7]]
        
        outlin = [stat_charID , stat_numID] + list(geok.XYZ2GEO(*C))
        
        outdic[typ].append(outlin)

outdic_export_dir  = "/home/psakicki/aaa_FOURBI/"
outdic_export_name = "GGSP_stat_typ_dic"

gf.pickle_saver(outdic , outdic_export_dir , outdic_export_name )

coldic = dict()
symdic = dict()

typtup     = ["IGS"  , "MGEX","GESS"    ,"GSS"]
coltup     = ["blue" , "green"  , "#984ea3" , "orange"] 
symtup     = ["^" , "v" , "<" , ">"] 

for typ , col ,sym in zip(typtup,coltup,symtup):
    coldic[typ] = col 
    symdic[typ] = sym 

if 1:
    
    plter_name = "cartopy"

    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import matplotlib.patches as mpatches
    
    import matplotlib.lines as mlines
    
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
    ax.set_global()
    
    #ax.stock_img()
    ax.coastlines()
    
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.BORDERS, linestyle=':' , edgecolor='gray' )
    
    gl = ax.gridlines(draw_labels=0,linewidth=1,color="k")
        
    legend_list = []
    for typ  in typtup:
        typvals = outdic[typ]
        DF = pd.DataFrame(outdic[typ])
        for _,df in DF.iterrows():
            symbol_ploted  = ax.scatter(df[3] , df[2] , color=coldic[typ], marker=symdic[typ],
                    transform=ccrs.PlateCarree(),label=typ,s=125)
        legend_list.append(symbol_ploted)

            
    # make two proxy artists to add to a legend
    direct_hit = mpatches.Rectangle((0, 0), 1, 1, facecolor="red")
    within_2_deg = mpatches.Rectangle((0, 0), 1, 1, facecolor="#FF7E00")
                                      

#    #### LEGEND
#        import matplotlib.lines as mlines
#        for arcnam , col in colordico_for_main_datadico.items():
#            legend_list.append(mlines.Line2D([], [], color=col,
#                                                     label=arcnam))
    legend = ax.legend(handles=legend_list,loc='lower left',markerscale=1.5)

    frame = legend.get_frame()
    frame.set_facecolor('ivory')
    frame.set_alpha(1)
                                      
#    symbols = symtup
#    labels = typ
#    ax.legend(symbols, labels,
#              loc='lower left', bbox_to_anchor=(0.025, -0.1), fancybox=True)
#            
            
else:
    
    plter_name = "basemap"
    
    from mpl_toolkits.basemap import Basemap

    projection='robin'
    figsize=(10, 7)
    resolution='c'
    fig, ax = plt.subplots(figsize=figsize)
    m = Basemap(projection=projection, resolution=resolution,
                lon_0=0, ax=ax)
    m.drawcoastlines()
    m.fillcontinents(color='0.85')
    m.drawmapboundary(fill_color='aqua')

    parallels = np.arange(-60, 90, 30.)
    meridians = np.arange(-360, 360, 60.)
    m.drawparallels(parallels, labels=[0, 1, 0, 0])
    m.drawmeridians(meridians, labels=[0, 0, 1, 0])

    for typ  , typvals in outdic.items():
        DF = pd.DataFrame(outdic[typ])
        for _,df in DF.iterrows():
            #ax.plot(df[3] , df[2] , color=coldic[typ], marker='o',
            #       transform=ccrs.PlateCarree())
            ax.plot(*m(df[3] , df[2]), color=coldic[typ], marker='o')

fig.patch.set_alpha(0)

outplt = os.path.join(outdir, "Map_GGSP_Stations_" + plter_name)

for ext in (".svg" , ".png" , ".pdf"):
    plt.savefig(outplt + ext,bbox_inches='tight')    

   
    
        