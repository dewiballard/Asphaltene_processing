#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:40:27 2020

@author: dewiballard
"""

import os

csv_header = '0,sample,group,group2,vdW,hbond,electro,total'
csv_out = 'Scaled_data.csv'

tot1 = (32+11+13+12+23)
RA_HC = (32/tot1)*100
RA_Nx = (11/tot1)*100
RA_Ox = (13/tot1)*100
RA_OxSy = (12/tot1)*100
RA_Sx = (23/tot1)*100

tot2 = (22+8+27+25+11)
IAA_HC = (22/tot2)*100
IAA_NxOy = (8/tot2)*100
IAA_Ox = (27/tot2)*100
IAA_OxSy = (25/tot2)*100
IAA_Sx = (11/tot2)*100

RA_HC_HC = (RA_HC/100)*(RA_HC/100)
RA_HC_Nx = (RA_HC/100)*(RA_Nx/100)
RA_HC_Ox = (RA_HC/100)*(RA_Ox/100)
RA_HC_OxSy = (RA_HC/100)*(RA_OxSy/100)
RA_HC_Sx = (RA_HC/100)*(RA_Sx/100)
RA_Nx_Nx = (RA_Nx/100)*(RA_Nx/100)
RA_Nx_Ox = (RA_Nx/100)*(RA_Ox/100)
RA_Nx_OxSy = (RA_Nx/100)*(RA_OxSy/100)
RA_Nx_Sx = (RA_Nx/100)*(RA_Sx/100)
RA_Ox_Ox = (RA_Ox/100)*(RA_Ox/100)
RA_Ox_OxSy = (RA_Ox/100)*(RA_OxSy/100)
RA_Ox_Sx = (RA_Ox/100)*(RA_Sx/100)
RA_OxSy_OxSy = (RA_OxSy/100)*(RA_OxSy/100)
RA_OxSy_Sx = (RA_OxSy/100)*(RA_Sx/100)
RA_Sx_Sx = (RA_Sx/100)*(RA_Sx/100)

IAA_HC_HC = (IAA_HC/100)*(IAA_HC/100)
IAA_HC_NxOy = (IAA_HC/100)*(IAA_NxOy/100)
IAA_HC_Ox = (IAA_HC/100)*(IAA_Ox/100)
IAA_HC_OxSy = (IAA_HC/100)*(IAA_OxSy/100)
IAA_HC_Sx = (IAA_HC/100)*(IAA_Sx/100)
IAA_NxOy_NxOy = (IAA_NxOy/100)*(IAA_NxOy/100)
IAA_NxOy_Ox = (IAA_NxOy/100)*(IAA_Ox/100)
IAA_NxOy_OxSy = (IAA_NxOy/100)*(IAA_OxSy/100)
IAA_NxOy_Sx = (IAA_NxOy/100)*(IAA_Sx/100)
IAA_Ox_Ox = (IAA_Ox/100)*(IAA_Ox/100)
IAA_Ox_OxSy = (IAA_Ox/100)*(IAA_OxSy/100)
IAA_Ox_Sx = (IAA_Ox/100)*(IAA_Sx/100)
IAA_OxSy_OxSy = (IAA_OxSy/100)*(IAA_OxSy/100)
IAA_OxSy_Sx = (IAA_OxSy/100)*(IAA_Sx/100)
IAA_Sx_Sx = (IAA_Sx/100)*(IAA_Sx/100)

scaling_factor_RA = RA_HC_HC+RA_HC_Nx+RA_HC_Ox+RA_HC_OxSy+RA_HC_Sx+RA_Nx_Nx+RA_Nx_Ox+RA_Nx_OxSy+RA_Nx_Sx+RA_Ox_Ox+RA_Ox_OxSy+RA_Ox_Sx+RA_OxSy_OxSy+RA_OxSy_Sx+RA_Sx_Sx
scaling_factor_IAA = IAA_HC_HC+IAA_HC_NxOy+IAA_HC_Ox+IAA_HC_OxSy+IAA_HC_Sx+IAA_NxOy_NxOy+IAA_NxOy_Ox+IAA_NxOy_OxSy+IAA_NxOy_Sx+IAA_Ox_Ox+IAA_Ox_OxSy+IAA_Ox_Sx+IAA_OxSy_OxSy+IAA_OxSy_Sx+IAA_Sx_Sx

RA_HC_HC_scaled = (RA_HC_HC*100)/scaling_factor_IAA
RA_HC_Nx_scaled = (RA_HC_Nx*100)/scaling_factor_IAA
RA_HC_Ox_scaled = (RA_HC_Ox*100)/scaling_factor_IAA
RA_HC_OxSy_scaled = (RA_HC_OxSy*100)/scaling_factor_IAA
RA_HC_Sx_scaled = (RA_HC_Sx*100)/scaling_factor_IAA
RA_Nx_Nx_scaled = (RA_Nx_Nx*100)/scaling_factor_IAA
RA_Nx_Ox_scaled = (RA_Nx_Ox*100)/scaling_factor_IAA
RA_Nx_OxSy_scaled = (RA_Nx_OxSy*100)/scaling_factor_IAA
RA_Nx_Sx_scaled = (RA_Nx_Sx*100)/scaling_factor_IAA
RA_Ox_Ox_scaled = (RA_Ox_Ox*100)/scaling_factor_IAA
RA_Ox_OxSy_scaled = (RA_Ox_OxSy*100)/scaling_factor_IAA
RA_Ox_Sx_scaled = (RA_Ox_Sx*100)/scaling_factor_IAA
RA_OxSy_OxSy_scaled = (RA_OxSy_OxSy*100)/scaling_factor_IAA
RA_OxSy_Sx_scaled = (RA_OxSy_Sx*100)/scaling_factor_IAA
RA_Sx_Sx_scaled = (RA_Sx_Sx*100)/scaling_factor_IAA

IAA_HC_HC_scaled = (IAA_HC_HC*100)/scaling_factor_IAA
IAA_HC_NxOy_scaled = (IAA_HC_NxOy*100)/scaling_factor_IAA
IAA_HC_Ox_scaled = (IAA_HC_Ox*100)/scaling_factor_IAA
IAA_HC_OxSy_scaled = (IAA_HC_OxSy*100)/scaling_factor_IAA
IAA_HC_Sx_scaled = (IAA_HC_Sx*100)/scaling_factor_IAA
IAA_NxOy_NxOy_scaled = (IAA_NxOy_NxOy*100)/scaling_factor_IAA
IAA_NxOy_Ox_scaled = (IAA_NxOy_Ox*100)/scaling_factor_IAA
IAA_NxOy_OxSy_scaled = (IAA_NxOy_OxSy*100)/scaling_factor_IAA
IAA_NxOy_Sx_scaled = (IAA_NxOy_Sx*100)/scaling_factor_IAA
IAA_Ox_Ox_scaled = (IAA_Ox_Ox*100)/scaling_factor_IAA
IAA_Ox_OxSy_scaled = (IAA_Ox_OxSy*100)/scaling_factor_IAA
IAA_Ox_Sx_scaled = (IAA_Ox_Sx*100)/scaling_factor_IAA
IAA_OxSy_OxSy_scaled = (IAA_OxSy_OxSy*100)/scaling_factor_IAA
IAA_OxSy_Sx_scaled = (IAA_OxSy_Sx*100)/scaling_factor_IAA
IAA_Sx_Sx_scaled = (IAA_Sx_Sx*100)/scaling_factor_IAA

#####################################################################

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
               if 'HC, HC' in line:
                   for i in range(round(RA_HC_HC_scaled)):
                       csv_processed.write(line)
               if 'Nx / NxOy' in line:
                   for i in range(round(RA_HC_Nx_scaled)):
                       csv_processed.write(line)
               if 'Ox' in line:
                   for i in range(round(RA_HC_Ox_scaled)):
                       csv_processed.write(line)
               if 'OxSy' in line:
                   for i in range(round(RA_HC_OxSy_scaled)):
                       csv_processed.write(line)
               if 'Sx' in line:
                   for i in range(round(RA_HC_Sx_scaled)):
                       csv_processed.write(line)
               else:
                    pass                       
           if 'Nx / NxOy' in line:
               if 'Nx / NxOy, Nx / NxOy' in line:
                   for i in range(round(RA_Nx_Nx_scaled)):
                       csv_processed.write(line)
               if 'Ox' in line:
                   for i in range(round(RA_Nx_Ox_scaled)):
                       csv_processed.write(line)
               if 'OxSy' in line:
                   for i in range(round(RA_Nx_OxSy_scaled)):
                       csv_processed.write(line)
               if 'Sx' in line:
                   for i in range(round(RA_Nx_Sx_scaled)):
                       csv_processed.write(line)
               else:
                    pass                       
           if 'Ox,' in line:
               if 'Ox, Ox' in line:
                   for i in range(round(RA_Ox_Ox_scaled)):
                       csv_processed.write(line)
               if 'OxSy' in line:
                   for i in range(round(RA_Ox_OxSy_scaled)):
                       csv_processed.write(line)   
               if 'Sx' in line:
                   for i in range(round(RA_Ox_Sx_scaled)):
                       csv_processed.write(line)    
               else:
                    pass                       
           if 'OxSy' in line:
               if 'OxSy, OxSy' in line:
                   for i in range(round(RA_OxSy_OxSy_scaled)):
                       csv_processed.write(line)
               if 'Sx' in line:
                   for i in range(round(RA_OxSy_Sx_scaled)):
                       csv_processed.write(line)                       
           if 'Sx' in line:
               if 'Sx, Sx' in line:
                   for i in range(round(RA_Ox_Ox_scaled)):
                       csv_processed.write(line)
               else:
                    pass                       
       elif 'I' in line:
           if 'HC' in line:
               if 'HC, HC' in line:
                   for i in range(round(IAA_HC_HC_scaled)):
                       csv_processed.write(line)
               if 'Nx / NxOy' in line:
                   for i in range(round(IAA_HC_NxOy_scaled)):
                       csv_processed.write(line)
               if 'Ox' in line:
                   for i in range(round(IAA_HC_Ox_scaled)):
                       csv_processed.write(line)
               if 'OxSy' in line:
                   for i in range(round(IAA_HC_OxSy_scaled)):
                       csv_processed.write(line)
               if 'Sx' in line:
                   for i in range(round(IAA_HC_Sx_scaled)):
                       csv_processed.write(line)
               else:
                    pass                       
           if 'Nx / NxOy' in line:
               if 'Nx / NxOy, Nx / NxOy' in line:
                   for i in range(round(IAA_NxOy_NxOy_scaled)):
                       csv_processed.write(line)
               if 'Ox' in line:
                   for i in range(round(IAA_NxOy_Ox_scaled)):
                       csv_processed.write(line)
               if 'OxSy' in line:
                   for i in range(round(IAA_NxOy_OxSy_scaled)):
                       csv_processed.write(line)
               if 'Sx' in line:
                   for i in range(round(IAA_NxOy_Sx_scaled)):
                       csv_processed.write(line)
               else:
                    pass                       
           if 'Ox,' in line:
               if 'Ox, Ox' in line:
                   for i in range(round(IAA_Ox_Ox_scaled)):
                       csv_processed.write(line)
               if 'OxSy' in line:
                   for i in range(round(IAA_Ox_OxSy_scaled)):
                       csv_processed.write(line)   
               if 'Sx' in line:
                   for i in range(round(IAA_Ox_Sx_scaled)):
                       csv_processed.write(line)   
               else:
                    pass                      
           if 'OxSy' in line:
               if 'OxSy, OxSy' in line:
                   for i in range(round(IAA_OxSy_OxSy_scaled)):
                       csv_processed.write(line)
               if 'Sx' in line:
                   for i in range(round(IAA_OxSy_Sx_scaled)):
                       csv_processed.write(line)    
               else:
                    pass
           if 'Sx' in line:
               if 'Sx, Sx' in line:
                   for i in range(round(IAA_Ox_Ox_scaled)):
                       csv_processed.write(line)
               else:
                    pass
           else:
               pass
       else:
          pass

   csv_in.close()

csv_processed.close()

print(RA_HC_HC_scaled)