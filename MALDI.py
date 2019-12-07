#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:11:21 2019

@author: dewiballard
"""

import xlrd

loc = ('/Users/dewiballard/Downloads/MALDIresults.xlsx')

def Average(lst1, lst2): 
    return sum(lst1) / sum(lst2) 

maldi = xlrd.open_workbook(loc) 
sheet = maldi.sheet_by_index(0) 
sheet.cell_value(0, 0) 

average_up_to_1000 = []

for i in range(sheet.nrows):
    if sheet.cell_value(i, 26) <= 1000:
        average_up_to_1000.append(sheet.cell_value(i, 21))

number_of_data_points = len(average_up_to_1000)

peak_heights = []

for i in range(1, number_of_data_points):
    peak_heights.append(sheet.cell_value(i, 27))

peaks = [a*b for a,b in zip(average_up_to_1000,peak_heights)]

print(Average(peaks, peak_heights))

#multiply those values together 