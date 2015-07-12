import numpy
from scipy import stats
from sklearn.externals import joblib
x=numpy.loadtxt("mrt_property.txt")

clf=joblib.load('mrt.pkl')
model=clf.best_estimator_
num=0
for i in x[0:,0]:
	print i, clf.predict(x[0:,1:])[num]
	num=num+1
	



