####################Drug Clearance Prediction ############################
#Author:Mengyuan Zhu, Binghe Wang
#Email: mzhu7@gsu.edu
#Department of Chemistry
#Georgia State University
#Usage: python mrt.py filename
##########################################################################

import numpy
from sklearn.externals import joblib
import pybel
import sys
import subprocess
import mrt
import t_half
import volume
inputfile=pybel.readfile(sys.argv[1].split(".")[-1],sys.argv[1])
value=()


for mol in inputfile:
	descvalues=mol.calcdesc()
	value= value+(descvalues.get('TPSA'),)
	value= value+(descvalues.get('HBD'),)
	value= value+(descvalues.get('logP'),)
	value= value+(descvalues.get('MW'),)
	value= value+(descvalues.get('tbonds'),)
	value= value+(descvalues.get('nF'),)
	value= value+(descvalues.get('bonds'),)
	value= value+(descvalues.get('atoms'),)
	value= value+(descvalues.get('HBA1'),)
	value= value+(descvalues.get('HBA2'),)
	value= value+(descvalues.get('sbonds'),)
	value= value+(descvalues.get('dbonds'),)
	value= value+(descvalues.get('MR'),)
	value= value+(descvalues.get('abonds'),)
	
	smarts = pybel.Smarts("[+]")
	num=smarts.findall(mol)				
	value= value+(len(num),)			
	
	smarts = pybel.Smarts("[-]")
	num=smarts.findall(mol)				
	value= value+(len(num),)

model=joblib.load('clearance_model/clearance.pkl')

value=value+(mrt.run(),)
value=value+(t_half.run(),)
value=value+(volume.run(),)

for result in model.predict(value):
	print "CL value:", round(result,2)
