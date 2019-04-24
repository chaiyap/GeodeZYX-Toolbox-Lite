"""
This function is the alpha test version
NOT USEFUL FOR OPERATIONAL

Simple Selection of the X component by clicking on the plot
Implemented operationally for times series

See renag_synthetic_series or for more details
for the TimeSerie method ts.discont_manu_click(fig)
or
LAST2018_2_create_SSP_Temp_n_ColdWater_afined_extraction.py
for the generic function 
PnC           = gcls.point_n_click_plot()
multi , cid   = PnC(fig=1)
selectedX_out = sorted(PnC.selectedX)
"""



import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import Cursor




# https://stackoverflow.com/questions/25521120/store-mouse-click-event-coordinates-with-matplotlib

x = np.arange(-10,10)
y = x**2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)

coords = []

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print(ix)

    global coords
    coords.append(ix)
    
    return coords

# Fixing random state for reproducibility
np.random.seed(19680801)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, facecolor='#FFFFCC')

x, y = 4*(np.random.rand(2, 100) - .5)
ax.plot(x, y, 'o')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# set useblit = True on gtkagg for enhanced performance
cursor = Cursor(ax, useblit=True, color='red', linewidth=2 , horizOn=0)
cid = fig.canvas.mpl_connect('button_press_event', onclick)