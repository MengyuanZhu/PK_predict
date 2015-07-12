import numpy
from scipy import stats
from sklearn.externals import joblib
x=numpy.loadtxt("volume_property.txt")

clf=joblib.load('volume.pkl')
model=clf.best_estimator_

