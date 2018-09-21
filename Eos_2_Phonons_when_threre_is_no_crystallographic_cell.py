#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import glob
import commands
import re
#global N_atom_irreducible_unit
#N_atom_irreducible_unit = 5

path='./'
filename = os.path.join(path, '*.out')
#filename = glob.glob(name)
for fname in glob.glob(filename):
  print fname

CRYSTAL_word = "CRYSTAL$"
Title_CRYSTAL_IFLAGs  = (commands.getstatusoutput("grep -C 1 '%s' %s"%(CRYSTAL_word, filename)))[1]
Space_Group = (commands.getstatusoutput("cat %s | grep '%s' -A2 | tail -n 1" %(filename, CRYSTAL_word)))[1]

print 'Title_CRYSTAL_IFLAGs = ', Title_CRYSTAL_IFLAGs
print 'Space_Group  = ', Space_Group
N_atom_irreducible_unit = (commands.getstatusoutput("cat %s | grep '%s' -A4 | tail -n 1" %(filename, CRYSTAL_word)))[1]
print 'N_atom_irreducible_unit = ', N_atom_irreducible_unit

VOLUMES = []
ET = []
TS = []
EL = []
E0 = []
VOLUME_EACH = []
T = []

print 'fname = ', fname
#sys.exit()
#with open(filename[0]) as gout:
with open(fname) as gout:
    final_optimized_geometry = False
    for line in gout:
        if 'FINAL OPTIMIZED GEOMETRY' in line:
            final_optimized_geometry = True
        elif 'PRIMITIVE CELL - CENTRING CODE' in line:
            if final_optimized_geometry:
                volume = line.split()
                print volume
                print volume[7]
                volume = line.split()[7]
                VOLUMES.append(volume)

        if re.match(r"^ ET            :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_ET = line[start:end]
         ET.append(result_ET)

        if re.match(r"^ TS            :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_TS = line[start:end]
         TS.append(result_TS)

        if re.match(r"^ EL            :", line):
         start = line.find(':') + 4
         end = line.find(':') + 22
         result_EL = line[start:end]
         EL.append(result_EL)

        if re.match(r"^ E0            :", line):
         start = line.find(':') + 8
         end = line.find(':') + 22
         result_E0 = line[start:end]
         E0.append(result_E0)

        if re.match(r"^ AT \(T =", line):
         start = line.find('T =') + 4
         end = line.find('K')
         result_Temperatures = line[start:end]
         T.append(result_Temperatures)



        final_optimized_geometry = False



print 'VOLUMES = ', VOLUMES
print 'T =', T
sys.exit()
