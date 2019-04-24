

import glob
import geoclass as gcls
import geodetik as geok

import matplotlib.pyplot as plt


p = "/home/chup01/software/GINS/gin/batch/solution/*IPPP"
L = sorted(glob.glob(p))



ts_stack = []

for f in L:
    print(f)
    ts = gcls.read_gins_solution(f)
    ts_stack.append(ts)

tsout = gcls.merge_ts(ts_stack)

tsout.ENUcalc_from_mean_posi()


import datetime as dt

#tsout.plot("ENU")

start ,end = dt.datetime(2016,1,17,11) , dt.datetime(2016,1,17,13)

tsout2 = gcls.time_win(tsout,[[start,end]])

#plt.figure()
tsout2.plot("FLH")

F,L,H,T,sF,sL,sH = tsout2.to_list("FLH")

F,L,H,T,sF,sL,sH = tsout.to_list("FLH")


plt.plot(geok.posix2dt(T),H)

p = "/home/chup01/software/GINS/gin/batch/solution/sessions_longues/DIR_KALMAN0_CNGH_24122_a.yml.190213_152649.190213_153136.gins.PPP"
ts_long = gcls.read_gins_solution(p)
F,L,H,T,sF,sL,sH = ts_long.to_list("FLH")
plt.plot(geok.posix2dt(T),H)


#plt.show()
#plt.savefig("/home/chup01/aaaa.png")