import numpy
from scipy import stats
from sklearn.externals import joblib
x=numpy.loadtxt("t_half_property.txt")

clf=joblib.load('t_half.pkl')
model=clf.best_estimator_
importances = model.feature_importances_

feature= x[0:,1:]
target= x[0:,0]
num=0
for i in target:
	print i, round(model.predict(feature[num])[0],2)
	num=num+1
#for i in importances:
#	print i





