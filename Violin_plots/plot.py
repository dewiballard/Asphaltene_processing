#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:32:43 2020

@author: dewiballard
"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import seaborn as sns

df = pd.read_csv('Consolidated_data.csv')

order = ["HC", "Nx / NxOy", "Ox", "OxSy", "Sx"]
hue_order = ["RA", "IAA"]

def new_hue(x):
    if 'R' in str(x):
        return ["IAA", "RA"]
    else:
        return ["RA", "IAA"]

g = plt.subplots(figsize=(15,10))

#for system1 in order:
#    for system2 in hue_order:
#        grouped1 = df.groupby('group').get_group(system1)
#        grouped2 = df.groupby('sample').get_group(system2)
#        grouped = pd.merge(grouped1, grouped2)
#        fig = sns.violinplot(x=grouped['group'], y=grouped['total'], hue=df['sample'], order=order, hue_order=hue_order, split=True, width=grouped['vdW'].mean()+grouped['electro'].mean()+grouped['hbond'].mean(), inner=None, palette=['blue','blue'])
#        fig = sns.violinplot(x=grouped['group'], y=grouped['total'], hue=df['sample'], order=order, hue_order=hue_order, split=True, width=grouped['electro'].mean()+grouped['hbond'].mean(), inner=None, palette=['yellow','yellow'])
#        fig = sns.violinplot(x=grouped['group'], y=grouped['total'], hue=df['sample'], order=order, hue_order=hue_order, split=True, width=grouped['hbond'].mean(), inner=None, palette=['red','red'])

for system1 in order:
    for system2 in hue_order:
        grouped1 = df.groupby('group').get_group(system1)
        grouped2 = df.groupby('sample').get_group(system2)
        grouped = pd.merge(grouped1, grouped2)
#        if df['sample'] = 'RA':
#            new_hue_order = ["IAA", "RA"]
#        else:
#            new_hue_order = ["RA", "IAA"]
        fig = sns.violinplot(x=grouped['group'], y=grouped['total'], hue=df['sample'], order=order, hue_order=new_hue(grouped['sample']), split=True, width=grouped['vdW'].mean()+grouped['electro'].mean()+grouped['hbond'].mean(), inner=None, palette=['blue','blue'])
        fig = sns.violinplot(x=grouped['group'], y=grouped['total'], hue=df['sample'], order=order, hue_order=new_hue(grouped['sample']), split=True, width=grouped['electro'].mean()+grouped['hbond'].mean(), inner=None, palette=['yellow','yellow'])
        fig = sns.violinplot(x=grouped['group'], y=grouped['total'], hue=df['sample'], order=order, hue_order=new_hue(grouped['sample']), split=True, width=grouped['hbond'].mean(), inner=None, palette=['red','red'])

#fig = sns.violinplot(x=df['group'], y=df['total'], hue=df['sample'],order=order,  split=True, width=1, inner=None, palette=['blue','red'])
fig.set_title('Interactions with itself', fontsize=20)

fig.set_xlabel('Heteroatom group', fontsize=20)

fig.set_ylabel('Interaction energy (kcal/mol)', fontsize=20)

custom_legend = [Line2D([0], [0], color="blue", lw=4), Line2D([0], [0], color="yellow", lw=4), Line2D([0], [0], color="red", lw=4)]

fig.legend(custom_legend, ['van der Waals', 'Electrostatic', 'Hydrogen bonding'], loc='lower left')

plt.savefig('out.png')

plt.show()