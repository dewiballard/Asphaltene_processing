#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:40:27 2020

@author: dewiballard
"""

import os

csv_header = '0,sample,group,vdW,hbond,electro,total'
csv_out = 'Scaled_data.csv'

tot1 = (32+11+13+12+23)
RA_HC = round((32/tot1)*100)
RA_Nx = round((11/tot1)*100)
RA_Ox = round((13/tot1)*100)
RA_OxSy = round((12/tot1)*100)
RA_Sx = round((23/tot1)*100)

tot2 = (22+8+27+25+11)
IAA_HC = round((22/tot2)*100)
IAA_NxOy = round((8/tot2)*100)
IAA_Ox = round((27/tot2)*100)
IAA_OxSy = round((25/tot2)*100)
IAA_Sx = round((11/tot2)*100)

csv_dir = os.getcwd()

dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
   pass

csv_list = []
for file in filenames:
   if file.endswith('data.csv'):
      csv_list.append(file)

csv_processed = open(csv_out, 'w')
csv_processed.write(csv_header)
csv_processed.write('\n')

for file in csv_list:
   csv_in = open(file)
   for line in csv_in:
       if line.startswith(csv_header):
           continue
       if 'R' in line:
           if 'HC' in line:
               for i in range(RA_HC):
                   csv_processed.write(line)
           if 'Nx' in line:
               for i in range(RA_Nx):
                   csv_processed.write(line)
           if 'Ox,' in line:
               for i in range(RA_Ox):
                   csv_processed.write(line)
           if 'OxSy' in line:
               for i in range(RA_OxSy):
                   csv_processed.write(line)
           if 'Sx' in line:
               for i in range(RA_Sx):
                   csv_processed.write(line)
       elif 'I' in line:
           if 'HC' in line:
               for i in range(IAA_HC):
                   csv_processed.write(line)
           if 'Nx' in line:
               for i in range(IAA_NxOy):
                   csv_processed.write(line)
           if 'Ox,' in line:
               for i in range(IAA_Ox):
                   csv_processed.write(line)
           if 'OxSy' in line:
               for i in range(IAA_OxSy):
                   csv_processed.write(line)
           if 'Sx' in line:
               for i in range(IAA_Sx):
                   csv_processed.write(line)
       else:
          pass
   
   csv_in.close()

csv_processed.close()
