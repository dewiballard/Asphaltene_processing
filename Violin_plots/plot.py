#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:32:43 2020

@author: dewiballard
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('Output.csv')

#histogram of the interaction values total and from vdW

vdW_width = df['vdW'][:10].mean()
electro_width = df['electro'].mean()
hbond_width = df['hbond'].mean()

fig = sns.violinplot(x=df['sample'], y=df['total'], width=vdW_width, inner=None, color="blue")
fig = sns.violinplot(x=df['sample'], y=df['total'], width=electro_width, inner=None, color="yellow")
fig = sns.violinplot(x=df['sample'], y=df['total'], width=hbond_width, inner=None, color="red")
fig.set(xlabel= '', ylabel='Interaction energy (kcal/mol)')
plt.ylim(-10, 0)
plt.savefig('out.png')
plt.show()

#hue=df_RA['sample'], split=True.... width factor doesn't work!