# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 22:33:22 2022

@author: nightlan1015297
"""

import matplotlib.pyplot as plt
import math

# constants
sun_mass = 1.989e30
G = 6.67e-11
orbit_period = 60*60*24*365.25
dt = 60
step = int(orbit_period/dt) 

# define a function to calculate the magnitude of acceleration
def acc(r_square):
    if r_square == 0:
        return 0
    return G*sun_mass/r_square

# define initial value and initialize lists to storage data
initial_x = 1.47e11
initial_y = 0
initial_vx = 0
initial_vy = 3.03e4
x = [initial_x]
y = [initial_y]
vx = [initial_vx]
vy = [initial_vy]

# calculate orbit
for i in range(step):
    r_square = x[i]**2+y[i]**2
    a = acc(r_square)
    r = math.sqrt(r_square)
    # calculate the acceleration in different axis
    ax = -a * x[i]/r
    ay = -a * y[i]/r
    # Euler method
    vx.append(vx[i] + ax*dt)
    vy.append(vy[i] + ay*dt)
    x.append(x[i] + vx[i]*dt)
    y.append(y[i] + vy[i]*dt)

# plot the graph 

plt.plot(x,y)
plt.xlabel("x (unit : meter)")
plt.ylabel("y (unit : meter)")
plt.show()
