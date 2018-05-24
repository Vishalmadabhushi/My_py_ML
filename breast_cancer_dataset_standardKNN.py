import random
from scipy.spatial import distance

from sklearn import datasets
breast_cancer=datasets.load_breast_cancer()
x=breast_cancer.data
y=breast_cancer.target
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)
from sklearn.neighbors import KNeighborsClassifier
my_clf=KNeighborsClassifier()
my_clf.fit(x_train,y_train) 
predictions=my_clf.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))
list(breast_cancer.target_names)

