#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np


SP = 100  # setpoint (target)
PV = 0  # process value (what is being controlled)
time = 20

Kp = 0.4
Ki = 0.4
Kd = 0.4


summation = 0
lastET = SP - PV

xpoints = list(np.arange(1, time+1))  # time
ypoints = np.array([])
test = []


def proportional(SP, Kp, PV):
    return (Kp * (SP - PV))


def integral(SP, Ki, PV, summation):
    return Ki * summation

# def summate(SP, PV, summation):
#     et = (SP - PV) # error
#     dt = (1/time) # cycle time???
#     summation += et * dt
#     return summation


def derivative(SP, Kd, PV, lastEt):
    et = (SP - PV)  # current error
    etDELTA = et - lastEt
    dt = (1/time)
    # print(et, etDELTA, dt)
    return Kd * (etDELTA / dt)


def output(P, I, D):
    return P+I+D+SP


for i in range(time):
    lastET = (SP - PV)
    ypoints = np.append(ypoints, PV)
    test.append(PV)
    # summation = summate(SP, PV, summation)
    PV = output(
        proportional(SP, Kp, PV),
        integral(SP, Ki, PV, summation),
        derivative(SP, Kd, PV, lastET)
    )


print("-------------------------")
print(test)
plt.plot(xpoints, ypoints)
plt.show()
