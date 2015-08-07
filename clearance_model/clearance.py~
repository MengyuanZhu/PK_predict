import numpy
from scipy import stats
from sklearn.externals import joblib
x=numpy.loadtxt("clearance_property.txt")

clf=joblib.load('clearance.pkl')
model=clf.best_estimator_
importances = model.feature_importances_

for i in importances:
	print i



