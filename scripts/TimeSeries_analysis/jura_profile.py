#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:28:56 2018

@author: psakicki
"""

from megalib import *
import pandas as pd
import utm
import matplotlib.pyplot as plt
import geodetik as geok
import numpy as np
import matplotlib.lines as mlines
from adjustText import adjust_text

p = "/home/psakicki/GFZ_WORK/RENDU/1711_Article_Jura_MRabin/Review_Work_for_AW/vel_jura_rw4_itrf.vel"


p = "/home/psakicki/GFZ_WORK/RENDU/1711_Article_Jura_MRabin/Review_Work_for_AW/vel_jura_rw4_europe.vel"
pp = "/home/psakicki/GFZ_WORK/RENDU/1711_Article_Jura_MRabin/Review_Work_for_AW/vel_jura_rw4.org"
PREFIX = "AW"

outplotdir = '/home/psakicki/GFZ_WORK/RENDU/1711_Article_Jura_MRabin/Review_Work_for_AW/OUTPUT_PLOT/' + PREFIX

gf.create_dir(outplotdir)

D = gfc.read_globk_vel_file(p)


plot_droite = True 

blue_star       = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                          markersize=2, label='< 5 years')
red_square      = mlines.Line2D([], [], color='xkcd:tangerine', marker='o', linestyle='None',
                          markersize=2, label='5 < years < 8')
purple_triangle = mlines.Line2D([], [], color='blue', marker='o', linestyle='None',
                          markersize=2, label='> 8 years')
pale_dot        = mlines.Line2D([], [], color='xkcd:sky blue', marker='o', linestyle='None',
                          markersize=2, label='> 8 years \n (not used for\n regression)')


def age_color(stat):
    age = stat_age_dict[stat]
    if age < 5.:
        color = 'r'
    elif 5. < age < 8.:
        color = 'xkcd:tangerine'
    elif age > 8.:
        color = 'b'
    return color
stat_color_dict = dict()

#L  = genefun.grep(pp,"Postion of ")
#LL = [(e.split()[2],np.abs(float(e.split()[-2]))) for e in L]

L = genefun.grep(pp,"pbr.")

diclength_all = dict()
Stat_lis = [] 
Leng_lis = []
LL_stk = []
for l in L:
    lsplit = l.split()
    DATE = [geok.date_string_2_dt(e) for e in lsplit[-2:]]
    ddif = DATE[1] - DATE[0]
    LL = [lsplit[1]] + DATE + [ddif.days / 365.25]
    diclength_all[LL[0]] = LL
    LL_stk.append(LL)

Period_DF = pd.DataFrame(LL_stk)

pt_alsace = np.array([47.564746, 7.303990])
pt_ain    = np.array([46.323922, 5.483940])

main_ori  = geok.vincenty_full(pt_ain,pt_alsace)

long_milieu = np.mean([pt_alsace[0] , pt_ain[0]])
lat_milieu  = np.mean([pt_alsace[1] , pt_ain[1]])


#utm.from_latlon(lat_milieu,long_milieu)
#
#utm_stk = []
#for lat , lon in zip(D["Lat"],D["Long"]):
#    if lon > 180:
#        lon = lon - 360
#    utm_pt = utm.from_latlon(lat,lon)
#    utm_stk.append(utm_pt)
#    plt.scatter(utm_pt[0],utm_pt[1])

D["SITE"] = D["SITE"].str[0:8]
D["Long"][D["Long"] > 180] = D["Long"][D["Long"] > 180] - 360

geok.lambert_projection_CC_frontend(*np.flipud(pt_alsace))
xain,yain      =geok.lambert_projection_CC_frontend(*np.flipud(pt_ain))
xalsace,yalsace=geok.lambert_projection_CC_frontend(*np.flipud(pt_alsace))
xbrest,ybrest  =geok.lambert_projection_CC_frontend(*(np.flipud([48.3389, -4.4852])))
xmilieu,ymilieu = np.mean([xalsace,xain]) , np.mean([yalsace,yain])
Pmilieu = np.array([xmilieu,ymilieu])

X,Y=geok.lambert_projection_CC_frontend(D["Long"],D["Lat"])

fig1 , ax1 = plt.subplots()
fig3 , ax3 = plt.subplots()

plt.clf()

ax1.axis('equal')
ax1.scatter(X,Y)
ax1.scatter(xalsace,yalsace,c="r")
ax1.scatter(xain,yain,c="r")
ax1.scatter(xbrest,ybrest,c="r")
ax1.scatter(xmilieu,ymilieu,c="r")

Pain   = np.array([xain , yain])
Valain = np.array([xalsace - xain,yalsace - yain])
Vortho = np.array([-Valain[1],Valain[0]]) 
Vortho = Vortho / np.linalg.norm(Vortho)
Vortho = Vortho * 5000
ax1.scatter(xmilieu + Vortho[0],ymilieu + Vortho[1],c="g")

Vortho2 = np.array([-Vortho[0],-Vortho[1]])
ax1.scatter(xmilieu + Vortho2[0],ymilieu + Vortho2[1],c="y")

#### ANGLE POUR ROTATION
theta  = geok.anglesfromvects(1,0,Valain[0],Valain[1])
theta2 = geok.anglesfromvects(1,0,Vortho2[0],Vortho2[1])

MatRot = geok.C_2D(theta2)
MatRot.dot([1,-1])

#### FILTRAGE
sLength  = len(D['E'])
D['Dh_along'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['Xh_along'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['Yh_along'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['Dmilieu_along'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)

D['Dh_across'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['Xh_across'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['Yh_across'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['Dmilieu_across'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)

D['E2'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['N2'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['E2_sig'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['N2_sig'] = pd.Series(np.ones(sLength)*np.nan, index=D.index)
D['color']  = pd.Series(["k"] * sLength , index=D.index)
D['age']  = pd.Series([np.nan] * sLength , index=D.index)
D['network']  = pd.Series(["aaa"] * sLength , index=D.index)


for x,y,(irow,Dlin) in zip(X,Y,D.iterrows()):
    XX = np.array([x,y])
    Ph_along , Dh_along   = geok.orthogonal_projection(XX , Pain , Valain)
    Ph_across , Dh_across = geok.orthogonal_projection(XX , Pmilieu , Vortho2)
    
    EN2    = MatRot.dot(np.array([Dlin['E'],Dlin['N']]))
    ENsig2 = MatRot.dot(np.array([Dlin['E_sig'],Dlin['N_sig']]))
    SIGMA  = np.array([[Dlin['E_sig']**2,Dlin['Rho']],
                      [Dlin['Rho'],Dlin['N_sig']**2]])
    
    SIGMA2 = np.abs(MatRot.dot(SIGMA).dot(MatRot.T))
    #ENsig2 = MatRot.dot(np.array([np.sqrt(SIGMA2[0,0]),np.sqrt(SIGMA2[1,1])]))
    ENsig2 = np.array([np.sqrt(SIGMA2[0,0]),np.sqrt(SIGMA2[1,1])])
        
    MatRot.dot([1,-1])
    
#    if np.abs(Dh_along) < 80*1000. and 1:
#    if np.abs(Dh_across) < 100*1000. and np.abs(Dh_along) < 100*1000:
    if "MR" in PREFIX:
        size_select = 200
    else:
        size_select = 100
    if np.abs(Dh_across) < size_select*1000. and np.abs(Dh_along) < size_select*1000:
        Dmilieu_along = geok.dist(Ph_along,Pmilieu)
        Dlin["Dh_along"] = Dh_along
        Dlin["Xh_along"] = Ph_along[0]
        Dlin["Yh_along"] = Ph_along[1]
        booll = (Ph_along - Pmilieu) > 0
        if np.all(booll):
            k =  -1
        else:
            k = 1
        Dlin["Dmilieu_along"] = k * Dmilieu_along
        
        Dmilieu_across = geok.dist(Ph_across,Pmilieu)
        Dlin["Dh_across"] = Dh_across
        Dlin["Xh_across"] = Ph_across[0]
        Dlin["Yh_across"] = Ph_across[1]
        diff_direct = (Ph_across - Pmilieu)
        
        if   diff_direct[0] > 0 and diff_direct[1] < 0:
            k =  1
        elif diff_direct[0] < 0 and diff_direct[1] > 0:
            k = -1
        else:
            print("ERRRRRRRRRRRRRRRRRRROOOOOOOOOOOORRRRRRRRRRRRRR")
        Dlin["Dmilieu_across"] = k * Dmilieu_across        
        
        Dlin["E2"] = EN2[0]
        Dlin["N2"] = EN2[1]

        Dlin["E2_sig"] = ENsig2[0]
        Dlin["N2_sig"] = ENsig2[1]

        ax1.scatter(Ph_along[0],Ph_along[1]  ,c="k")
        ax1.scatter(Ph_across[0],Ph_across[1],c="gray")
        D.loc[irow] = Dlin 

DD = D[~np.isnan(D["Dmilieu_across"])]

######### Recherche des segement les plus long

### Sur les stations sleectionnes
site_all  = DD["SITE"].apply(lambda x: x.split("_")[0])
site_uniq = DD["SITE"].apply(lambda x: x.split("_")[0]).unique()

L_site_period_longest_stk = []
stat_age_dict = dict()
for site in site_uniq:
    site_period = Period_DF[Period_DF[0].str.contains(site)]
    site_period_longest = site_period[site_period[3] == np.max(site_period[3])]
    L_site_period_longest_stk.append(str(site_period_longest[0]).split()[1])
    
    stat_age_dict[site] = (np.max(site_period[2]) - np.min(site_period[1])).days / 325.25

DDD = DD[DD["SITE"].isin(L_site_period_longest_stk)]


### Sur toutes les stations pour export de la liste des stations 
if False:
    network_dict = dict()
    pnet = "/home/psakicki/GFZ_WORK/RENDU/1711_Article_Jura_MRabin/network_lists/"
    network_dict["AGNES"] = pd.read_table(pnet + "agnes.txt",header=-1)
    network_dict["IGS"]   = pd.read_table(pnet + "igs.txt",header=-1)
    network_dict["RGP"]   = pd.read_table(pnet + "rgp.txt",header=-1)
    network_dict["RENAG"] = pd.read_table(pnet + "renag.txt",header=-1)
    
    
    site_all  = D["SITE"].apply(lambda x: x.split("_")[0])
    site_uniq = D["SITE"].apply(lambda x: x.split("_")[0]).unique()
    
    L_site_period_longest_stk = []
    stat_age_dict = dict()
    stat_install_dict = dict()
    
    for site in site_uniq:
        site_period = Period_DF[Period_DF[0].str.contains(site)]
        site_period_longest = site_period[site_period[3] == np.max(site_period[3])]
        L_site_period_longest_stk.append(str(site_period_longest[0]).split()[1])
    
        stat_age_dict[site]     = (np.max(site_period[2]) - np.min(site_period[1])).days / 325.25    
        stat_install_dict[site] =geok.dt2year_decimal(np.min(site_period[1]))
    
    
    DDD_all_stats = D[D["SITE"].isin(L_site_period_longest_stk)]
    DDD2_stk = []
    for irow , drow in DDD_all_stats.iterrows():
        color = None
        color = age_color(drow["SITE"][0:4])
        drow["color"] = color
        drow["age"]   = stat_install_dict[drow["SITE"][0:4]]
        drow["SITE"] = drow["SITE"][0:4]
        netstrout = []
        for netnam , netlist in network_dict.items():
            if np.any(netlist == drow["SITE"][0:4]):
                netstrout.append(netnam)
        #if "RGP" in netstrout and "RENAG" in netstrout:
        netstrout = sorted(netstrout)
        drow["network"] = "/".join(netstrout)
        DDD2_stk.append(drow)
    
    DDD_all_stats = pd.DataFrame(DDD2_stk)
    outpath = "/home/psakicki/GFZ_WORK/RENDU/1711_Article_Jura_MRabin/Review_Work_for_AW/"
    #DDD_all_stats.drop(['Dh_along','Xh_along','Yh_along','Dmilieu_along',
    #                    'Dh_across','Xh_across','Yh_across','Dmilieu_across',
    #                    'E2','N2','E2_sig','N2_sig'],inplace=True)
    DDD_all_stats.to_csv(outpath + os.path.basename(p) + ".csv" )

plt.clf()

##### CLEAN BAD STAT
bad_stat_list = ["ZIM2_GPS"]
DDD = DDD[np.logical_not(DDD["SITE"].isin(bad_stat_list))]

####### FIG E
figE , axE = plt.subplots()

#axE.errorbar(DDD["Dmilieu_across"] / 1000., DDD["E2"],np.abs(DDD["E2_sig"]),fmt="o")
#axE.plot(DDD["Dmilieu"] / 1000., len(DDD["Dmilieu"]) * [0],".")

#%%
########### FABRICATION DE LA COULEUR ET DES PTS POUR LA REGRESSSION   

#### regression
#DDD_aged_stat_PS = DDD[DDD["color"] == "b"]
#stat_old_list_PS = list(DDD_aged_stat_PS["SITE"].str[0:4])
if PREFIX == "PS":
    stat_old_list_PS = ['HUTT',
     'ZIMM',
     'LUCE',
     'BOUR',
     'PAYE',
     'NEUC',
     'BLFT',
     'FRAC',
     'EPFL',
     'STCX',
     'PRNY',
     'GENE',
     'BSCN',
     'JOUX',
     'SEUR']
    DDD_aged_stat_PS = DDD[DDD["SITE"].str[0:4].isin(stat_old_list_PS)]

    DDD_aged_stat = DDD_aged_stat_PS
    stat_old_list = stat_old_list_PS
#==============================0
elif PREFIX == "AW":
    stat_old_list_AW = ['BOUR', 'BSCN', 'EPFL', 'ETHZ', 'FHBB', 'FRIC', 'GENE', 'HUTT', 
                        'JOUX', 'NEUC', 'PAYE', 'SEUR', 'SJDV', 'STCX' , 'ZIMM']
    DDD_aged_stat_AW = DDD[DDD["SITE"].str[0:4].isin(stat_old_list_AW)]

    DDD_aged_stat = DDD_aged_stat_AW
    stat_old_list = stat_old_list_AW
# ===================================
elif PREFIX == "MR1":
    stat_old_list_MR1 = [ 'SJDV', 'SEUR', 'BSCN', 'BOUR', 'FHBB', 'FRIC']
    DDD_aged_stat_MR1 = DDD[DDD["SITE"].str[0:4].isin(stat_old_list_MR1)]

    DDD_aged_stat = DDD_aged_stat_MR1
    stat_old_list = stat_old_list_MR1    
elif PREFIX == "MR2":
    stat_old_list_MR2 = ["JOUX", "STCX", "NEUC"]
    DDD_aged_stat_MR2 = DDD[DDD["SITE"].str[0:4].isin(stat_old_list_MR2)]
    
    DDD_aged_stat = DDD_aged_stat_MR2
    stat_old_list = stat_old_list_MR2
elif PREFIX == "MR3":
    stat_old_list_MR3 = ['GENE' , 'EPFL' , 'PAYE' , 'ZIMM' , 'HUTT' ,'ETHZ']
    DDD_aged_stat_MR3 = DDD[DDD["SITE"].str[0:4].isin(stat_old_list_MR3)]

    DDD_aged_stat = DDD_aged_stat_MR3
    stat_old_list = stat_old_list_MR3

#### Couleur 
for site in site_uniq:
    stat_color_dict[site] = age_color(site)
    
DDD2_stk = []
for irow , drow in DDD.iterrows():
    color = None
    color = age_color(drow["SITE"][0:4])
    drow["color"] = color
    if (drow["color"] == "b") and not (drow["SITE"][0:4] in stat_old_list):
        drow["color"] = "xkcd:sky blue"
        print("LIGHT BLUUUUUE")
    drow["age"]   = stat_age_dict[drow["SITE"][0:4]]
    DDD2_stk.append(drow)
DDD = pd.DataFrame(DDD2_stk)


#### PARAM LABEL PTS
ha="center"
size=8
xytext=(15,11)
rotation=30

for irow , drow in DDD.iterrows():
    axE.errorbar(drow["Dmilieu_across"] / 1000., drow["E2"],drow["E2_sig"],c=drow["color"],fmt="o")
    #axE.scatter(drow["Dmilieu_across"] / 1000., drow["E2"],
    #            c=stat_color_dict[str(drow["SITE"][0:4])])
    axE.annotate(drow["SITE"][0:4],(drow["Dmilieu_across"] / 1000. , drow["E2"]),
                 rotation=rotation,textcoords="offset points",xytext=xytext,ha=ha,size=size)   

Dist = DDD_aged_stat["Dmilieu_across"] / 1000.
a,b,confid_interval_slope,std_err = geok.linear_regression(Dist ,  DDD_aged_stat["E2"] , fulloutput=True)
Xreg , Yreg = geok.linear_reg_getvalue(np.linspace(np.min(Dist)-10,np.max(Dist)+10) , a , b )

gf.axis_data_coords_sys_transform(axE,.1,.1)
axE.plot(Xreg , Yreg)


axE.set_xlim(-80,80)
axE.set_ylim(-1.5,2.5)
axE.set_ylim(-1,1)

xregtxt , yregtxt = .03,.08
XYtxt = gf.axis_data_coords_sys_transform(axE,xregtxt , yregtxt)
axE.text(XYtxt[0] , XYtxt[1] , "regression :\n" +  str(np.round(a,5)) + "±" + str(np.round(std_err,5)) + " mm/yr/km",size=10)


figE.suptitle("GPS horizontal velocities along NW-SE profile, profile-parallel vels.")

axE.set_xlabel("NW-SE Distance to the profile center (km)")
axE.set_ylabel("Velocity (mm/yr)")
axE.legend(handles=[blue_star, red_square, purple_triangle,pale_dot], prop={'size': 8},loc=4)

figE.tight_layout()
figE.subplots_adjust(top=0.90)

for ext in (".png" ,".pdf",".svg"):

    figE.savefig(os.path.join(outplotdir , "H_parall" + ext))


####### FIG N
figN , axN = plt.subplots()

#axE.plot(DDD["Dmilieu"] / 1000., len(DDD["Dmilieu"]) * [0],".")

Txt_stk = []
for irow , drow in DDD.iterrows():
    axN.errorbar(drow["Dmilieu_across"] / 1000., drow["N2"],drow["N2_sig"],c=drow["color"],fmt="o")
#    axN.scatter(drow["Dmilieu_along"] / 1000., drow["N2"],
#                c=stat_color_dict[str(drow["SITE"][0:4])])
    txt = axN.annotate(drow["SITE"][0:4],(drow["Dmilieu_across"] / 1000. , drow["N2"]),
                 rotation=rotation,textcoords="offset points",xytext=xytext,ha=ha,size=size)
#    Txt_stk.append(txt)

#DDD_aged_stat = DDD[DDD["color"] == "b"]
Dist = DDD_aged_stat["Dmilieu_across"] / 1000.
a,b,confid_interval_slope,std_err = geok.linear_regression(Dist ,  DDD_aged_stat["N2"] , fulloutput=True)
Xreg , Yreg = geok.linear_reg_getvalue(np.linspace(np.min(Dist)-10,np.max(Dist)+10) , a , b )
axN.plot(Xreg , Yreg)


axN.set_xlim(-80,80)
axN.set_ylim(-1.5,2.5)
axN.set_ylim(-1,1)

XYtxt = gf.axis_data_coords_sys_transform(axN,xregtxt , yregtxt)
axN.text(XYtxt[0] , XYtxt[1] , "regression :\n" +  str(np.round(a,5)) + "±" + str(np.round(std_err,5)) + " mm/yr/km",size=10)


figN.suptitle("GPS horizontal velocities along NW-SE profile, profile-perpendicular vels.")
axN.set_xlabel("NW-SE Distance to the profile center (km)")
axN.set_ylabel("Velocity (mm/yr)")

#adjust_text(Txt_stk,only_move={'points':'y', 'text':'y', 'objects':'y'})
axN.legend(handles=[blue_star, red_square, purple_triangle,pale_dot], prop={'size': 8},loc=4)
figN.tight_layout()
figN.subplots_adjust(top=0.90)

for ext in (".png" , ".pdf",".svg"):

    figN.savefig(os.path.join(outplotdir , "H_perpend" + ext))


####### FIG EV
figEV , axEV = plt.subplots()

#axE.errorbar(DDD["Dmilieu_across"] / 1000., DDD["E2"],np.abs(DDD["E2_sig"]),fmt="o")
axEV.set_xlim(-190,190)
#axE.plot(DDD["Dmilieu"] / 1000., len(DDD["Dmilieu"]) * [0],".")

for irow , drow in DDD.iterrows():
    #axEV.scatter(drow["Dmilieu_across"] / 1000., drow["H"],
    #             c=stat_color_dict[str(drow["SITE"][0:4])])
    axEV.errorbar(drow["Dmilieu_across"] / 1000., drow["H"],drow["H_sig"],c=drow["color"],fmt="o")
    axEV.annotate(drow["SITE"][0:4],(drow["Dmilieu_across"] / 1000. , drow["H"]),
                 rotation=rotation,textcoords="offset points",xytext=xytext,ha=ha,size=size)

#DDD_aged_stat = DDD[DDD["color"] == "b"]
Dist = DDD_aged_stat["Dmilieu_across"] / 1000.
a,b,confid_interval_slope,std_err = geok.linear_regression(Dist ,  DDD_aged_stat["H"] , fulloutput=True)
Xreg , Yreg = geok.linear_reg_getvalue(np.linspace(np.min(Dist)-10,np.max(Dist)+10) , a , b )
axEV.plot(Xreg , Yreg)


axEV.set_xlim(-80,80)
axEV.set_ylim(-4.5,12)
axEV.set_ylim(-1,1)

XYtxt = gf.axis_data_coords_sys_transform(axEV,xregtxt , yregtxt)
axEV.text(XYtxt[0] , XYtxt[1] , "regression : \n" +  str(np.round(a,5)) + "±" + str(np.round(std_err,5)) + " mm/yr/km",size=10)


figEV.suptitle("GPS vertical velocities along NW-SE profile")

axEV.set_xlabel("NW-SE Distance to the profile center (km)")
axEV.set_ylabel("Velocity (mm/yr)")
axEV.legend(handles=[blue_star, red_square, purple_triangle,pale_dot], prop={'size': 8},loc=4)
figEV.tight_layout()
figEV.subplots_adjust(top=0.90)

for ext in (".png" , ".pdf",".svg"):
    figEV.savefig(os.path.join(outplotdir , "V" + ext))



DDD.to_csv(outplotdir + "/export_data_" + PREFIX + ".csv" )


######## FIG NV
#figNV , axNV = plt.subplots()
#
##axN.errorbar(DDD["Dmilieu_along"] / 1000., DDD["N2"],np.abs(DDD["N2_sig"]),fmt="o")
##axE.plot(DDD["Dmilieu"] / 1000., len(DDD["Dmilieu"]) * [0],".")
#
#for irow , drow in DDD.iterrows():
#    color = None
#    color = age_color(drow["SITE"][0:4])
##    axNV.scatter(drow["Dmilieu_along"] / 1000., drow["H"],
##                 c=stat_color_dict[str(drow["SITE"][0:4])])
#    axNV.errorbar(drow["Dmilieu_across"] / 1000., drow["H"],drow["H_sig"],c=color,fmt="o")
#    axNV.annotate(drow["SITE"][0:4],(drow["Dmilieu_across"] / 1000. , drow["H"]),
#                 rotation=90)
#    
#    
#
#figNV.suptitle("SW-NE (along arc) profile of GPS vertical velocities")
#axNV.set_xlabel("NW-SE Distance to the profile center (km)")
#axNV.set_ylabel("Velocity (mm/yr)")
#
#axNV.set_xlim(-80,80)
#axNV.set_ylim(-4.5,12)
#axNV.legend(handles=[blue_star, red_square, purple_triangle])
#figNV.tight_layout()
#figNV.subplots_adjust(top=0.90)
#
#for ext in (".png" , ".pdf",".svg"):

#    figNV.savefig(os.path.join(outplotdir , "Along_V" + ext))

if 0:
    print(DDD[["SITE","E","N","E2","N2"]])

########### TROUVER LA BONNE VELOCITE
stat     = "SJDV"
Dstat    = D[D["SITE"].str.contains(stat)]
normV    = np.sqrt(Dstat["E"]**2 + Dstat["N"]**2)
oriV     = np.rad2deg(np.arctan2(Dstat["E"] , Dstat["N"]))
normVadj = np.sqrt(Dstat["E_adj"]**2 + Dstat["N_adj"]**2)