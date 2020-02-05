#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:56:12 2020

@author: dewiballard
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import seaborn as sns

df = pd.read_csv('Consolidated_data.csv')

samples = ['RA', 'IAA']
electro =[]

for system in samples:
    grouped = df.groupby('sample').get_group(system)
    print(grouped['sample'], grouped['electro'].mean())