#  Prerequisites

# virtualenv -p python3 plc && . plc/bin/activate
#    pip install matplotlib
#    pip install numpy

#  Runner
#  python3 testpolice.py

import matplotlib.pyplot as plot
import numpy as np
DT = 22
T0 = 0
Tf = 30
dt = (Tf-T0)/DT
T = np.linspace(T0, Tf, DT)

# Speeder
vs = 36   #  m/sc
xs_0 = 0    #  m

xs = np.linspace(T0, Tf, DT)
xs[0]= xs_0
indx = 0
for i in range(1,DT):
    xs[i] = xs[i-1] + vs*dt

plot.plot(T,xs, label='speeder')


#police
vp_0 = 0    #  m/s
xp_0 = 0    #  m
a = 3     #  m/s2

vp = np.linspace(T0, Tf, DT)
xp = np.linspace(T0, Tf, DT)
xp[0]= xp_0
vp[0]= vp_0
for i in range(1,DT):
    vp[i] = vp[i-1] + a*dt
    xp[i] = xp[i-1]+ vp[i]*dt
plot.plot(T,xp, label='police')


print(T)
print(xs)
print(vp)
print(xp)


plot.savefig('police.png')
