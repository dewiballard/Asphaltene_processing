#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:15:20 2020

@author: dewiballard
"""

# Code to compile all the Output_XX_XX.csv files to an Output.csv file

import os

csv_header = '0,sample,group,vdW,hbond,electro,total'
csv_out = 'Consolidated_data.csv'

csv_dir = os.getcwd()

dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
   pass

csv_list = []
for file in filenames:
   if file.endswith('.csv'):
      csv_list.append(file)

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header)
csv_merge.write('\n')

for file in csv_list:
   csv_in = open(file)
   for line in csv_in:
       if line.startswith(csv_header):
           continue
       else:
          csv_merge.write(line)
   
   csv_in.close()

csv_merge.close()

print('Verify consolidated CSV file : ' + csv_out)