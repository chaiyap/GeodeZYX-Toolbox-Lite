#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:55:41 2018

@author: psakicki
"""

from megalib import *



###### Manual Selection of values
X = np.arange(100)
Y = np.random.rand(100)

plt.plot(X,Y)

F = plt.gcf()

PnC = gcls.point_n_click_plot()
PnC(F,False)


X = np.arange(100)
Y = np.random.rand(100)

#%%
import geodetik as geok

plt.clf()

## Generation of a Time Series
N = 1000
X = np.arange(N)
Y = np.arange(N)

## Noise and add outliers in the Time Series
Ynoise    =  np.random.randn(N) * 100
Youtlier1 =  np.random.randn(N) 
Youtlier1_bool = np.abs(Youtlier1) > 2.
Youtlier2  =  np.zeros(N)
Youtlier2[Youtlier1_bool] = Youtlier1[Youtlier1_bool] * 200
Y = Y + Ynoise + Youtlier2

## Plot it 
plt.plot(X,Y,"x")

## Find the outliers 
if 0:
    mad_threshold = 3
    Ynew , Xnew = geok.outlier_mad_binom(Y,X,mad_threshold,
                                         detrend_first=True)
    plt.plot(Xnew,Ynew,"+")
