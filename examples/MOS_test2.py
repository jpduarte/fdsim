#!/usr/bin/ipython
#from solver.drift_diffusion import J_solver1D
from solver.dev_sim import dev_solver2D
import numpy as np
import csv
import pickle

s = pickle.load(open('MOS_Vg0.00.dat','rb'))
cg = s.contact[0]
cs = s.contact[1]
cd = s.contact[2]
cb = s.contact[3]
m2 = s.meshes[2]

f = open("info2.csv",'wb')
writer = csv.writer(f)
step = 10
Vg = np.linspace(0,-1,step)

IDn   = np.empty(step)
IDp   = np.empty(step)
#IDn_t = np.empty(step)
#IDp_t = np.empty(step)

Ign   = np.empty(step)
Igp   = np.empty(step)
#Ign_t = np.empty(step)
#Igp_t = np.empty(step)

for n,V in enumerate(Vg):
   cg.V= V
   filename1 = "MOS_Vg{:.3F}.dat".format(V)
   output    = open(filename1,'wb')
   s.solve(1e-3,True,False)
   (IDn[n],IDp[n]) = (cd.Jn, cd.Jp)
   (Ign[n],Igp[n]) = (cg.Jn, cg.Jp)
   print ("**** VG={}, IDn={}, Ig={} ***".format(V,cd.Jn,cg.Jn))

   s.visualize(['Ec','Ev'])
   m2.cshow('n')

   pickle.dump(s,output)
   #s.solve(1e-3,True,True)
   #(IDn_t[n],IDp_t[n]) = (-cd.Jn, -cd.Jp)
   #(Ign_t[n],Igp_t[n]) = ( cg.Jn,  cg.Jp)
   #print ("**** tunneling: VG={}, IDn={}, Ig={} ***"
   #         .format(V,-cd.Jn,cg.Jn))

writer.writerow(Vg)
writer.writerow(IDn)
writer.writerow(IDp)
writer.writerow(Ign)
writer.writerow(Igp)
#writer.writerow(IDn_t)
#writer.writerow(IDp_t)
#writer.writerow(Ign_t)
#writer.writerow(Igp_t)