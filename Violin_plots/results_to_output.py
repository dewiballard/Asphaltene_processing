#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:51:40 2020

@author: dewiballard
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

n_points = 1000
################## Make arrays with only necessary columns ###################

vdW = []
hb = []
elec = []
tot = []

with open('results.dat','r') as file:
    for line in file:
        vdW_att = line[84:91]
        vdW_rep = line[98:105]
        hbond_att = line[111:117]
        hbond_rep = line[124:130]
        electro = line[137:143]
        total_vdW = round(float(vdW_att) + float(vdW_rep), 3)
        total_hbond = round(float(hbond_att) + float(hbond_rep), 3)
        total_electro = round(float(electro), 3)
        total = round(float(vdW_att) + float(vdW_rep) + float(hbond_att) + float(hbond_rep) + float(electro), 3)
        vdW.append(total_vdW)
        hb.append(total_hbond)
        elec.append(total_electro)
        tot.append(total)

############################# Sort in order of total ##########################

data_hori = np.vstack((vdW, hb, elec, tot))
data = data_hori.T

idx = np.argsort(data_hori[3:])

sorted_data_nested = data[idx]
sorted_data = sorted_data_nested[0]

top_thousand = sorted_data[0:n_points]

################## Export document with the necessary data #####################

vdW_total = top_thousand[0]

with open('Output.csv','w') as file:

    x = 0
    file.write('0,sample,group,vdW,hbond,electro,total\n')
    
    for i in range(0,n_points):
        x = x + 1
        data_point = top_thousand[i]
        if data_point[0] > data_point[3]:
            if data_point[0] < 0:
                vdW_contribution = data_point[0]/data_point[3]
            else:
                vdW_contribution = 0
        else:
            vdW_contribution = 1
        if data_point[1] > data_point[3]:
            if data_point[1] < 0:
                hbond_contribution = data_point[1]/data_point[3]
            else:
                hbond_contribution = 0
        else:
            hbond_contribution = 1
        if data_point[2] > data_point[3]:
            if data_point[2] < 0:
                electro_contribution = data_point[2]/data_point[3]
            else:
                electro_contribution = 0
        else:
            electro_contribution = 1
        total_interaction = data_point[3]
        file.write(str(x) + ',' + 'IAA'+ ',' + 'Sx' + ',' + str(vdW_contribution) + ',' + str(hbond_contribution)+ ',' + str(electro_contribution) + ',' + str(total_interaction) + '\n')







