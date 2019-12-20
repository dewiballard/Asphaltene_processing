#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:48:06 2019

@author: dewiballard
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import math

data = open('IAA_fovern_overtone3.csv', 'r')

SAMPLE = 'IAA 0.1 g/L'

####################  Plot raw f/n with time #################
def runningmean(x, N):
    return np.convolve(x, np.ones((N,))/N)[(N-1):]

xaxis = []
yaxisuntreated = []

for line in data:
    a, b = line.split(',')
    xaxis.append(float(a))
    yaxisuntreated.append(float(b))

yaxis = runningmean(yaxisuntreated,1)

plt.figure()
plt.plot(xaxis, yaxis)
plt.ylabel('delta f/n (Hz)')
plt.xlabel('Time (mins)')
plt.xlim(0,1000)
plt.legend((SAMPLE,),loc='upper right')

############## Convert raw data to mass adsorbed #############
for i in yaxis:
    frequencyshift = yaxis
    Sauerbreys = (-1*frequencyshift*math.sqrt(2648*2.947E10))/(2*(4.96E6)*(4.96E6))
    unitchange = Sauerbreys * 1E6

plt.figure()
plt.plot(xaxis, unitchange)
plt.ylabel('Mass adsorbed (mg/m2)')
plt.xlabel('Time (mins)')
plt.xlim(0,1000)
plt.legend((SAMPLE,),loc='upper right')


######## Fitting natural exponent curve to the QCM data #############

#data to be fitted
xdata = np.array(xaxis)
ydata = np.array(unitchange)

def fit(x, a, b, c):
    return -a * np.exp(-b * x) + c

variables = np.array([2.26813118e+01, 2.82179384e-03, 2.48165285e+01]) #copy values from printed ones above outputted figure
#this next line will print out the fitted values for a b and c
print(scipy.optimize.curve_fit(fit, xdata, ydata, variables))
plt.plot(xdata, fit(xdata, *variables), 'r--')

############# Code to calculate mg/m2 at 1000 min #############

A = variables[0]
B = variables[1]
C = variables[2]

mass_adsorbed = -A * np.exp(-B * 1000) + C
print(mass_adsorbed, 'mg/m2 at equilibrium.')

report = open('Report.txt', 'w')
report.write('Sample is ')
report.write(str(SAMPLE))
report.write('\n')
report.write('\n')
report.write(str(mass_adsorbed))
report.write(' mg/m2 at equilibrium.')
report.write('\n')
report.write('where A is: ')
report.write(str(A))
report.write('\n')
report.write('where B is: ')
report.write(str(B))
report.write('\n')
report.write('where C is: ')
report.write(str(C))
report.write('in -a * np.exp(-b * x) + c')
report.write('\n')
report.write('\n')
report.write('Data for plotting is:')
report.write('\n')
report.write('\n')
for line in xdata:
    report.write(str(line))
    report.write('\n')
report.write('\n')
report.write('\n')
for line in ydata:
    report.write(str(line))
    report.write('\n')
