# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:50:10 2015

@author: psakicki

LE PROBLEME DE GINS EN KINE C'EST QU'IL 
DONNE LA POSITION RELATIVE
A LA POSITION A PRIORI
IL FAUT DONC L'AJOUTER EN MANU 
"""

from megalib import *


fillis = ["/home/psakicki/gin/batch/listing/SX_xxxxxxxxxxxxxxxxxxxxx.gsea4",
"/home/psakicki/gin/batch/listing/SY_xxxxxxxxxxxxxxxxxxxxx.gsea4",
"/home/psakicki/gin/batch/listing/SZ_xxxxxxxxxxxxxxxxxxxxx.gsea4"]


ts = gcls.read_gins_multi_extracted(fillis)
ts2 = gcls.sigma_cleaner(ts)

ts2.plot('XYZ')

aaa = gcls.export_ts(ts2,'/home/psakicki/aaa_FOURBI','XYZ')


# Si on a fait la bêtise d'exporter les SXE et pas les SX
# Inutile normalement

if 0:
    fillis = ["/home/psakicki/gin/batch/listing/SXExxxxxxxxxxxxxxxxxxxxx.gsea1",
    "/home/psakicki/gin/batch/listing/SYExxxxxxxxxxxxxxxxxxxxx.gsea1",
    "/home/psakicki/gin/batch/listing/SZExxxxxxxxxxxxxxxxxxxxx.gsea1"]
    
    ts = gcls.read_gins_multi_extracted(fillis)
    
    coords = [[4595402.413,630644.646,4363209.073],
    [4595402.877 ,  630645.271 , 4363208.228]]
    window = [geok.doy2dt(2015,172)]
    
    ts4 = gcls.add_offset_smart_for_GINS_kine(ts,coords,window)
    ts5 = gcls.sigma_cleaner(ts4)
    
    aaa = gcls.export_ts(ts5,'/home/psakicki/aaa_FOURBI','XYZ')
