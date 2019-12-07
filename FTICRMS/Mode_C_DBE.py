#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:08:19 2019

@author: dewiballard
"""

# library
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

colnames = ['cnumber', 'dbe', 'abund']
data = pd.read_csv('C_DBE_Abundance.csv', names=colnames)

X = np.array(data.cnumber.tolist())
Y = np.array(data.dbe.tolist())
Z = np.array(data.abund.tolist())

####### DBE plot #######
#c = np.abs(Z)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#cmhot = plt.get_cmap("hot")
#cax = ax.scatter(X, Y, Z, s=5, c=c, cmap=cmhot)
#ax.view_init(azim=-90, elev=90)
#plt.show()

matrix = np.transpose([X, Y, Z])

dfX = pd.DataFrame(matrix, columns = ["First Col", "Second Col", "Third Col"])
dfX = dfX.drop(columns=['Second Col'])
groupedbyX = dfX.groupby("First Col").sum()

dfY = pd.DataFrame(matrix, columns = ["First Col", "Second Col", "Third Col"])
dfY = dfY.drop(columns=['First Col'])
groupedbyY = dfY.groupby("Second Col").sum()

carbonnumber = groupedbyX['Third Col'].idxmax()
dbe = groupedbyY['Third Col'].idxmax()

print('The mode of Carbon number is', carbonnumber, '. The mode of DBE is ', dbe,'.')