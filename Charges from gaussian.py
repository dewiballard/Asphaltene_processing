#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:52:05 2019

@author: dewiballard
"""

#########################Enter document name here############################
transform = 'DBSA.log'


import os
from decimal import *
#############################################################################


# Cut out part we need

data = open(transform, 'r')
file = data.read()

start = file.rfind('ESP charges:')
finish = file.rfind('Sum of ESP charges')

actual_start = start + 30
actual_finish = finish - 1

new_doc = file[actual_start:actual_finish]

charges = open('Charges.txt', 'w')
charges.write(new_doc)
charges.close()

#############################################################################

#convert to mol_mol format

charges2 = open('Charges2.txt', 'w')

with open('Charges.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            cutspaces = line[12:20] + line[9:11] + line[10:11] + line[8:9]
            cutspaces = cutspaces.strip('\n')
            charges2.write(cutspaces)
            charges2.write('  -1 F')
            charges2.write('\n')
            break
        
charges2.close()

#############################################################################

# round numbers
#swap c, n, s, o, h

charges3 = open('Charges3.txt', 'w')

with open('Charges2.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            replaceatoms = line[:]
            charges3.write(replaceatoms.replace('H', '2'))
            break
        
charges3.close()

charges4 = open('Charges4.txt', 'w')

with open('Charges3.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            replaceatoms = line[:]
            charges4.write(replaceatoms.replace('C', '3'))
            break
        
charges4.close()

charges5 = open('Charges5.txt', 'w')

with open('Charges4.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            replaceatoms = line[:]
            charges5.write(replaceatoms.replace('N', '4'))
            break
        
charges5.close()

charges6 = open('Charges6.txt', 'w')

with open('Charges5.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            replaceatoms = line[:]
            charges6.write(replaceatoms.replace('O', '5'))
            break
        
charges6.close()

charges7 = open('Charges7.txt', 'w')

with open('Charges6.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            replaceatoms = line[:]
            charges7.write(replaceatoms.replace('S', '8'))
            break
        
charges7.close()

charges8 = open('Charges8.txt', 'w')

with open('Charges7.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            replaceatoms = line[:]
            charges8.write(replaceatoms.replace(' 0.', '000.'))
            break
        
charges8.close()

charges9 = open('Charges9.txt', 'w')

with open('Charges8.txt','r') as f:
    for line in f:
        for i in enumerate(line):
            replaceatoms = line[:]
            charges9.write(replaceatoms.replace('-0.', '-00.'))
            break
        
charges9.close()

os.remove('Charges2.txt')
os.remove('Charges3.txt')
os.remove('Charges4.txt')
os.remove('Charges5.txt')
os.remove('Charges6.txt')
os.remove('Charges7.txt')
os.remove('Charges8.txt')

################# change F to T for atom types 4 and 5 #####################

charges10 = open('Charges10.txt', 'w')

with open('Charges9.txt', 'r') as f:
    for line in f:
        final = line[:]
        if line[12] == '4':
            charges10.write(final.replace('F', 'T'))
        elif line[12] == '5':
            charges10.write(final.replace('F', 'T'))
        else:
            charges10.write(final)

charges10.close

################### round to 4 decimal places instead of 5 ################

finalcharges = open('Finalcharges.txt', 'w')

with open('Charges10.txt', 'r') as f:
    for line in f:
        for i in enumerate(line):
            x = Decimal(line[2:9])
            '{}'.format(x.quantize(Decimal('.01'), rounding=ROUND_HALF_EVEN))
            a = round(x, 4)
            final = line[0:2] + str(a) + line[9:]
            finalcharges.write(final)
            break

finalcharges.write('Check mol2 file to find any hydrogens which are attached to O. If so, change atom number and -1 to -x')
finalcharges.close

###########################################################################