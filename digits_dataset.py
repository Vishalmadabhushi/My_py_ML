import numpy as np
from sklearn import datasets
digits=datasets.load_digits()
x=digits.data
y=digits.target
test_index=[4,183,363,543,723,903,1083,1263,1443,1623]
train_target=np.delete(digits.target,test_index)
train_data=np.delete(digits.data,test_index,axis=0)
test_target=digits.target[test_index]
test_data=digits.data[test_index]
from sklearn.neighbors import KNeighborsClassifier
my_clf=KNeighborsClassifier()
my_clf.fit(train_data,train_target) 
predictions=my_clf.predict(test_data)
from sklearn.metrics import accuracy_score
print(accuracy_score(test_target,predictions))
print(x)