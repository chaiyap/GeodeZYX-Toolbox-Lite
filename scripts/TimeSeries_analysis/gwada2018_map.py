#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:38:46 2019

@author: psakicki
"""

from megalib import *
import velo_field_map_plt as vfmp


################' GENERAL PARAMETERS ########################'

plot_vertical   = True
clean_outliers  = True
no_incertitudes = False
plot_hi_res     = True
software = "GINS"
software = "EPOS"


################' DATA PARAMETERS ########################'

main_path = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1811_Repro_Gwada_18/01_Syncro_Server_TPX1/GNSS_RESULTS/"

if   software == "GINS":
    soft_path = main_path + "/GINS/01_GFZorbs/"
elif software == "EPOS":
    soft_path = main_path + "/EPOS/OK_mk2_good/"
    

p             = soft_path + "/04a_HECTOR_WORK/vel_output/trend_output_halfyear_DataFrame.pik"
export_dir    = soft_path + "/05_Exports_Maps"
gf.create_dir(export_dir)


################' PLOT PARAMETERS ################'
GEBCO=0

hw=5000 #largeur fleche
#posl=[25215.4,38689.2]

# DEZOOM
scale_arrow=10000000
scale_arrow=15000000
scale_arrow=10000000


scale_arrow=15000000
scale_ellipse=5000000


# General : GUA+MAR+SBA
latm=14 #latitude minimum
latM=19 # latitude maximum

lonm=360-64 # longitude minimum
lonM=360-60 #longitude maximum

# Gouadeloupe only
latm=15.4 # latitude minimum
latM=16.8 # latitude maximum
lonm=360-62 # longitude minimum
lonM=360-60.8 #longitude maximum

### LEGEND
legend_arrow_length = ( "1 mm/yr",0.001)
legend_ellipse_size = ( "1 mm/yr",0.001)


path = ""
title_midfix_plate = "ITRF2014"
source_run = ""
pole_used  = ""

############################# LOADING ###################################

DForig = gf.pickle_loader(p)    
DF     = DForig.copy()

if software == "EPOS":
  DF["Longitude"] = 360 - np.abs(DF["Longitude"])



if clean_outliers:
    DF = DF[DF["V_North"] < 0.05]
    DF = DF[DF["V_East"]  < 0.05]
    DF = DF[DF["V_Up"]    < 0.05]

DF.reset_index()

pos_ref_select = np.column_stack((DF["Latitude"],DF["Longitude"]))

lat_ref   = np.array(DF["Latitude"])
long_ref  = np.array(DF["Longitude"])

vn_ref    = np.array(DF["V_North"])
ve_ref    = np.array(DF["V_East"])
vu_ref    = np.array(DF["V_Up"])

vne = np.column_stack((vn_ref , ve_ref))

if not no_incertitudes:
    incvn_ref = np.array(DF["sV_North"])
    incve_ref = np.array(DF["sV_East"])
    incvu_ref = np.array(DF["sV_Up"])
else:
    incvn_ref = None
    incve_ref = None
    incvu_ref = None

Stations = np.array(DF["Station"])

#############################' PLOT ###################################''

station_etude = Stations
nstation = len(Stations)
        
if plot_vertical:
    legend_position=(0.5,0.08)
    
else:
    legend_position=(0.5,0.9)

fig , ax , m = vfmp.draw_map(station_etude,latm,latM,lonm,lonM,path,
         pos_ref_select,hw,vne[:,0],vne[:,1],vu_ref,
         incvn_ref,incve_ref,incvu_ref,plot_GEBCO=False,
         plot_vertical=plot_vertical,
         plot_ellipses=True,plot_topo=plot_hi_res,
         coarse_lines=(not plot_hi_res),
         legend_position=legend_position,
         scale_arrow=scale_arrow,
         scale_ellipse=scale_ellipse,
         legend_arrow_length=legend_arrow_length,
         legend_ellipse_size=legend_ellipse_size)

#### FINITIONS                    
if not plot_vertical:
    HV_mark = "H"
    title_prefix = "Horizontal"
else:
    HV_mark = "V"
    title_prefix = "Vertical"

path_pb = "/home/psakicki/GFZ_WORK/PROJECTS_OTHERS/1806_Jordan/plate_bound/sinai_fault_extract.txt"
PBpb = np.loadtxt(path_pb)

Xplate, Yplate = m(PBpb[:,0],PBpb[:,1])
m.plot(Xplate,Yplate,
       color='red',
       linewidth = 2)

title = title_prefix + " velocities w.r.t. " + title_midfix_plate + " \n using " + software

plt.suptitle(title)

export_path = os.path.join(export_dir,"_".join(("vel_map",
                                               source_run,
                                               HV_mark,
                                               pole_used,
                                               str(scale_arrow))))

plt.tight_layout()
plt.subplots_adjust(top=0.90)

for ext in (".png",".svg",".pdf"):
    plt.savefig(export_path + ext)
            