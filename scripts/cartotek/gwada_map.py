# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 13:57:37 2015

@author: psakicki
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


m = Basemap(width=140000,height=100000,projection='lcc',
            resolution='l',lat_1=10.,lat_2=20,lat_0=16.2,lon_0=-61.5)
m.drawcoastlines()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='tan',lake_color='aqua')
# labels = [left,right,top,bottom]
parallels = np.arange(0.,20.,0.5)
m.drawparallels(parallels,labels=[False,True,True,False])
meridians = np.arange(-70.,-60.,0.5)
m.drawmeridians(meridians,labels=[True,False,False,True])

filelist = ['/home/psakicki/gin/TP/GWADA/gps_continu.csv',
            '/home/psakicki/gin/TP/GWADA/gps_repet.csv']

good_stat = ['ABMF','ADE0','ASF0','CBE0','DHS0','DSD0','FNA0','FSDC','HOUE','LAM0','MGL0','PDB0','PSA1','SOUF','TDB0','FFE0']
good_startrest = list(good_stat)
delta_dic = {}
delta_dic['TDB0'] = [0,-4500]
delta_dic['DSD0'] = [500,-5000]
delta_dic['ADE0'] = [0,-6500]
delta_dic['SOUF & \n PSA1'] = [-15000,-4000]


col = ['b','r']
legendlabel = ['permanent','repetition']


for i,fil in enumerate(filelist):
    data = pd.read_csv(open(fil))
    
    alias_lis_raw = list(data['Alias'])
    lon_lis_raw = list(data['Lon. (WGS84)'])
    lat_lis_raw = list(data['Lat. (WGS84)'])
    alias, lat, lon = [] , [] , []
    
    for a , lo , la in zip(alias_lis_raw,lon_lis_raw,lat_lis_raw):
        coluniq = col[i]
        if not a in good_stat:
            print 'not ' + str(a)
            continue
        if a == 'TDB0' and i == 0:
            continue
        if a == 'PSA1' and i == 1:
            continue
        if a == 'PSA1' and i == 0:
            continue      
        if a == 'SOUF' and i == 0:
            a = 'SOUF & \n PSA1'
        lon.append(float(lo))
        lat.append(float(la))
        alias.append(a)
        try:
            good_startrest.remove(a)
        except:
            pass
              
    x,y = m(lon,lat)
    m.plot(x, y, 'bo', markersize=10,color = coluniq ,label =legendlabel[i])
    for a , xp,yp in zip(alias,x,y):
        if a in delta_dic.keys():
            dx = delta_dic[a][0]
            dy = delta_dic[a][1]
            print 'in'
        else:
            dx = 0
            dy = 0
        print dx,dy
        plt.text(xp + 1500 + dx ,yp + 1500 + dy,a)
    #m.shadedrelief()
    plt.title('Guadeloupe GNSS network processed with GINS')
    plt.legend()
    plt.show()
    


    
