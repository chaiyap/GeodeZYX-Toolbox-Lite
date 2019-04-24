#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 15:09:23 2018

@author: psakicki

Range selection of a time serie => not implemented operationnaly for the moment !!!! (1807)
"""

from megalib import *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:52:02 2018

@author: psakicki
"""

from megalib import *

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from matplotlib.widgets import Button

class ButtonClass(object):
    ind = 0
    
    def __init__(self,onselect_obj):
        self.onselect_obj = onselect_obj 
        
    def button_dummy(self , event):
        print("DUMMY")
        return None

    def button_valid(self, event):
        self.onselect_obj.validate()
        return None

    def button_finish(self, event):
        self.onselect_obj.final_selection() 
        plt.close(self.onselect_obj.fig)

        return None

class Onselect():

    def __init__(self,xinp,yinp):
        
        #The input values
        self.xinp   = xinp
        self.yinp   = yinp

        # Vals of a temporary selection
        self.xtmp   = None
        self.ytmp   = None
        self.indtmp = None
        
        # Stacking of the validated vals
        self.X      = []
        self.Y      = []
        self.Ind    = []

        # Stacked validated values for export
        self.Xstk   = np.array([])
        self.Ystk   = np.array([])
        self.Indstk = np.array([])
        
        self.fig_init()

    def __call__(self, xmin, xmax):
        
        x  = self.xinp
        y  = self.yinp
        
        indmin, indmax = np.searchsorted(x, (xmin, xmax))
        indmax = min(len(x)-1, indmax)

        thisx = x[indmin:indmax]
        thisy = y[indmin:indmax]
        
        self.xtmp   = thisx
        self.ytmp   = thisy
        self.indtmp = list(range(indmin,indmax))

        print("INFO : ",len(self.xtmp),"elts selected, waiting for validation")
                
        self.line2.set_data(thisx, thisy)
        self.ax2.set_xlim(thisx[0], thisx[-1])
        self.ax2.set_ylim(thisy.min(), thisy.max())
        self.fig.canvas.draw()
        
        return 42
        
    def fig_init(self):
        
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, figsize=(8, 6))
        self.ax1.set(facecolor='#FFFFCC')

        self.ax1.plot(self.xinp, self.yinp, '-')
        self.ax1.set_ylim(-2, 2)
        self.ax1.set_title('Press left mouse button and drag to test')
    
        self.ax2.set(facecolor='#FFFFCC')
        self.line2, = self.ax2.plot(self.xinp, self.yinp, '-')    
        
        
    def validate(self):
        
        self.X.append(self.xtmp)
        self.Y.append(self.ytmp)
        self.Ind.append(self.indtmp)
        
        print("INFO : ",len(self.indtmp),"elts added to the valid selection")


        self.xtmp   = None
        self.ytmp   = None
        self.indtmp = None        
        
    
    def final_selection(self):

        if len(self.X) > 0:
            self.Xstk   = np.hstack(self.X)
            self.Ystk   = np.hstack(self.Y)
            self.Indstk = np.hstack(self.Ind)
                
        return  self.Xstk , self.Ystk , self.Indstk
    

#def tralala():
#    # Fixing random state for reproducibility
#    np.random.seed(19680801)
#
#    x = np.arange(0.0, 5.0, 0.01)
#    y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))
#        
#    
#    onselect = Onselect(x,y)
#    callback = ButtonClass(onselect)
#
#    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))
#    ax1.set(facecolor='#FFFFCC')
#    
#    ax1.plot(x, y, '-')
#    ax1.set_ylim(-2, 2)
#    ax1.set_title('Press left mouse button and drag to test')
#    
#    ax2.set(facecolor='#FFFFCC')
#    line2, = ax2.plot(x, y, '-')
#           
#    
#    # set useblit True on gtkagg for enhanced performance
#    span = SpanSelector(ax1, onselect, 'horizontal', useblit=True,
#                        rectprops=dict(alpha=0.5, facecolor='red') , 
#                        span_stays=True)
#    
#    
#    axprev = plt.axes([0.7 , 0.05, 0.1, 0.075])
#    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
#    bnext = Button(axnext, 'Finish')
#    bnext.on_clicked(callback.button_finish)
#    bprev = Button(axprev, 'Valid. Sel.')
#    bprev.on_clicked(callback.button_valid)
#    
#        
#    return onselect.final_selection() , callback , onselect , bnext , bprev



def handler(*args, **kwargs):
    print('handled')

def testfn():
    
    np.random.seed(19680801)
    
    x = np.arange(0.0, 5.0, 0.01)
    y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))
    

    onselect = Onselect(x,y)
    callback = ButtonClass(onselect)
    
    
    span = SpanSelector(onselect.ax1, onselect, 'horizontal', useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red') , 
                    span_stays=True)
    
    
    b1 = Button(onselect.fig.add_axes([0.4, 0.3, 0.1, 0.04]), 'Click!')
    #b1.on_clicked(handler)
    b1.on_clicked(callback.button_dummy)
    axprev = plt.axes([0.7 , 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    b_finish = Button(axnext, 'Finish')
    b_finish.on_clicked(callback.button_finish)
    b_valid = Button(axprev, 'Valid. Sel.')
    b_valid.on_clicked(callback.button_valid)
    
    
    return b1 , b_valid , b_finish , onselect , span

button = testfn()

plt.show()
