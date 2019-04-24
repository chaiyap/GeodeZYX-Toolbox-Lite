# -*- coding: utf-8 -*-
"""
Created on Sun May  1 16:48:32 2016

@author: psakicki


script tres tres exploratoire pour la fonction add_offset
il y a des disfonctionnement entre la théorie et la pratique
ici on a chercher à concillier les 2 en ajoutant des facteurs moins
et en inversant les angles RPY
"""


from megalib import *

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#fig = plt.figure()
#ax  = fig.gca(projection='3d')

# === Partie Exploratoire
if 0:
    V   = [0,1,0]
    dV  =  np.array([1,0,0])
    goodresult = np.array([0,2,0])
    
    V   = [0,-1,0]
    dV  =  np.array([0,1,0])
    goodresult = np.array([1,-1,0])
    #
    #V   = [0,0,1]
    #dV  =  np.array([1,0,0])
    #goodresult = np.array([0,0,2])
    
    #
    #V   = [0,0,-2]
    #dV  =  np.array([-1,0,0])
    #goodresult = np.array([0,0,-1])
    
    #V   = [0,0,-2]
    #dV  =  np.array([1,0,0])
    #goodresult = np.array([0,0,-3])
    
    
    stkgood = []
    
    rpy_raw = vector_RPY(V,1)
    
    
    print(V , dV)
    
    i = 0
    
    
    for koef in  list(itertools.combinations_with_replacement((1,-1),3)):
        for rpy , rpyorder  in  zip(itertools.permutations(rpy_raw,3) , itertools.permutations((1,2,3),3)):
            
            i = i+1
            
            rpy = rpy * np.array(koef)
            print(rpy , i)    
            
            C_rpy2enu = geok.C_rpy2enu(*rpy)
            C_enu2rpy = np.linalg.inv(geok.C_rpy2enu(*rpy))
            
    #        pt  = V + C_rpy2enu.dot(dV)
    #        print '1', pt
    #        if np.all(np.isclose(pt , goodresult)):
    #            print 'good1' , i
            
            pt2 = V + C_rpy2enu.dot(geok.C_ned2enu().dot(dV))
            if np.all(np.isclose(pt2 , goodresult)):        
                print('good2' , i , koef , rpy ,rpyorder)
                stkgood.append(i)
            
            
    print(V , dV)


# === Parite de Validation
if 0:
    PI1 = np.arange(0,2*np.pi,0.6)
    PI = (np.pi/2 , np.pi , 3 * np.pi / 2) + tuple(PI1[0:3])
    
    for pp in PI:
        V  = [np.cos(pp),np.sin(pp),0]
        dV = geok.add_offset(V,([0,0.1,0]))
        
        plt.plot( V[0],V[1],'ob')
        plt.plot( [0,V[0]],[0,V[1]],'-b')
    
        plt.plot(dV[0],dV[1],'or')
    
    plt.axis('equal')
    
# 
    
