#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:26:05 2020

@author: dewiballard
"""

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
   
df = pd.read_csv('scaled_data.csv')

order = ["HC", "Nx / NxOy", "Ox", "OxSy", "Sx"]
hue_order = ["RA", "IAA"]

g = plt.subplots(figsize=(15,10))

for system in hue_order:

    grouped = df.groupby('sample').get_group(system)

    fig = sns.violinplot(x=grouped['sample'], y=grouped['total'], hue=df['sample'],hue_order=hue_order,  split=True, width=1, inner=None, palette=['blue','blue'])

    fig = sns.violinplot(x=grouped['sample'], y=grouped['total'], hue=df['sample'],hue_order=hue_order, split=True, width=grouped['electro'].mean(), inner=None, palette=['yellow','yellow'])

    fig = sns.violinplot(x=grouped['sample'], y=grouped['total'], hue=df['sample'],hue_order=hue_order,  split=True, width=grouped['hbond'].mean(), inner=None, palette=['red','red'])

 

fig.set(title='Interactions with itself')

fig.set(xlabel= '')#, ylabel='Interaction energy (kcal/mol)')

fig.set_ylabel('Interaction energy (kcal/mol)', fontsize=16)

custom_legend = [Line2D([0], [0], color="blue", lw=4), Line2D([0], [0], color="yellow", lw=4), Line2D([0], [0], color="red", lw=4)]

fig.legend(custom_legend, ['van der Waals', 'Electrostatic', 'Hydrogen bonding'], loc='lower left')

plt.savefig('out.png')

plt.show()