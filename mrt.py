####################Drug Mean Residence Time Prediction ############################
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



def run():
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


	model=joblib.load('mrt_model/mrt.pkl')

	for result in model.predict(value):
		return round(result,2)

print run()



