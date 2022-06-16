#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage of `yield` and generators in Python to create a 2-way communication loop

import matplotlib.pyplot as plt
import numpy as np
import math

# PID controller for a AC heating system


SP = 100 # setpoint (target)
PV = 0 # process value (what is being controlled)
time = 50

Kp = 0.7
Ki = 0.8
Kd = 0


summation = 0

xpoints = list(np.arange(1, time+1)) # time
ypoints = np.array([])
test = []

def proportional(SP, Kp, PV):
    return (Kp * (SP - PV))

def integral(SP, Ki, PV, summation):
    et = (SP - PV) # error
    dt = (1/time) # cycle time???
    summation += et * dt
    return Ki * summation

def derivative(SP, Kd, PV):
    return 0


def output(P, I, D):
    return P+I+D+SP

for i in range(time):
    PV = output(proportional(SP, Kp, PV), integral(SP, Ki, PV, summation), derivative(SP, Kd, PV)) 
    summation = integral(SP, Ki, PV, summation)
    
    ypoints = np.append(ypoints, PV)
    test.append(PV)
    print(summation)


print("-------------------------")
print(test)
plt.plot(xpoints, ypoints)
plt.show()
