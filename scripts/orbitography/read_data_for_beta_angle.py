#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:47:41 2017

@author: adminuser
"""

import genefun as gf
import numpy as np
import geodetik as geok
import pandas as pds

def yaw_nominal_gal_iov(Psat,Vsat,Psun,switch_mode = False):
    
    Psat = np.array( Psat )
    Vsat = np.array( Vsat )
    Psun = np.array( Psun )   

    Psun_norm = Psun / np.linalg.norm(Psun)
    
    S = geok.ECI2RTN_or_RPY(Psat,Vsat,Psun_norm,out_rpy=1)
        
    AY1 = -S[1] / np.sqrt(1- S[2]**2)
    AY2 = -S[0] / np.sqrt(1- S[2]**2)
    
    PSI_IOV = np.arctan2(AY1,AY2) 
    #PSI_IOV = np.arctan2(-S[1],-S[0]) 
    
    if switch_mode:
        PSI_IOV *= -1
    
    return PSI_IOV , S

def yaw_nominal_gal_foc(Psat,Vsat,Psun,switch_mode = False):
        
    Psat = np.array( Psat )
    Vsat = np.array( Vsat )
    Psun = np.array( Psun )   
    
    Psat_norm = Psat / np.linalg.norm(Psat)
    Vsat_norm = Vsat / np.linalg.norm(Vsat)
    Psun_norm = Psun / np.linalg.norm(Psun)
    
    if not switch_mode:
        N_norm    = np.cross(Psat_norm,Vsat_norm)
        KROSS  = np.cross(Psat_norm,N_norm)

    else:
        N_norm = np.cross(Vsat_norm,Psat_norm)
        KROSS  = np.cross(N_norm,Psat_norm)
    
    AT1 = np.dot(Psun_norm,N_norm)  
    AT2 = np.dot(Psun_norm,KROSS)
    
    
    PSI_FOC = np.arctan2(AT1,AT2)
    
    return PSI_FOC


adding_ICO = True

fil = '/home/adminuser/aaa_FOURBI/10.03_pdm7_1_post_a.log'
fil = '/home/adminuser/aaa_FOURBI/10.03_pdm7_0_clean.log'

parfol = "/home/adminuser/aaa_FOURBI/RAec3/"

filist = sorted(gf.find_recursive(parfol , '10.03_pdm7_0_clean.log'))
#filist = [filist[-1]]

#filist = ['/home/adminuser/aaa_FOURBI/10.03_pdm7_0_clean.log']

plt.close('all')


for fil in filist:
    
    datadiclist = []
    DFstk = []

    print(fil)
    for cle in ('XIV','XFC'):
        print(cle)
        L = gf.grep(fil,cle)
    
        L = [e.strip() for e in L]
    
        keez = gf.uniqify_list([e.split()[0] for e in L])
        
        datadic = dict()
        
        for k in keez:
            datadic[k] = []
            
        for ll in L:
            l = ll.split()
            curk = l[0].strip()
            if 'cond' in curk:
                
                datadic[curk].append([0 if l[1:] == 0 else 1])
            else:
                datadic[curk].append([float(e) for e in l[1:]])
    
        bigdata  = []
        titlelis = []
        
        for k in keez:
            datadic[k] = np.stack(datadic[k])
            bigdata.append(datadic[k])
            
            if adding_ICO:
                ICOprefix = k[3]
            else:
                ICOprefix = ''
            
            if datadic[k].shape[1] != 1:
                titlelis = titlelis + [ICOprefix + k[5:] + '_' + str(i+1) for i in range(datadic[k].shape[1])] 
            else:
                titlelis.append(ICOprefix + k[5:])
            
        BIGdata = np.concatenate(bigdata,axis=1)
        
        DF = pds.DataFrame(BIGdata , columns = titlelis)
        DFstk.append(DF)
    
    
    DFmain = DFstk[0]
    DFbis  = DFstk[1]
    
    DFmain.columns
    DFbis.columns
    
    #DFbis['Cdtim']
    
    #for  irow , row in DFmain.iterrows():  
    #    xsat = row[['Ixsat_1','Ixsat_2','Ixsat_3']]
    #    xsun = row[['Ixsun_1','Ixsun_2','Ixsun_3']]
    #    vsat = row[['Ivsat_1','Ivsat_2','Ivsat_3']]
    #    yaw_iov , S = yaw_nominal_gal_iov(xsat,xsun,vsat,switch_mode=0)
    #    yaw_foc = yaw_nominal_gal_foc(xsat,xsun,vsat,switch_mode=0)
    #    
        #print yaw_iov , yaw_foc , row['yran_2'] , DFbis.iloc[irow]['yran_2']
    
    #    print yaw_iov , yaw_foc , row['Oyran_2'] , DFbis.iloc[irow]['Oyran_2']
    
        #print 'S1', S
        #print 'S2' , DFbis.iloc[irow]['Csuor_1'] , DFbis.iloc[irow]['Csuor_2'] , DFbis.iloc[irow]['Csuor_3']
    
    #%%
#    plt.close('all')
    
    for isat,sat in enumerate(set(DFbis['Iisat'])) :
        if not (sat in (36,)): #range(34,40)
            print(sat , 'not in range')
            continue
        plt.figure()
        DFmain_sat = DFmain[DFmain['Iisat'] == sat]
        DFbis_sat  = DFbis[DFbis['Iisat'] == sat] 
    
        # MANU
        BETA    = DFmain_sat['Cbeta']
        sunors1 = DFmain_sat[['Csuor_1', 'Csuor_2', 'Csuor_3']]
        
        ze_valu_a_ateindre_via_trigotrick = np.sin(np.deg2rad(4.1+np.pi*2))
    
        ze_valu = np.sin(np.deg2rad(4.1) + 0.035*np.pi)
        ze_valu = np.sin(np.deg2rad(4.1))
        ze_valu = np.sin(np.deg2rad(15))  
        ze_valu = np.cos(np.deg2rad(4.1))
    
        daux = np.abs( np.arcsin( ze_valu / np.cos(BETA) ) )  
        daux = np.abs( np.arccos( ze_valu / np.cos(BETA) ) )  
    
    
        sunors = np.divide(sunors1 , np.linalg.norm(sunors1,axis=1)[:,None])
    
    
        usatSer = 1.5 * np.pi - np.arctan2(sunors['Csuor_3'],sunors['Csuor_1'])
        
        usat = np.array(usatSer)
        
    #    usat = 1.5d0 * pi - atan2(sunors(3),sunors(1))
    #    if (usat .gt. two_pi) usat = usat - two_pi   ! usat is in the range:   0<=usat<=two_pi
    #    if (usat .gt.     pi) usat = usat - two_pi   ! usat is in the range: -pi<=usat<=pi
    
    #    uaux = usat
    #    if (abs(usat) > 0.5*pi) then
    #      uaux = uaux - sign(pi,usat)   ! Distinguish orbit noon/midnight
    #    end if
    #    uaux = uaux + daux
    
        
        estk = []
        for e in usat:
            if e > 2*np.pi: e = e - 2*np.pi
            if e > 1*np.pi:  e =  - 2*np.pi
            estk.append(e)
        usat = np.array(estk)
    #    
        uaux = usat
    
        uauxeltstk = []
        for uauxelt , usatelt in zip(uaux,usat):
            if (abs(usatelt) > 0.5*np.pi):
                uauxelt = uauxelt - np.pi * np.sign(usatelt) 
            uauxeltstk.append(uauxelt)
        
        uaux = np.array(uauxeltstk)
    #    
        uaux = uaux + daux
    
    
        ang_vel = 24.0 / DFmain_sat['Creti'] *  2*np.pi
        dtim    = uaux / ang_vel
            
        
        XXX1 = DFmain_sat['Itsen']
        YYY1 = DFmain_sat['Cdtim']  #Cdtim
        XXX2 = DFbis_sat['Itsen']
        YYY2 = DFbis_sat['Cdtim']
        YYYE = DFbis_sat['Cdt_e']
        YYYB = DFbis_sat['Cdt_b']
    
    
        if 0:
            plt.plot(XXX1*86400,YYY1*86400,'xb',label='IOV in eclipse')
            plt.plot(XXX2*86400,YYY2*86400,'xr',label='FOC in eclipse')
            plt.plot(XXX2*86400,YYYE*86400,'o',label='1st ep. in eclipse for epsilon cond.')
            plt.plot(XXX2*86400,YYYB*86400,'o',label='1st ep. in eclipse for beta cond.')
            plt.legend()
            print("plotting")
            plt_name_prefix = 'eclipse_start'
            #plt_outname = plt_name_prefix + '_' + gf.join_improved('_',*geok.dt2gpstime(pdat))
            plt_outname = plt_name_prefix  + '_E' + str(int(sat)) + '_' +  fil.split('/')[6]
            plt_outdir  = '/home/adminuser/aaa_FOURBI/ANA/plotsFOC3/'
            gf.create_dir(plt_outdir)
            plt_outname = plt_name_prefix  + '_E' + str(int(sat)) + '_' +  fil.split('/')[-3]
            #plt_outname = "toto"

            for extplt in ('svg',):
                outpath = os.path.join(plt_outdir, plt_outname + '.' + extplt)
                plt.savefig(outpath)
            

            
        #plt.plot(XXX2,DFbis_sat['Cdti2'],'*')
        #plt.plot(XXX2,dtim,'+g')
        
        if 0:
    #        plt.plot(XXX2,DFbis_sat['C1nu2'],'.')
            plt.plot(XXX2,DFbis_sat['Crsat'],'.')
    
        def sign_mod(A):
            return 1 * (A >= 0) + (-1) * (A<0)


        if 0:
            # les yaw finaux 
            plt.plot(XXX1,DFmain_sat['Oyran_2'],'+')
            plt.plot(XXX2,DFbis_sat['Oyran_2'],'x')
            
            psi_init = np.array(DFbis_sat['Lyas2'])
            t_mod    = np.array(DFbis_sat['Ldtim'])
            signe    = sign_mod(psi_init)
            
            A1 = (np.pi * .5) * signe 
            A2 = (psi_init - (np.pi * .5) * signe)
            A3 = np.cos(86400. * t_mod * ((2. * np.pi) / 5656.))
            YAWmanu  =  A1 + A2 * A3  
            plt.plot(XXX2,YAWmanu,'.')
            #plt.plot(XXX2,t_mod,'x')
            #plt.plot(XXX2,DFbis_sat['Cdtim'],'+')
            
            np.all(np.isclose(DFbis_sat['LyaA1'] , A1))
            np.all(np.isclose(DFbis_sat['LyaA2'] , A2))        
            np.all(np.isclose(DFbis_sat['LyaA3'] , A3))
    
        if 0:
            plt.plot(XXX1,np.rad2deg(DFmain_sat['Oyran_2'] - DFmain_sat['Oyran_3']),'+')
            plt.plot(XXX2,np.rad2deg(DFbis_sat['Oyran_2']  - DFbis_sat['Oyran_3']),'x')
                    
    
        if 0:
            plt.plot(XXX1,np.rad2deg(DFmain_sat['Oyran_2']),'+b')
            plt.plot(XXX2,np.rad2deg(DFbis_sat['Oyran_2']) ,'+r')
                    
            plt.plot(XXX1,np.rad2deg(DFmain_sat['Oyran_3']),'xb')
            plt.plot(XXX2,np.rad2deg(DFbis_sat['Oyran_3']) ,'xr')
    
    
        if 1:            
            plt.plot(XXX1,(DFmain_sat['Oyran_1']),'+')
            plt.plot(XXX2,(DFbis_sat['Oyran_1']) ,'x')


        if 0:            
            plt.plot(XXX2,(DFbis_sat['Cyaso']) ,'x')

        if 0:            
            plt.plot(XXX2,(DFbis_sat['Cepso']) ,'x')
            #plt.plot(XXX1,(DFmain_sat['Oyran_1'] - DFbis_sat['Oyran_1']),'.')
                    
    
        if 0:
            plt.plot(XXX1,np.rad2deg(DFmain_sat['Oyran_2']),'+')
            plt.plot(XXX2,np.rad2deg(DFbis_sat['Oyran_2']) ,'x')
    
            plt.plot(XXX1,np.rad2deg(DFmain_sat['Oyran_2'] - DFbis_sat['Oyran_2']),'.')
                    
        if 0:
                    
            plt.plot(XXX1,np.rad2deg(DFmain_sat['Oyran_3']),'+')
            plt.plot(XXX2,np.rad2deg(DFbis_sat['Oyran_3']) ,'x')
    
            plt.plot(XXX1,np.rad2deg(DFmain_sat['Oyran_3'] - DFbis_sat['Oyran_3']),'.')
                    
        if 0:
            plt.plot(XXX1,DFbis_sat['Cdt_e'],'.')
            plt.plot(XXX2,DFbis_sat['Cdt_b'],'x')
            plt.plot(XXX2,DFbis_sat['Cdt2b'],'+')        
    
        if 0:
            plt.plot(XXX1,DFbis_sat['Ca__b'],'+')
            plt.plot(XXX2,DFbis_sat['Cb__b'],'x')
    
    un_sur_nu = 6380. / (23222. + 6380. ) 
    
    un_sur_nu**2
    